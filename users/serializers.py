from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .tasks import send_activation_code_celery, send_password_celery


User = get_user_model()

class ActivationLogOutSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(ModelSerializer):
    password_confirm = CharField(min_length=5, required=True, write_only=True)

    class Meta:
        model = User
        fields = 'username', 'email', 'password', 'password_confirm'

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1 != pass2:
            raise ValidationError('Passwords do not match!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code_celery.delay(user.email, user.activation_code)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length=4, required=True)
    new_password = serializers.CharField(min_length=4, required=True)
    new_password_confirm = serializers.CharField(min_length=4, required=True)

    def validate_old_password(self, old_password):
        request = self.context.get('request')
        user = request.user
        if not user.check_password(old_password):
            raise serializers.ValidationError(
                'Введите корректный пароль'
            )
        return old_password

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')

        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                'Пароли не совпадают'
            )
        if new_password == old_password:
            raise serializers.ValidationError(
                'Старый и новый пароли совпадают'
            )
        return attrs

    def set_new_password(self):
        new_password = self.validated_data.get('new_password')
        user = self.context.get('request').user
        user.set_password(new_password)
        user.save()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с таким email не найден')
        return attrs

    def send_verification_email(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_forgot_password_code()
        send_password_celery.delay(user.email, user.forgot_password_code)
        return user 


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=4, required=True)
    password_confirm = serializers.CharField(min_length=4, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if not User.objects.filter(email=email, forgot_password_code=code).exists():
            raise serializers.ValidationError('Пользователь не найден или неправильный код')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.forgot_password_code = ''
        user.save()


class SetTokenSerializer(serializers.Serializer):
    fcm_token = serializers.CharField()

    def save(self, **kwargs):
        user = User.objects.get(id=self.context.get('request').user.id)
        user.fcm_token = self.initial_data['fcm_token']
        user.save()
from rest_framework import serializers
from apps.games.models.submit_games_models import SubmitGame
from apps.games.models.games import Tags, Game, GameImage, GameApplication, Date


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'title')


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'date')


class GameImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameImage
        fields = ('id', 'image')


class GameSerializer(serializers.ModelSerializer):
    images = GameImageSerializer(many=True, read_only=True)
    tags = TagSerializer(read_only=True)
    date = DateSerializer(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'title', 'region', 'price', 'images', 'description', 'tags', 'date', 'max_people')


class GameCardSerializer(serializers.ModelSerializer):
    images = GameImageSerializer(many=True, read_only=True)
    date = DateSerializer(read_only=True)

    class Meta:
        model = Game
        fields = ('images', 'price', 'title', 'date', 'max_people')


class SubmitSerializer(serializers.ModelSerializer):
    game = GameCardSerializer(read_only=True)

    class Meta:
        model = SubmitGame
        fields = ('id', 'game', 'added_at')

class GameApplicationSerializers(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)

    class Meta:
        model = GameApplication
        fields = ('id', 'phone_number', 'full_name', 'date', 'people_count', 'status')


class PriceRangeSerializer(serializers.Serializer):
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2)

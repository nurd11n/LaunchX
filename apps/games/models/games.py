from datetime import timedelta
from django.core.validators import RegexValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from apps.games.tasks import application_send_mail


class Tags(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тег')

    def __str__(self):
        return self.title
    

class Date(models.Model):
    date = models.DateField(verbose_name="Дата")


class Game(models.Model):
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, verbose_name='Теги',null=True)
    title = models.CharField(max_length=70, verbose_name="Название тура")
    region = models.CharField(max_length=255, verbose_name="Область и Страна")
    description = models.TextField(verbose_name="Описание")
    max_people = models.PositiveIntegerField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    date = models.ForeignKey(Date, on_delete=models.CASCADE, verbose_name="Дата")
    time = models.CharField(max_length=100)
    views = models.PositiveBigIntegerField(default=0, verbose_name='Просмотры')
    archived = models.BooleanField(default=False, verbose_name="Архивирован")

    def __str__(self):
        return self.title

    def check_and_archive(self):
        today = timezone.now().date()
        if (self.date.date <= today - timedelta(days=7)) or (self.date.date < today):
            self.archived = True
            self.save()


class GameImage(models.Model):
    game = models.ForeignKey(Game, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='game_images/', verbose_name="Изображение")


class GameApplication(models.Model):
    Status = (
        ('pending', 'Не рассмотрено'),
        ('reviewed', 'Рассмотрено'),
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(regex=r'^\+996\d{9}$',
                                   message="Format: '+996XXXXXXXXX'. Up to 12 digits allowed.")], verbose_name='Номер Телефона')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата')
    people_count = models.PositiveIntegerField(verbose_name='Количество человек', default=1, null=True, validators=[MaxValueValidator(50)])
    status = models.CharField(max_length=50, choices=Status, default='pending', verbose_name='Статус')

    def max_people_count(self, game):
        game = self.game
        if self.people_count > game.max_people:
            raise ValueError
        
    def save(self, *args, **kwargs):
        self.max_people_count(self.game)
        data = {
            'phone_number': self.phone_number,
            'full_name': self.full_name,
            'game': self.game.title,
            'games_date': f'Real date {self.game.date} -> Users Date {self.date}',
            'games_time': self.game.time,
            'games_max_people': self.game.max_people,
            'people_count': self.people_count,
        }
        application_send_mail.delay(data)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

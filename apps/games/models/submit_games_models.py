from django.db import models
from django.contrib.auth import get_user_model

from .games import Game

User = get_user_model()


class SubmitGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено в избранное")

    def __str__(self):
        return f"{self.user} - {self.game.title}"

    @staticmethod
    def submit(user, game):
        submit, created = SubmitGame.objects.get_or_create(user=user, game=game)
        return submit, created

    @staticmethod
    def remove_submit(user, game):
        SubmitGame.objects.filter(user=user, game=game).delete()

    @staticmethod
    def submited(user, game):
        return SubmitGame.objects.filter(user=user, game=game).exists()
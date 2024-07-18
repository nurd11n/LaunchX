from modeltranslation.translator import TranslationOptions, register
from apps.games.models.games import Game, Tags


@register(Tags)
class TagsTranslationOptions(TranslationOptions):
    fields = ('title',)
    
    
@register(Game)
class GameTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'region', )

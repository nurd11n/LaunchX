from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.games.models.games import Game, GameApplication, GameImage, Tags, Date


class TranslatorMediaMixin(TranslationAdmin):
    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }

class GameImageInline(admin.TabularInline):
    model = GameImage
    extra = 1

@admin.register(Game)
class GameAdmin(TranslatorMediaMixin, admin.ModelAdmin):
    inlines = [GameImageInline]
    list_display = ['title', 'date', 'archived']
    list_filter = ['archived']
    search_fields = ['title', 'description']
    fields = ('title', 'region', 'price', 'description', 'tags',
              'date', 'archived',)

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('image'):
            obj.save_image()
        super().save_model(request, obj, form, change)
        obj.check_and_archive()

@admin.register(Tags)
class TagsAdmin(TranslatorMediaMixin):
    list_display = ('id', 'title',)
    list_display_links = ("id",)
    search_fields = ['title',]

admin.site.register(GameImage)
admin.site.register(GameApplication)
admin.site.register(Date)
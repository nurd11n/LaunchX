import asyncio
from googletrans import Translator

translator = Translator()


class TranslationMixin:
    fields_to_translate = []

    async def translate_text(self, text, lang):
        translated_text = await asyncio.sleep(0, translator.translate(text, src='ru', dest=lang))
        return translated_text.text

    async def translate_fields(self):
        tasks = []
        for field_name in self.fields_to_translate:
            text = getattr(self, field_name)
            languages = ['en', 'ky', 'zh-tw']
            tasks.extend([self.translate_text(text, lang) for lang in languages])
        translations = await asyncio.gather(*tasks)
        for i, field_name in enumerate(self.fields_to_translate):
            for j, lang in enumerate(languages):
                translated_text = translations[i * len(languages) + j]
                setattr(self, f"{field_name}_{lang}" if lang != 'zh-tw' else f"{field_name}_zh_hant", translated_text)

    def save(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.translate_fields())
        super().save(*args, **kwargs)
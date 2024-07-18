import io
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.fields.files import ImageFieldFile
import uuid


class WEBPFieldFile(ImageFieldFile):
 
    def save(self, name, content, save=True):
        content.file.seek(0)
        image = Image.open(content.file)
        image_bytes = io.BytesIO()
        image.save(fp=image_bytes, format="webp")
        image_content_file = ContentFile(content=image_bytes.getvalue())
        super().save(name, image_content_file, save)
 
 
class WEBPField(models.ImageField):
    attr_class = WEBPFieldFile

def image_folder(instance, filename,):
    return '{}_image/{}.webp'.format(instance.__class__.__name__.lower(), uuid.uuid4().hex)
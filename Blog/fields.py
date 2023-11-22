import io
from random import randrange

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.fields.files import ImageFieldFile


class PNGFieldFile(ImageFieldFile):

    def save(self, name, content, save=True):
        content.file.seek(0)
        image = Image.open(content.file)

        watermark = Image.open("staticfiles/images/watermark.png")
        place = (randrange(image.size[0]), randrange(image.size[1]))
        image.paste(watermark, place, mask=watermark)

        image_bytes = io.BytesIO()
        image.save(fp=image_bytes, format="PNG")
        image_content_file = ContentFile(content=image_bytes.getvalue())
        super().save(name, image_content_file, save)


class PNGField(models.ImageField):
    attr_class = PNGFieldFile

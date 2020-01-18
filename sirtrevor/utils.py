from functools import partial
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def resize_image_attachment(file_, size=(1024, 9999)):
    try:
        temp = BytesIO()
        image = Image.open(file_)
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(temp, 'jpeg')
        temp.seek(0)
        return SimpleUploadedFile(file_.name, temp.read(), content_type='image/jpeg')
    except Exception as ex:
        return file_


def resize_image_attachment_processor(w, h):
    return partial(resize_image_attachment, size=(w, h))

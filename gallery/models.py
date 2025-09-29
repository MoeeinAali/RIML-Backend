from django.db import models
from django.core.validators import FileExtensionValidator
from pathlib import Path
import uuid


def gallery_image_path(instance, filename):
    ext = (Path(filename).suffix or "").lower().lstrip(".")
    ext = ext or "jpg"
    return f"gallery/images/{instance.id}.{ext}"


class GalleryImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=gallery_image_path,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])],
    )
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

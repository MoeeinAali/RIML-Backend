from django.db import models
from django.core.validators import FileExtensionValidator
from pathlib import Path
from core.models import TeamMember


def field_image_path(instance, filename):
    ext = (Path(filename).suffix or "").lower().lstrip(".")
    ext = ext or "jpg"
    return f"club/fields/{instance.name}.{ext}"


def journal_image_path(instance, filename):
    ext = (Path(filename).suffix or "").lower().lstrip(".")
    ext = ext or "jpg"
    return f"club/journals/{instance.name}.{ext}"


class ResearchField(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=field_image_path,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])],
    )
    markdown = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class JournalClub(models.Model):
    class AttendanceType(models.TextChoices):
        IN_PERSON = "in_person"
        ONLINE = "online"
        HYBRID = "hybrid"

    title = models.CharField(max_length=255)
    markdown = models.TextField(blank=True)
    presenter = models.ForeignKey(
        TeamMember, on_delete=models.SET_NULL, null=True, blank=True, related_name="journal_clubs"
    )
    date = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=255, blank=True)
    attendance_type = models.CharField(
        max_length=16, choices=AttendanceType.choices, default=AttendanceType.IN_PERSON
    )
    research_fields = models.ManyToManyField(
        ResearchField, blank=True, related_name="journal_clubs"
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=journal_image_path,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

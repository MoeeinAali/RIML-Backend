from django.db import models
from django.utils.text import slugify
from core.models import TeamMember


def publisher_logo_image_path(instance, filename):
    ext = (filename.rsplit('.', 1)[-1] or '').lower()
    name_slug = slugify(instance.name or '')
    year_slug = slugify(instance.year or '')
    return f"publishers/{name_slug}/{name_slug}-{year_slug}.{ext}"


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField(blank=True, null=True)
    logo = models.ImageField(null=True, blank=True, upload_to=publisher_logo_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.year}" if self.year else self.name


class Publication(models.Model):
    title = models.TextField()
    authors = models.TextField(blank=True, null=True)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, blank=True, null=True, related_name="publications")
    team_members = models.ManyToManyField(
        TeamMember, blank=True, null=True, related_name="publications")
    badges = models.ManyToManyField(
        "PublicationBadge",
        blank=True,
        related_name="publications",
        through="PublicationBadgeLink",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PublicationBadge(models.Model):
    name = models.CharField(max_length=127)
    label = models.CharField(max_length=127)
    link = models.CharField(max_length=127)
    
    def __str__(self):
        return self.name


class PublicationBadgeLink(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    badge = models.ForeignKey(PublicationBadge, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("publication", "badge")

    def __str__(self):
        return f"{self.publication} ↔ {self.badge}"
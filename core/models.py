from django.db import models
from django.utils.text import slugify


def team_member_image_path(instance, filename):
    ext = (filename.rsplit('.', 1)[-1] or '').lower()
    first_name_slug = slugify(instance.first_name or '')
    last_name_slug = slugify(instance.last_name or '')
    return f"team_members/{first_name_slug}-{last_name_slug}-{instance.id}.{ext}"


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ForeignKey(
        Team,
        related_name="members",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to=team_member_image_path, null=True, blank=True)
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(max_length=255, blank=True)
    github_url = models.URLField(max_length=255, blank=True)
    twitter_url = models.URLField(max_length=255, blank=True)
    website_url = models.URLField(max_length=255, blank=True)
    scholar_url = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

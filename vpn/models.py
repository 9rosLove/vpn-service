from django.db import models

from core import settings


class Site(models.Model):
    name = models.CharField(max_length=63, blank=True)
    url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sites",
    )

    class Meta:
        unique_together = ("created_by", "url")
        ordering = ["-created_at"]

    @property
    def get_short_url(self):
        return self.url if len(self.url) < 26 else self.url[:23] + "..."

    def __str__(self):
        return f"{self.name}: {self.get_short_url}"

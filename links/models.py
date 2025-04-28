from django.db import models
from users.models import User

class Link(models.Model):
    LINK_TYPES = (
        ('website', 'Website'),
        ('book', 'Book'),
        ('article', 'Article'),
        ('music', 'Music'),
        ('video', 'Video'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="links")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    image = models.URLField(blank=True, null=True)
    link_type = models.CharField(max_length=20, choices=LINK_TYPES, default='website')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'url')

    def __str__(self):
        return self.title

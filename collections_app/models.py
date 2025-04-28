from django.db import models
from users.models import User
from links.models import Link

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    links = models.ManyToManyField(Link, related_name="collections")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

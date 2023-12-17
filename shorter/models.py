from django.db import models
from django.contrib.auth.models import User



class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_url = models.URLField()
    short_code = models.CharField(max_length=8, unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_click = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        # return self.user.username + ' ' + self.short_code
        return self.short_code
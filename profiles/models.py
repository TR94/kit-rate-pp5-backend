from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Profile model based on the DRF walkthough project from Code Institute
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_iwm3kr'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

# uses django signals to create a user profile, calling
# create_profile function and expecting signal from User model
post_save.connect(create_profile, sender=User)

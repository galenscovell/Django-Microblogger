from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=24)
    content = models.TextField(max_length=120)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    favorites = models.SmallIntegerField(default=0)

    def update(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    # Each comment is related to a single Post
    post = models.ForeignKey(Post)
    author = models.ForeignKey('auth.user')
    content = models.CharField(max_length=60)
    created_at = models.DateTimeField(default=timezone.now)
    votes = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.id)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    post_count = models.PositiveSmallIntegerField(default=0)
    comment_count = models.PositiveSmallIntegerField(default=0)
    karma = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.user.username


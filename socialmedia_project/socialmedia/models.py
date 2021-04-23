from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    image = models.ImageField(upload_to="images", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Profile'
        verbose_name = 'profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    p_date = models.DateTimeField(auto_now_add=True)
    u_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.p_date = timezone.now()
        self.u_date = timezone.now()
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-post']

    def __str__(self):
        return str(self.comment)[:30]


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requirement_comment_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField()

    class Meta:
        db_table = 'Like'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Like


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    comment = serializers.StringRelatedField(many=True)
    like = serializers.SerializerMethodField('get_likes')
    comment_count = serializers.SerializerMethodField('count_comment')

    def get_likes(self, Post):
        like = Like.objects.filter(post=Post)
        return like.count()

    def count_comment(self, Post):
        comment = Comment.objects.filter(post=Post)
        return comment.count()

    class Meta:
        model = Post
        fields = ['id', 'title', 'owner', 'p_date', 'u_date', 'comment', 'like', 'comment_count']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'owner', 'post', 'comment']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'owner', 'post', 'like']

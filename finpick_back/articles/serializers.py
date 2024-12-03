from rest_framework import serializers
from .models import Article, Comment

# 게시글(Article)
class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

# 댓글(Comment)
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'

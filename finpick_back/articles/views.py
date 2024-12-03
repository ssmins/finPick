from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from .models import Article

# 게시글 목록을 GET 요청으로 가져오는 API
@api_view(['GET'])
def get_articles(request): 
    articles = Article.objects.all() 
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

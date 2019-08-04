from rest_framework import serializers

from Article.models import Article, Revisions


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class RrevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revisions
        fields = '__all__'
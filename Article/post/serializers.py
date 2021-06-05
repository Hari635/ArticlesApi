from datetime import datetime
from django.db import models
from django.db.models import fields
from django.utils.timesince import timesince
from rest_framework import serializers
from .models import Author,Article

class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication=serializers.SerializerMethodField()

    class Meta:
        model=Article
        exclude=("id",)

    def get_time_since_publication(self,object):
        publication_date=object.publication_date
        now =datetime.now()
        time_delta=timesince(publication_date,now)
        return time_delta
    def validate(self, data):
        if(data["title"]==data["description"]):
            raise serializers.ValidationError("Title and Description must be different from one another!")
        return data
    def validate_title(self,value):
        if len(value) < 30:
            raise serializers.ValidationError("The title has to be at least 30 chars long!")
        return value


class AuthorSerializer(serializers.ModelSerializer):
     articles = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="article-detail")

     class Meta:
         model =Author
         fields="__all__"

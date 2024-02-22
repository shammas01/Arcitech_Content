from rest_framework import serializers
from useraccount.models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id','user','title','body','summary','document','categories']
    

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.body = validated_data.get('body',instance.body)
        instance.summary = validated_data.get('summary',instance.summary)
        instance.document = validated_data.get('document',instance.document)
        instance.categories.set(validated_data.get('categories', instance.categories.all()))
        instance.save()
        return instance
import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        #fields = "__all__"
        fields = ("title", "content", "cat")

    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())













"""
Звичайний серілізатор, написаний на базовому класі
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    # PUT
    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    # PUT
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance

    #DELETE
    def delete(self, validated_data):
        return Women.objects.delete(**validated_data)

"""



"""
class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = WomenModel('Lina Kostenko', 'Content: Lina Kostenko biography')
    model_sr = WomenSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json, type(json), sep='\n')

def decode():
    stream = io.BytesIO(b'{"title":"Lina Kostenko","content":"Content: Lina Kostenko biography"}')
    data = JSONParser().parse(stream)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
    
"""
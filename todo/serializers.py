from rest_framework.serializers import ModelSerializer
from .models import Books, Author


class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["author"] = instance.author.all().values()
        return rep


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

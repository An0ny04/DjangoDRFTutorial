from rest_framework.serializers import ModelSerializer
from .models.author import Author
from .models.books import Books
from django.contrib.auth.models import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


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

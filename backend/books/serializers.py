from rest_framework import serializers
<<<<<<< HEAD
=======

>>>>>>> a143f0374d71ef02dd748a53a45e4e3d43aabb8e
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.copies += validated_data.get("copies", 0)
        instance.save()
        return instance
>>>>>>> a143f0374d71ef02dd748a53a45e4e3d43aabb8e

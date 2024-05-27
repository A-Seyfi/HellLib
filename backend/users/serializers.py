from books.serializers import BookSerializer
from rest_framework import serializers

<<<<<<< HEAD
from .models import Student, BorrowRecord
=======
from .models import BorrowRecord, Student
>>>>>>> 90cd2125caf7336f50e0b1f29f5ab58dba177e72


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class BorrowRecordSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    class Meta:
        model = BorrowRecord
        fields = "__all__"
=======
    student = StudentSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = BorrowRecord
        fields = "__all__"


class BorrowRecordSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        exclude = ["is_returned"]
>>>>>>> 90cd2125caf7336f50e0b1f29f5ab58dba177e72

<<<<<<< HEAD
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['POST'])
def AddBook(request : Request):
    serializer = BookSerializer(data = request.data)

    title = serializer.initial_data['title']
    publisher = serializer.initial_data['publisher']
    author = serializer.initial_data['author']
    copies = serializer.initial_data['copies']

    book = Book.objects.filter(title = title, publisher = publisher, author = author).first()

    if serializer.is_valid() and book == None:
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        book.copies += copies
        book.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
=======
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BooksAPIView(ListCreateAPIView):
    serializer_class = BookSerializer

    def perform_create(self, serializer: serializer_class):

        book = Book.objects.filter(
            title=serializer.validated_data["title"],
            publisher=serializer.validated_data["publisher"],
            author=serializer.validated_data["author"],
        ).first()

        if book is not None:
            return serializer.update(book, serializer.validated_data)

        return serializer.save()

    def get_queryset(self):
        return Book.objects.all()


class SearchBooks(ListAPIView):
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        queryset = (
            Book.objects.annotate(
                similarity=TrigramSimilarity("title", kwargs["title"]),
            )
            .filter(similarity__gt=0.2)
            .order_by("-similarity")
        )

        serializer = self.serializer_class(queryset, many=True)

        return Response({"books": serializer.data}, status=status.HTTP_200_OK)
>>>>>>> a143f0374d71ef02dd748a53a45e4e3d43aabb8e

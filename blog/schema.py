# schema is like a serializer
# describe a data model
import graphene
from graphene_django import DjangoObjectType
from blog.models import Books

class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "author")

class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)

    def resolve_all_books(root, info):
        return Books.objects.all()
schema = graphene.Schema(query=Query)
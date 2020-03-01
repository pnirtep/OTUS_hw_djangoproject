from django.urls import path
from graphene_django.views import GraphQLView
from . import schema
import graphene
import courses_gql.schema


class Query(courses_gql.schema.Query, graphene.ObjectType):
    pass


class Mutation(courses_gql.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

urlpatterns = [
    path('', GraphQLView.as_view(graphiql=True, schema=schema)),
]

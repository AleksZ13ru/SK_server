import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Build


class BuildType(DjangoObjectType):
    class Meta:
        model = Build
        filter_fields = ['build_services', 'machine__name']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    build = relay.Node.Field(BuildType)
    builds = DjangoFilterConnectionField(BuildType)

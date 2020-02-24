import graphene
from graphene_django import DjangoObjectType

from .models import Machine


class MachineType(DjangoObjectType):
    class Meta:
        model = Machine

    extra_field = graphene.Int()


class MyMachineType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    speed = graphene.Int()
    kmv = graphene.Int()


class Query(graphene.ObjectType):
    machines = graphene.List(MyMachineType)
    machines0 = graphene.List(MachineType)

    def resolve_machines0(self, info, **kwargs):
        return Machine.objects.all()

    def resolve_machines(self, info, **kwargs):
        machines = Machine.objects.all()
        result = []
        for m in machines:
            result.append({
                'id': m.pk,
                'name': m.name,
                'speed': 1,
                'kmv': 12
            })

        return result

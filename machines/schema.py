import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Machine, Value


class MachineType(DjangoObjectType):
    class Meta:
        model = Machine
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'comment': ['exact', 'icontains', 'istartswith'],
            # 'value__day': ['exect'],
        }
        interfaces = (relay.Node,)


class ValueType(DjangoObjectType):
    class Meta:
        model = Value
        filter_fields = ['day', 'machine__name']
        interfaces = (relay.Node,)

    speed = graphene.Int()
    kmv = graphene.Float()

    # todo: как то не правильно организован вызов... нет подсветки на self.create_speed()
    def resolve_speed(self, info):
        return self.create_speed()

    # todo: как то не правильно организован вызов... нет подсветки на self.create_kmv()
    def resolve_kmv(self, info):
        return self.create_kmv()


class Query(graphene.ObjectType):
    machine = relay.Node.Field(MachineType)
    machines = DjangoFilterConnectionField(MachineType)
    value = relay.Node.Field(ValueType)
    values = DjangoFilterConnectionField(ValueType)

    # machines = graphene.List(MachineType)
    # machine = graphene.Field(MachineType, pk=graphene.String())
    # values = graphene.List(ValueType, day=graphene.String())
    # value = graphene.Field(ValueType, day=graphene.String())

    # def resolve_machines(self, info, **kwargs):
    #     result = Machine.objects.all()
    #     return result
    #
    # def resolve_machine(self, info, pk):
    #     return Machine.objects.get(pk=pk)
    #
    # def resolve_values(self, info, day=None):
    #     if day is None:
    #         return Value.objects.all()
    #     else:
    #         return Value.objects.filter(day=day)
    #
    # def resolve_value(self, info, day):
    #     return Value.objects.filter(day=day).first()

import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Manufacturing, ProductionArea, Machine, Value


class ManufacturingType(DjangoObjectType):
    class Meta:
        model = Manufacturing
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)


class ProductionAreaType(DjangoObjectType):
    class Meta:
        model = ProductionArea
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)


# todo: добавить поле выбора избранного оборудования
class MachineType(DjangoObjectType):
    class Meta:
        model = Machine
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'comment': ['exact', 'icontains', 'istartswith'],
            # 'value__day': ['exect'],
        }
        interfaces = (relay.Node,)

    location = graphene.String()
    area = graphene.String()

    def create_manufacturing(self):
        return self.create_manufacturing()

    def create_area(self):
        return self.create_area()

    def resolve_location(self, info):
        return self.create_manufacturing()

    def resolve_area(self, info):
        return self.create_area()


class ValueType(DjangoObjectType):
    class Meta:
        model = Value
        filter_fields = ['day', 'machine__name']
        interfaces = (relay.Node,)

    speed = graphene.Int()
    kmv = graphene.Float()
    status = graphene.String()

    def create_speed(self):
        return self.create_speed()

    def create_kmv(self):
        return self.create_kmv()

    def resolve_speed(self, info):
        return self.create_speed()

    def resolve_kmv(self, info):
        return self.create_kmv()

    # green: 'success',
    # blue: 'info',
    # red: 'danger'
    def resolve_status(self, info):
        return "red"


class Query(graphene.ObjectType):
    manufacturing = relay.Node.Field(ManufacturingType)
    manufacturings = DjangoFilterConnectionField(ManufacturingType)
    production_area = relay.Node.Field(ProductionAreaType)
    production_areas = DjangoFilterConnectionField(ProductionAreaType)
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

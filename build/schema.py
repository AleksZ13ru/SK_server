import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Build
from users.schema import UserType
from machines.schema import MachineType, DeveloperType
from machines.models import Machine

class BuildType(DjangoObjectType):
    class Meta:
        model = Build
        filter_fields = ['build_services', 'machine__name']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    build = relay.Node.Field(BuildType)
    builds = DjangoFilterConnectionField(BuildType)


class BuildAdd(graphene.Mutation):
    machine = graphene.Field(MachineType)
    date = graphene.Date()
    timeStart = graphene.Time()
    timeEnd = graphene.Time()
    text = graphene.String()
    comment = graphene.String()
    build_services = graphene.Field(DeveloperType)
    posted_by = graphene.Field(UserType)

    class Arguments:
        machine_id = graphene.Int()

        text = graphene.String()
        service = graphene.String()

    def mutate(self, info, machine_id, date, time_start, time_end, text, service):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged to vote!')

        machine = Machine.objects.filter(id=machine_id).first()
        if not machine:
            raise Exception('Invalid Machine!')

        event = Build.objects.create(
            machine=machine,
            date=date,
            timeStart=time_start,
            timeEnd=time_end,
            text=text,
            service=service,
            posted_by=user,
        )

        return BuildAdd(
            machine=machine,
            text=text,
            service=service,
            posted_by=user,
        )

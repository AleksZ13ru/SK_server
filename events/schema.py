import graphene
from graphene_django import DjangoObjectType

from events.models import Event, Status
from machines.models import Machine

from users.schema import UserType
from machines.schema import MachineType


class EventsType(DjangoObjectType):
    class Meta:
        model = Event


class StatusType(DjangoObjectType):
    class Meta:
        model = Status


class Query(graphene.ObjectType):
    events = graphene.List(EventsType)
    statuses = graphene.List(StatusType)

    def resolve_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_statuses(self, info, **kwargs):
        return Status.objects.all()


class CreateEvent(graphene.Mutation):
    machine = graphene.Field(MachineType)
    text = graphene.String()
    service = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        machine_id = graphene.Int()
        text = graphene.String()
        service = graphene.String()

    def mutate(self, info, machine_id, text, service):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged to vote!')

        machine = Machine.objects.filter(id=machine_id).first()
        if not machine:
            raise Exception('Invalid Machine!')

        event = Event.objects.create(
            machine=machine,
            text=text,
            service=service,
            posted_by=user,
        )

        Status.objects.create(
            event=event,
            text='Открыта',
            comment='',
            posted_by=user
        )

        return CreateEvent(
            machine=machine,
            text=text,
            service=service,
            posted_by=user,
        )


class CreateStatus(graphene.Mutation):
    event = graphene.Field(EventsType)
    text = graphene.String()
    comment = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        event_id = graphene.Int()
        text = graphene.String()
        comment = graphene.String()

    def mutate(self, info, event_id, text, comment):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged to vote!')

        event = Event.objects.filter(id=event_id).first()
        if not event:
            raise Exception('Invalid Event!')

        Status.objects.create(
            event=event,
            text=text,
            comment=comment,
            posted_by=user
        )
        return CreateStatus(
            event=event,
            text=text,
            comment=comment,
            posted_by=graphene.Field(UserType)
        )


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
    create_status = CreateStatus.Field()

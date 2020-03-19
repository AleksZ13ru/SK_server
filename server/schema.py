import graphene
import graphene
import graphql_jwt

import machines.schema
import users.schema
import events.schema
import build.schema


class Query(users.schema.Query, events.schema.Query, machines.schema.Query, build.schema.Query, graphene.ObjectType):
    pass


# events.schema.Mutation,
class Mutation(users.schema.Mutation, graphene.ObjectType, ):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

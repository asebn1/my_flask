import graphene

class User(graphene.ObjectType):
    # Add something here
    name = graphene.String(required=True)
    description = graphene.String()

class Query(graphene.ObjectType):
    user = graphene.Field(User, name=graphene.String())

    def resolve_user(self, info, name):
        return User(name="admin",
                       description="I'm an admin I can do anything")

schema = graphene.Schema(query=Query)


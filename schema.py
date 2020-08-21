import graphene

class User(graphene.ObjectType):
    # Add something here

class Query(graphene.ObjectType):
    user = graphene.Field(User, name=graphene.String())

    def resolve_user(self, info, name):
        return Website(name="admin",
                       description="I'm an admin I can do anything")

schema = graphene.Schema(query=Query)


import graphene

class SecretUser(graphene.ObjectType):
    name = graphene.String(required=True)
    description = graphene.String(deprecation_reason="I don't need this field anymore, it has a sensitive data")
    secretfield = graphene.String()

class User(graphene.ObjectType):
    name = graphene.String(required=True)

class Query(graphene.ObjectType):
    user = graphene.Field(User, name=graphene.String())

    def resolve_user(self, info, name):
        return User(name="admin")

class QuerySecret(graphene.ObjectType):
    user = graphene.Field(SecretUser, name=graphene.String())

    def resolve_user(self, info, name):
        return SecretUser(name="admin",
                       description="I'm an admin I can do anything")

IS_AUTHENTICATED = True

if IS_AUTHENTICATED == True:
    schema = graphene.Schema(query=QuerySecret)
else:
    schema = graphene.Schema(query=Query)


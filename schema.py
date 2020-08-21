mport graphene

class User(graphene.ObjectType):
	hello = graphene.String(name=graphene.String(default_value="World"))
	def resolve_hello(self, info, name):
		return 'Hello ' + name

class Query(graphene.ObjectType):
    user = graphene.Field(User, name=graphene.String())

    def resolve_user(self, info, name):
        return Website(name="admin",
                       description="I'm an admin I can do anything")

schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
print(result.data['hello']) # "Hello World"

import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Product as ProductModel

class Product(MongoengineObjectType):

    class Meta:
        model = ProductModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    GetProducts = graphene.List(Product, name=graphene.String(), code=graphene.Int(), cost=graphene.Int(), amount=graphene.Int(), )
    def resolve_GetProducts(self, info, **kwargs):
        return list(ProductModel.objects.filter(**kwargs))

class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        code = graphene.Int(required=True)
        amount = graphene.Int(required=True)
        cost = graphene.Int(required=True)
        
    product = graphene.Field(Product)

    def mutate(self, info, **kwargs):
        product = ProductModel(**kwargs)
        product.save()
        return CreateProduct(product=product)

class DeleteProduct(graphene.Mutation):
    class Arguments:
        code = graphene.Int(required=True)
        
    product = graphene.Field(Product)

    def mutate(self, info, code):
        product = ProductModel.objects(code=code).first()
        if product is not None:
            product.delete()
        return DeleteProduct(product=product)

class UpdateProductCost(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        code = graphene.Int(required=True)
        cost = graphene.Int(required=True)
        
    product = graphene.Field(Product)

    def mutate(self, info, name, code, cost):
        product = ProductModel.objects(name=name, code=code).first()
        if product is not None:
            product.update(cost=cost)
        return UpdateProductCost(product=product)

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    delete_product = DeleteProduct.Field()
    update_product_cost = UpdateProductCost.Field()

schema = graphene.Schema(query=Query, types=[Product], mutation=Mutation)


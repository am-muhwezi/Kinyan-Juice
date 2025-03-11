from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
from ..models.products import Product
from flask_jwt_extended import jwt_required, get_jwt_identity

product_namespace = Namespace(
    'product', description="namespace for all Product")

product_model = product_namespace.model(
    'Product',{
        'id':fields.Integer(description='The unique id of a product'),
        'name':fields.String(description='The name of a product'),
        'price':fields.Float(description='The price of a product'),
        'description':fields.String(description='The description of a product')
    })

@product_namespace.route('/products')
class GetCreateProducts(Resource):


    @product_namespace.marshal_with(product_model)
    @jwt_required(optional=True)
    def get(self):
        """
        Get all Products
        """
        products = Product.query.all()
        return products, HTTPStatus.OK

    @product_namespace.expect(product_model)
    @product_namespace.marshal_with(product_model)
    @jwt_required()
    def post(self):
        """
        Create a new Product
        """
        user_identity=get_jwt_identity()

        data=product_namespace.payload

        new_product=Product(
            name=data['name'],
            price=data['price'],
            description=data['description']
        )

        new_product.save()

        return new_product, HTTPStatus.CREATED

    def put(self):
        pass

    def update(self):
        pass

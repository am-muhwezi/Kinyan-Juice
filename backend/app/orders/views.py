from flask_restx import Namespace, Resource, fields


orders_namespace = Namespace(
    'orders', description="namespace for all orders")



@orders_namespace.route('/orders')
class Orders(Resource):

    def get(self):
        """
        Get all orders
        """
        pass

    def post(self):
        """
        Create a new order
        """
        pass
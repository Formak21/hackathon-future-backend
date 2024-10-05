from src.controllers import user, auth

def configure_routes(app):
    app.register_blueprint(auth.bp, url_prefix='/auth')
    app.register_blueprint(user.bp, url_prefix='/users')
    # app.register_blueprint(product_controller.bp, url_prefix='/products')
    # app.register_blueprint(order_controller.bp, url_prefix='/orders')
    # app.register_blueprint(auth_controller.bp, url_prefix='/auth')
    # app.register_blueprint(category_controller.bp, url_prefix='/categories')
    # app.register_blueprint(review_controller.bp, url_prefix='/reviews')
    # app.register_blueprint(cart_controller.bp, url_prefix='/cart')
    # app.register_blueprint(payment_controller.bp, url_prefix='/payment')
    # app.register_blueprint(shipment_controller.bp, url_prefix='/shipment')
    # app.register_blueprint(notification_controller.bp, url_prefix='/notifications')
    # app.register_blueprint(admin_controller.bp, url_prefix='/admin')

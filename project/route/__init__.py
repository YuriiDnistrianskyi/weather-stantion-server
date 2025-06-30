from flask import Flask

def register_routes(app: Flask) -> None:
    from project.route.orders.user_route import user_bp
    from project.route.orders.group_route import group_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(group_bp)

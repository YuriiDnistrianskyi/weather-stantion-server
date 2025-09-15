from flask import Flask

def register_routes(app: Flask) -> None:
    from project.route.orders.user_route import user_bp
    from project.route.orders.group_route import group_bp
    from project.route.orders.user_grop_route import user_group_bp
    from project.route.orders.weather_station_route import weather_station_bp
    from project.route.orders.info_route import info_bp

    from project.route.orders.get_max_min_temperature_route import get_max_min_temperature_bp

    from project.auth.routes import auth_bp

    from project.route.error_handle import error_handle_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(group_bp)
    app.register_blueprint(user_group_bp)
    app.register_blueprint(weather_station_bp)
    app.register_blueprint(info_bp)

    app.register_blueprint(get_max_min_temperature_bp)

    print("init auth")
    app.register_blueprint(auth_bp)

    app.register_blueprint(error_handle_bp)

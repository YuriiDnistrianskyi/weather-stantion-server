from flask_mail import Mail, Message
from project import mail

def exceeding_hing_temperature_email(email: str, weather_station_name: str, temperature: float) -> None:
    text = f"Your weather station {weather_station_name} has detected an excess high temperature " \
           f"of {temperature} degrees. Please, lower the temperature to make the climate more comfortable."

    message = Message (
        subject='Exceeding temperature on weather station',
        recipients=[email],
        body=text
    )
    mail.send(message)

def exceeding_low_temperature_email(email: str, weather_station_name: str, temperature: float) -> None:
    text = f"Your weather station {weather_station_name} has detected an excess low temperature " \
           f"of {temperature} degrees. Please, turn up the temperature to make the climate more comfortable."

    message = Message (
        subject='Exceeding low temperature on weather station',
        recipients=[email],
        body=text
    )
    mail.send(message)

# def return_to_normal_high_temperature_email(email: str, weather_station_name: str, temperature: float) -> None:
#     pass
#
# def return_to_normal_low_temperature_email(email: str, weather_station_name: str, temperature: float) -> None:
#     pass

import smtplib
def get_distance(time_seconds: int | float, velocity_meters_per_second: int | float) -> float:
    distance = time_seconds * velocity_meters_per_second * 1.0
    distance = round(distance, 2)
    return distance

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import jinja2
import config


def send_email(
    recipients: list[str],
    mail_body: str,
    mail_subject: str,
):
    TOKEN = config.TOKEN_UKR_NET
    USER = config.USER_UKR_NET
    SMTP_SERVER = config.SMTP_SERVER

    msg = MIMEMultipart("alternative")

    msg["Subject"] = mail_subject
    msg["From"] = f"<Email was sent from {USER}>"
    msg["To"] = ", ".join(recipients)
    msg["Reply-To"] = USER
    msg["Return-Path"] = USER

    text_to_send = MIMEText(mail_body, "html")

    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)

    mail.login(USER, TOKEN)

    mail.sendmail(
        USER,
        recipients,
        msg.as_string(),
    )

    mail.quit()


def create_string_report(data: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath="./")

    template_env = jinja2.Environment(
        loader=template_loader
    )

    template_file = "templates/string.html"

    template = template_env.get_template(
        template_file
    )

    output = template.render(data)

    return output
def print_msg() -> None:
    print('Welcome')
    print('message')
    # return
    # return None


def get_number_5() -> int:  # int float str list dict None
    print('function get_number_5 was called')
    number_5_to_give = 5
    return number_5_to_give


def foo():
    return


def calculate_summa(number_1: int | float, number_2: int | float) -> float:
    result = number_1 + number_2
    return result * 1.0


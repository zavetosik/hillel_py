import utils

from pywebio.input import input
from pywebio.input import input_group
from pywebio.output import put_success

from pywebio import start_server
from pywebio.session import run_js


def main():
    data = input_group(
        "Send String",
        [
            input("Name", name="name", required=True),
            input("String", name="content", required=True),
            input("Email", name="email", required=True),
        ]
    )

    content = data["content"].strip()

    email_body = utils.create_string_report(
        {
            "name": data["name"],
            "content": content,
            "length": len(content),
        }
    )

    utils.send_email(
        [data["email"]],
        email_body,
        mail_subject="String Length",
    )

    put_success("Email was sent. The page reloads in 5 seconds...")

    run_js("""
        setTimeout(() => {
            window.location.reload()
        }, 5000);
    """)


start_server(
    main,
    host="0.0.0.0",
    port=8888,
    debug=True,
)
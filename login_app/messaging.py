from django.core.mail import send_mail

def email_message(message_dict):
    contents = f"""
    Hi, thank you for trying to reset your password.
    Click this link to reset your password: {message_dict['reset_link']}
    """
    send_mail(
        'Password reset link',
        contents,
        'miklasbogvald@gmail.com',
        [message_dict['email_reciever']],
        fail_silently = False
    )
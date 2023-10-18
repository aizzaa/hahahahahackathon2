from django.core.mail import send_mail


def send_code(email, code):
    send_mail(
        'Активация аккаунта',
        f'Вы успешно зарегистрировались на нашем сайте. Активируетй аккаунт. Код активации: {code}',
        'test@gmail.com',
        [email]
    )


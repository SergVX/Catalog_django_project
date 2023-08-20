import json
from django.conf import settings
from django.core.mail import send_mail


def send_email_100(post_title):
    """Функция для отправки письма на электронную почту"""
    send_mail('Поздравляем!',  # Тема письма
              f"Дорогой администратор! Количество просмотров поста {post_title} достигло 100, мои поздравления",
              settings.EMAIL_HOST_USER,  # От кого письмо
              recipient_list=['virus-xe@yandex.ru'])

def save_contact_data(name, phone, message):
    contact_data = {
        'name': name,
        'phone': phone,
        'message': message
    }

    with open('contact_data.json', 'a', encoding='UTF-8') as file:
        json.dump(contact_data, file, ensure_ascii=False)
        file.write('\n')
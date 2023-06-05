import json


def save_contact_data(name, phone, message):
    contact_data = {
        'name': name,
        'phone': phone,
        'message': message
    }

    with open('contact_data.json', 'a', encoding='UTF-8') as file:
        json.dump(contact_data, file, ensure_ascii=False)
        file.write('\n')
import requests
from connectionBD import get_user

# Токен доступа к Битрикс24
access_token = 'ваш_токен_доступа'

# Адрес веб-хука для получения данных о контакте
webhook_url = ''

# Адрес метода для обновления контакта
update_url = ''

# Функция-обработчик веб-хука
def webhook_handler(data):
    
    contact_id = data['result'][0]['ID']
    contact_name = data['result'][0]['NAME']

    # Заполнить имя таблицы
    table_user = ""
    gender = get_user(table_user, contact_id)

    # Обновление контакта в Битрикс24
    if gender:
        update_data = {
            'id': contact_id,
            'fields': {
                'gender_in_birix': gender  # Замените 'gender_in_birix' на код своего пользовательского поля для хранения пола
            }
        }
    update_result = requests.post(update_url, headers={'Authorization': f'Bearer {access_token}'}, json=update_data).json()

    # Вывод Id, Name и пола контакта в консоль
    print(f'Id контакта: {contact_id}')
    print(f'Name контакта: {contact_name}')
    print(f'Пол контакта: {gender}')

# Получение данных из Битрикс24 по веб-хуку
webhook_data = requests.get(webhook_url, headers={'Authorization': f'Bearer {access_token}'}).json()

# Вызов функции-обработчика веб-хука
if __name__=="__main__":
    webhook_handler(webhook_data)
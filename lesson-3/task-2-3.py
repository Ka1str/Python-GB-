def print_information_about_user(name='гость', surname='не указана', year='не указан', city='не указан',
                                 email='не указан', phone_number='не указан'):
    """
    Принимает данные пользователя как именнованные аргументы
    :param name: имя
    :param surname: фамилия
    :param year: год рождения (int)
    :param city: город
    :param email: email
    :param phone_number: телефон
    :return: str
    """
    return print(
        f'Имя - {name}, фамилия - {surname}, год рождения - {year}, город - {city},'
        f' email - {email}, номер телефона - {phone_number}')


user_name = input('как вас зовут?')
user_surname = input('ваша фамилия?')
user_year = int(input('ваш год рождения?'))
user_city = input('ваш город проживания?')
user_email = input('ваш email?')
user_phone_number = input('ваш номер телефона?')
print_information_about_user(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email,
                             phone_number=user_phone_number)

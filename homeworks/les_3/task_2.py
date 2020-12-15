# homework lesson: 3, task:2

"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.

Функция должна принимать параметры как именованные аргументы.

Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(name: str,
              surname: str,
              birth_year: int,
              city: str,
              email: str,
              phone: int
              ):
    """
    Отображает данные о пользователе на экране
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: None
    """
    return f"{name} {surname} {birth_year} года рождения, " \
           f"в городе {city}. Контакты: {email}, {phone} "


def user_data_kw(**kwargs) -> str:
    """
    Отображает данные о пользователе на экране
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: str
    """

    name = kwargs.get('name', '')
    surname = kwargs.get('surname', '')
    birth_year = kwargs.get('birth_year', '')
    city = kwargs.get('city', '')
    email = kwargs.get('email', '')
    phone = kwargs.get('phone', '')

    return f"{name} {surname} {birth_year} года рождения, в городе {city}. Контакты: {email}, {phone} "

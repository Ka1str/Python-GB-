def check_for_latin(string):
    """
    Проверка на латинский алфавит
    :param string: str
    :return: True or False
    """
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    not_eng = None
    for one_char in string:
        if one_char not in alphabet:
            not_eng = True
    if not_eng == True:
        return False
    else:
        return True


def title_func(user_text):
    """
    Проверяет str на нижний регистр и на латинский алфавит
    Делает str с прописной первой буквой
    :param user_text: str
    :return: print str
    """
    if user_text.islower() and check_for_latin(user_text) == True:
        user_text = user_text.title()
        return print(user_text)
    return print('Ввели слово не из маленьких латинских букв')


def title_list_func(user_text):
    """
    Делает из list - str
    :param user_text: list
    :return: title_func(user_text)
    """
    separator = ' '
    user_text = separator.join(user_text)
    return title_func(user_text)


user_word = input('введите слово из маленьких латинских букв')
title_func(user_word)
user_split_text = input('введите строку из слов из латинских букв в нижнем регистре, разделенных пробелом').split()
title_list_func(user_split_text)

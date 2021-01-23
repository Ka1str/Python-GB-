def int_func(user_text):
    """
    Проверяет на нижний регистр и на латинский алфавит
    Делает str с прописной первой буквой
    :param user_text: str/list
    :return: print str
    """
    if type(user_text) == list:
        separator = ' '
        user_text = separator.join(user_text)

    latin_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                      "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    not_latin = False

    for letter in user_text:
        if letter not in latin_alphabet:
            not_latin = True

    if user_text.islower() and not_latin == False:
        user_text = user_text.title()
        return print(user_text)
    else:
        return print('Ввели слово/слова не из маленьких латинских букв')


user_word = input('введите слово из маленьких латинских букв')
int_func(user_word)
user_split_text = input('введите строку из слов из латинских букв в нижнем регистре, разделенных пробелом').split()
int_func(user_split_text)

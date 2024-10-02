#функция проверки на правильность ввода (англ)
def is_correct_eng(player_word):
    player_word = player_word.upper()
    ru_alph = {"А": 1, "Б": 1, "В": 1, "Г": 1, "Д": 1, "Е": 1, "Ё": 1, "Ж": 1, "З": 1, "И": 1,
               "Й": 1, "К": 1, "Л": 1, "М": 1, "Н": 1, "О": 1, "П": 1, "Р": 1, "С": 1, "Т": 1,
               "У": 1, "Ф": 1, "Х": 1, "Ц": 1, "Ч": 1, "Ш": 1, "Щ": 1, "Ъ": 1, "Ы": 1, "Ь": 1,
               "Э": 1, "Ю": 1, "Я": 1}

    if any(letter in player_word for letter in ru_alph):
        #print("use english")
        return 1

    if not player_word.isalpha():
        #print("use letters")
        return 2
    #all good
    return 0

#функция подсчета очков (англ)
def count_eng(player_word):
    player_word = player_word.upper()
    eng_alph = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "S": 1, "T": 1, "R": 1,
                "D": 2, "G": 2,
                "B": 3, "C": 3, "M": 3, "P": 3,
                "F": 4, "H": 4, "V": 4, "W": 4,
                "K": 5,
                "J": 8, "X": 8,
                "Q": 10, "Z": 10}

    res = 0
    if is_correct_eng(player_word) == 0:
        for j in player_word:
            res += eng_alph[j]
        output_text = "The value of your word is " + str(res) + "!"
        return output_text
    if is_correct_eng(player_word) == 1:
        return "Use only English/Switch the language"
    if is_correct_eng(player_word) == 2:
        return "Use only letters!"

#функция проверки на правильность ввода (рус)
def is_correct_ru(player_word):
    player_word = player_word.upper()
    eng_alph = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "S": 1, "T": 1, "R": 1,
                "D": 2, "G": 2,
                "B": 3, "C": 3, "M": 3, "P": 3,
                "F": 4, "H": 4, "V": 4, "W": 4,
                "K": 5,
                "J": 8, "X": 8,
                "Q": 10, "Z": 10}
    ru_alph = {"А": 1, "Б": 1, "В": 1, "Г": 1, "Д": 1, "Е": 1, "Ё": 1, "Ж": 1, "З": 1, "И": 1,
               "Й": 1, "К": 1, "Л": 1, "М": 1, "Н": 1, "О": 1, "П": 1, "Р": 1, "С": 1, "Т": 1,
               "У": 1, "Ф": 1, "Х": 1, "Ц": 1, "Ч": 1, "Ш": 1, "Щ": 1, "Ъ": 1, "Ы": 1, "Ь": 1,
               "Э": 1, "Ю": 1, "Я": 1}
    if any(letter in player_word for letter in eng_alph):
        #print("используйте русский")
        return 1

    sum_word = 0
    for j in player_word:
        if j in ru_alph:
            sum_word += 1
    if sum_word != len(player_word):
        #print("используйте буквы"
        return 2
    else:
        #всё правильно
        return 0

#функция подсчета очков (рус)
def count_ru(player_word):
    player_word = player_word.upper()
    ru_alph = {"А" : 1, "В" : 1, "Е" : 1, "И" : 1, "Н" : 1, "О" : 1, "Р" : 1, "С" : 1, "Т" : 1,
               "Д" : 2, "К" : 2, "Л" : 2, "М" : 2, "П" : 2, "У" : 2,
               "Б" : 3, "Г" : 3, "Ё" : 3, "Ь" : 3, "Я" : 3,
               "Й" : 4, "Ы" : 4,
               "Ж" : 5, "З" : 5, "Х" : 5, "Ц" : 5, "Ч" : 5,
               "Ш" : 8, "Э" : 8, "Ю" : 8,
               "Ф" : 10, "Щ" : 10, "Ъ" : 10}
    res = 0
    if is_correct_ru(player_word) == 0:
        for j in player_word:
            res += ru_alph[j]
        output_text = "Стоимость вашего слова равна " + str(res) + "!"
        return output_text
    if is_correct_ru(player_word) == 1:
        return "Используйте русский/Смените язык"
    if is_correct_ru(player_word) == 2:
        return "Используйте только буквы!"

# pip install googletrans==3.1.0a0
from googletrans import Translator


def translate_01():
    str_01 = input("Enter a sentence to translate: ")
    translator = Translator()
    try:
        ru_to_en = translator.translate(str_01, src='ru', dest='en')
        en_to_ru = translator.translate(str_01, src='en', dest='ru')
        ru_to_ua = translator.translate(str_01, src='ru', dest='uk')
        print('ru_to_en:', ru_to_en.text)
        print('en_to_ru:', en_to_ru.text)
        print('ru_to_ua:', ru_to_ua.text)

    except BaseException as err:
        print(f"Unexpected error: {err}, {type(err)}")


translate_01()

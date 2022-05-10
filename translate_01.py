# pip install googletrans==3.1.0a0
from googletrans import Translator


def translate_01():
    str_01 = input("Enter a sentence to translate: ")
    translator = Translator()
    try:
        result = translator.translate(str_01, src='ru', dest='en')
        print('src:', result.src)
        print('dest:', result.dest)
        print('text:', result.text)

    except BaseException as err:
        print(f"Unexpected error: {err}, {type(err)}")


translate_01()

from translate import Translator

while True:
    source = input("Enter the name of source file: ")
    source = f'{source}.txt'
    lang = input('Enter the output Language: ')
    lang = (lang[:2:]).lower()
    try:
        with open(source, mode='r') as my_file:
            a = my_file.read()

        with open('output.txt', "w", encoding="utf-8") as my_file2:
            translator = Translator(to_lang=lang)
            translation = translator.translate(a)
            my_file2.write(translation)
        break
    except FileNotFoundError:
        print("Incorrect File Name.")
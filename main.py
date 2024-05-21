

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    match i:= input("Enter 1 for Audio Adapter, 2 for Plug Adapter, 3 for Language Translator: "):
        case "1":
            import audio_adapter
        case "2":
            import plug_adapter
        case "3":
            import langauge_translator
        case _:
            print("Invalid Input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

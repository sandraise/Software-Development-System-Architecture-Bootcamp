class English:

    def translate(self):
        return "Hello!"

class French:

    def translate(self):
        return "Bonjour!"

class Spanish:

    def translate(self):
        return "Hola!"

def translate_word(phrase):
    print(phrase.translate())

eng = English()
fr = French()
sp = Spanish()

translate_word(eng)
translate_word(fr)
translate_word(sp)
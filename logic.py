from translate import Translator
import requests
from collections import defaultdict


qwestions = {'как тебя зовут' : "Я супер-крутой-бот и мое ппредназначение помогать тебе!",
             "сколько тебе лет" : "Это слишком философский вопрос"}

class TextAnalysis():   
    
    memory = defaultdict(list)

    def __init__(self, text, owner):
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")
        self.translation_ru = self.__translate(self.text, "en", "ru")
        self.translation_de = self.__translate(self.text, "ru", "de")
        self.translation_zh = self.__translate(self.text, "ru", "zh")
        
        if self.text.lower() in qwestions.keys():
            self.response = qwestions[self.text.lower()]
        else:
            self.response = self.get_answer()


    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang,to_lang=to_lang )
            translate = translator.translate(text)
            return translate
        except:
            return "Перевод не удался"


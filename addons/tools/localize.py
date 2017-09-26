import json

class LocalizeMe():
    def __init__(self, folder : str, base : str):
        self.folder = folder
        self.base = base
    
    def get(self, string : str, lang : str = None):
        if lang is None:
            lang = self.base
        file = open(self.folder + "/" + lang + ".json", "r")
        text = file.read()
        file.close()
        js = json.loads(text)
        return js[string]

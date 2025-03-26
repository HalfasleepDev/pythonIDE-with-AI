from PyQt6.QtCore import QThread
from PyQt6.Qsci import QsciAPIs
from jedi import Script
from jedi.api import Completion


class AutoCompleter(QThread):
    def __init__(self, file_path, api):
        super(AutoCompleter, self).__init__(None)
        self.file_path = file_path
        self.script: Script = None #TODO: disect how it works
        self.api: QsciAPIs = api
        self.completions: list[Completion] = None #TODO: disect how it works
        
        
        self.line = 0
        self.index = 0
        self.text = ""

    def run(self):
        try:
            self.script = Script(self.text, path=self.file_path) #TODO: disect how it works
            #print(self.script, "script") #Print to see what it ig getting
            self.completions = self.script.complete(self.line, self.index) #TODO: disect how it works
            #print(self.completions, " completeions") #Print to see what it ig getting
            self.load_autocomplete(self.completions) 
        except Exception as err:
            print(err)

        self.finished.emit() 

    def load_autocomplete(self, completions): #TODO: disect how it works
        self.api.clear()
        [self.api.add(i.name) for i in completions] 
        self.api.prepare() 

    def get_completions(self, line: int, index: int, text: str): #TODO: disect how it works
        self.line = line
        print(line, " line") #Print to see what it is getting
        self.index = index
        print(index, " index") #Print to see what it is getting
        self.text = text
        #print(text.splitlines()[line]) #Print to see what it is getting
        #print(Editor.text(line))
        self.start()

class GenerateFromPrompt(QThread):
    def __init__(self, file_path, api):
        super(AutoCompleter, self).__init__(None)


    '''def run(self):
        try:

        except Exception as err:
            print(err)'''
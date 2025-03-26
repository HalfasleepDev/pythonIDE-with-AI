import sys
import argparse
import torch
from transformers import T5ForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM,RobertaTokenizer
import re
import pprint
from collections import OrderedDict
'''sys.path.insert(0, '/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE')'''
from MainWindow import Ui_MainWindow
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
#TODO: make into a class

app = QApplication([])

class GenCode(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GenCode, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #parse arguments
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument('--output_path', type=str, help="")
        self.parser.add_argument('--start_index', type=int, default=0, help="")
        self.parser.add_argument('--end_index', type=int, default=164, help="")
        self.parser.add_argument('--temperature', type=float, default=0.5, help="")
        self.parser.add_argument('--N', type=int, default=200, help="")
        self.parser.add_argument('--max_len', type=int, default=600, help="")
        self.parser.add_argument('--decoding_style', type=str, default='sampling', help="")
        self.parser.add_argument('--num_seqs_per_iter', type=int, default=50, help='')
        self.parser.add_argument('--overwrite', action='store_true', help='')


        self.args = self.parser.parse_args()

        self.argsdict = vars(self.args)
        print(pprint.pformat(self.argsdict))

        # initialization of the model for generateCodeGeneral()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.currDevice1 = self.device
        self.dtype1 = torch.float16
        self.currDevice = "cpu"
        self.dtype = torch.float32
        self.currDevice2 = "cpu"
        self.dtype2 = torch.float32

        self.ui.TextToText.currentIndexChanged.connect(self.tTTIndexChanged)
        self.ui.CodeToCode.currentIndexChanged.connect(self.cTCIndexChanged)
        self.ui.Summerize.currentIndexChanged.connect(self.SummerizeIndexChanged)



        '''self.checkpoint = "Salesforce/codet5p-770m-py"

        self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint)
        self.model = T5ForConditionalGeneration.from_pretrained(self.checkpoint,
                                                        torch_dtype=self.dtype,
                                                        low_cpu_mem_usage=True).to(self.currDevice) # and a setting to alternate between cpu and gpu

        self.tokenizer.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")
        self.model.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")

        self.tokenizer = AutoTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")

        # initialization of the model for codeQuestion()
        self.checkpoint1 = "Salesforce/codet5p-2b"

        self.tokenizer1 = AutoTokenizer.from_pretrained(self.checkpoint1)
        self.model1 = AutoModelForSeq2SeqLM.from_pretrained(self.checkpoint1,
                                                    torch_dtype=self.dtype1,
                                                    low_cpu_mem_usage=True,
                                                    trust_remote_code=True).to(self.currDevice1)

        self.tokenizer1.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")
        self.model1.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")

        self.tokenizer1 = AutoTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")

        # initialization of the model for codeSummarize()
        self.checkpoint2 = 'Salesforce/codet5-base-multi-sum'

        self.tokenizer2 = RobertaTokenizer.from_pretrained(self.checkpoint2)
        self.model2 = T5ForConditionalGeneration.from_pretrained(self.checkpoint2,
                                                                torch_dtype=self.dtype2,
                                                                low_cpu_mem_usage=True).to(self.currDevice2)

        self.tokenizer2.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")
        self.model2.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")

        self.tokenizer2 = RobertaTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")'''

        '''self.loadModel1()
        self.loadModel2()
        self.loadModel3()'''

    def loadModel1(self):
        self.checkpoint = "Salesforce/codet5p-770m-py"

        self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint)
        self.model = T5ForConditionalGeneration.from_pretrained(self.checkpoint,
                                                        torch_dtype=self.dtype,
                                                        low_cpu_mem_usage=True).to(self.currDevice) # and a setting to alternate between cpu and gpu

        self.tokenizer.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")
        self.model.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")

        self.tokenizer = AutoTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")
    
    def loadModel2(self):
        self.checkpoint1 = "Salesforce/codet5p-2b"

        self.tokenizer1 = AutoTokenizer.from_pretrained(self.checkpoint1)
        self.model1 = AutoModelForSeq2SeqLM.from_pretrained(self.checkpoint1,
                                                    torch_dtype=self.dtype1,
                                                    low_cpu_mem_usage=True,
                                                    trust_remote_code=True).to(self.currDevice1)

        self.tokenizer1.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")
        self.model1.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")

    def loadModel3(self):
        self.checkpoint2 = 'Salesforce/codet5-base-multi-sum'

        self.tokenizer2 = RobertaTokenizer.from_pretrained(self.checkpoint2)
        self.model2 = T5ForConditionalGeneration.from_pretrained(self.checkpoint2,
                                                                torch_dtype=self.dtype2,
                                                                low_cpu_mem_usage=True).to(self.currDevice2)

        self.tokenizer2.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")
        self.model2.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")

        self.tokenizer2 = RobertaTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")
####################################################################
    def tTTIndexChanged(self, index):
        match index:
            case 0:
                print("action")
                self.currDevice1 = self.device
                self.dtype1 = torch.float16
                del self.model1
                self.loadModel2()
            case 1:
                print("action")
                self.currDevice1 = "cpu"
                self.dtype1 = torch.float32
                del self.model1
                self.loadModel2()
                print("action")
            case _:
                self.currDevice1 = self.device
                self.dtype1 = torch.float16
                del self.model1
                self.loadModel2()
    def cTCIndexChanged(self, index):
        match index:
            case 0:
                self.currDevice = "cpu"
                self.dtype = torch.float32
                del self.model
                self.loadModel1()
            case 1:
                self.currDevice = self.device
                self.dtype = torch.float16
                del self.model
                self.loadModel1()
            case _:
                self.currDevice = "cpu"
                self.dtype = torch.float32
                del self.model
                self.loadModel1()
    def SummerizeIndexChanged(self, index):
        match index:
            case 0:
                self.currDevice2 = "cpu"
                self.dtype2 = torch.float32
                del self.model2
                self.loadModel3()
            case 1:
                self.currDevice2 = self.device
                self.dtype2 = torch.float16
                del self.model2
                self.loadModel3()
            case _:
                self.currDevice2 = "cpu"
                self.dtype2 = torch.float32
                del self.model2
                self.loadModel3()



    # generate code general
    def generateCodeGeneral(self, userSentence):
        encoding = self.tokenizer(userSentence, truncation=True, max_length=self.args.max_len, return_tensors="pt").to(self.currDevice)
        encoding['decoder_input_ids'] = encoding['input_ids'].clone()
        outputs = self.model.generate(**encoding, 
                                max_length=self.args.max_len,
                                temperature=self.args.temperature,
                                #eos_token_id=tokenizer.eos_token_id,
                                top_p=0.95,
                                do_sample=True)
        sentenceOutput = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return str.strip(re.sub("'''", '',re.sub(userSentence,'', sentenceOutput)))


    # progrmaming questions
    def codeQuestion(self,userSentence):
        encoding = self.tokenizer1(userSentence, truncation=True, max_length=self.args.max_len, return_tensors="pt").to(self.currDevice1)
        encoding['decoder_input_ids'] = encoding['input_ids'].clone()
        outputs = self.model1.generate(**encoding,
                                        max_length=self.args.max_len//2,
                                        do_sample=True,
                                        temperature=self.args.temperature,
                                        eos_token_id=self.tokenizer.eos_token_id,
                                        top_p=0.95,
                                        encoder_repetition_penalty=0.5,
                                        top_k=self.args.max_len, #fix
                                        num_return_sequences=2,
                                        #decoder_start_token_id=tokenizer.pad_token_id,
                                        min_length=10)
        sentenceOutput = (self.tokenizer1.decode(outputs[0], skip_special_tokens=True))
        check =  str.strip(re.sub('"', '',re.sub(userSentence,'', sentenceOutput)))
        return "\n".join(list(OrderedDict.fromkeys(check.split("\n"))))

    #Summarizing code
    def codeSummarize(self, userCode):
        encoding = self.tokenizer2(userCode, truncation=True, max_length=self.args.max_len, return_tensors="pt").to(self.currDevice2)

        outputs = self.model2.generate(**encoding,
                                        max_length=self.args.max_len,
                                        do_sample=True,
                                        temperature=self.args.temperature,
                                        eos_token_id=self.tokenizer.eos_token_id,
                                        top_p=0.95,
                                        top_k=self.args.max_len, 
                                        num_return_sequences=10,
                                        no_repeat_ngram_size=2,
                                        early_stopping=True,
                                        min_length=10)
        sentenceOutput = self.tokenizer2.decode(outputs[0], skip_special_tokens=True)
        return sentenceOutput

    #Optimizing code
    def codeOptimize(self, userSentence, userCode): #This probably doesn't work... :(
        encoding = self.tokenizer1(userSentence, truncation=True, max_length=self.args.max_len, return_tensors="pt").to(self.currDevice1)
        encoding_decoder = self.tokenizer([userSentence + userCode], truncation=True, max_length=self.args.max_len, return_tensors="pt").to(self.currDevice1)
        outputs = self.model1.generate(**encoding,
                                    decoder_input_ids=encoding_decoder['input_ids'],
                                    max_length=self.args.max_len,
                                    do_sample=True,
                                    temperature=self.args.temperature,
                                    eos_token_id=self.tokenizer.eos_token_id,
                                    top_p=0.95,
                                    #encoder_repetition_penalty=0.6,
                                    #top_k=args.max_len, #fix
                                    decoder_start_token_id=self.tokenizer.pad_token_id,
                                    min_length=10)
        sentenceOutput = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return str.strip(re.sub("'''", '',re.sub(userSentence,'', sentenceOutput)))

    #must run on gpu default
    def codeCompletion(line, index):
        pass

    #must run on gpu default
    def autoDoc(tbd):
        pass


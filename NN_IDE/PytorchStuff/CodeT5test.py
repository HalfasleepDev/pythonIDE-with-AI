import torch
from transformers import T5ForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM, RobertaTokenizer
from accelerate import init_empty_weights
import argparse
import pprint
from collections import OrderedDict
import gc
import os
import re
from tqdm import tqdm

#os.environ['TF_FORCE_GPU_ALLOW_GROWTH']='true'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:1024"

getOption = input('choose model to test')
parser = argparse.ArgumentParser()

#parser.add_argument('--model', type=str, default='Salesforce/codet5p-770m-py', help="")

parser.add_argument('--output_path', type=str, help="")
parser.add_argument('--start_index', type=int, default=0, help="")
parser.add_argument('--end_index', type=int, default=164, help="")
parser.add_argument('--temperature', type=float, default=0.7, help="")
parser.add_argument('--N', type=int, default=200, help="")
parser.add_argument('--max_len', type=int, default=600, help="")
parser.add_argument('--decoding_style', type=str, default='sampling', help="")
parser.add_argument('--num_seqs_per_iter', type=int, default=50, help='')
parser.add_argument('--overwrite', action='store_true', help='')

args = parser.parse_args()

INSTRUCTION = """Below is an instruction that describes a task. Write a response that appropriately completes the request.


### Instruction:
Create a Python script for this problem:
{}

### Response:"""

'''argsdict = vars(args)
print(pprint.pformat(argsdict))

if args.decoding_style == 'sampling':
    loops = int(args.N / args.num_seqs_per_iter)
else:
    loops = 1'''

match int(getOption):
    case 1:
        #Code generation
        checkpoint = "Salesforce/codet5p-770m-py"


        tokenizer = RobertaTokenizer.from_pretrained(checkpoint)
        model = T5ForConditionalGeneration.from_pretrained(checkpoint,
                                                        torch_dtype=torch.float16,
                                                        low_cpu_mem_usage=True).to(device)

        tokenizer.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")
        model.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")

        tokenizer = RobertaTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")

        userSentence = "Optimize this python code for performance"
        userCode = '''Optimize this python code for performance:
        def calc( num1, num2):    
            result = 0    
            for i in range(num1, num2):       
                result += ((i+1) * (i+2))    
                return result'''
        prompt = (userSentence, userCode)

        print(torch.cuda.memory_allocated()/1024**2)
        encoding = tokenizer(userCode, truncation=True, max_length=args.max_len, return_tensors="pt").to(device)
        encoding['decoder_input_ids'] = encoding['input_ids'].clone()
        outputs = model.generate(**encoding, 
                                    max_length=args.max_len,
                                    temperature=args.temperature,
                                    eos_token_id=tokenizer.eos_token_id,
                                    top_p=0.95,
                                    do_sample=True)
        sentenceOutput = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(str.strip(re.sub("'''", '',re.sub(userSentence,'', sentenceOutput))))
        print(torch.cuda.mem_get_info())

    case 2:
        #Text to text explanation
        checkpoint = "Salesforce/codet5p-2b"



        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint,
                                              torch_dtype=torch.float16,
                                              low_cpu_mem_usage=True,
                                              trust_remote_code=True).to(device)

        tokenizer.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")
        model.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")

        tokenizer = AutoTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")

        userSentence = "What is the syntax for a function in Python"
        userSentenceDec = [userSentence + userSentence]

        print(torch.cuda.memory_allocated()/1024**2)
        
        encoding = tokenizer(userSentence, truncation=True, max_length=args.max_len, return_tensors="pt").to(device)
        encoding['decoder_input_ids'] = encoding['input_ids'].clone()
        outputs = model.generate(**encoding,
                                        max_length=args.max_len//3,
                                        do_sample=True,
                                        temperature=args.temperature,
                                        eos_token_id=tokenizer.eos_token_id,
                                        top_p=0.95,
                                        encoder_repetition_penalty=0.6,
                                        top_k=args.max_len//3, #fix
                                        decoder_start_token_id=tokenizer.pad_token_id,
                                        min_length=10)
        sentenceOutput = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(str.strip(re.sub("'''", '',re.sub(userSentence,'', sentenceOutput))))
        print(torch.cuda.mem_get_info())

    case 3:
        #Code sumarization
        checkpoint = 'Salesforce/codet5-base-multi-sum'

        tokenizer = RobertaTokenizer.from_pretrained(checkpoint)
        model = T5ForConditionalGeneration.from_pretrained(checkpoint,
                                                        torch_dtype=torch.float16,
                                                        low_cpu_mem_usage=True).to(device)

        tokenizer.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")
        model.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")

        tokenizer = RobertaTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")

        userSentence = """def svg_to_image(string, size=None):
    if isinstance(string, unicode):
        string = string.encode('utf-8')
        renderer = QtSvg.QSvgRenderer(QtCore.QByteArray(string))
    if not renderer.isValid():
        raise ValueError('Invalid SVG data.')
    if size is None:
        size = renderer.defaultSize()
        image = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
        painter = QtGui.QPainter(image)
        renderer.render(painter)
    return image"""
        encoding = tokenizer(userSentence, truncation=True, max_length=args.max_len, return_tensors="pt").to(device)

        outputs = model.generate(**encoding,
                                    max_length=args.max_len,
                                    do_sample=True,
                                    temperature=args.temperature,
                                    eos_token_id=tokenizer.eos_token_id,
                                    top_p=0.95,
                                    top_k=args.max_len, #fix
                                    no_repeat_ngram_size=2,
                                    #remove_invalid_values=True,
                                    early_stopping=True,
                                    min_length=10)
        sentenceOutput = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(str.strip(re.sub("'''", '',re.sub(userSentence,'', sentenceOutput))))
        print(torch.cuda.mem_get_info())
#Code Optimization
    case 4:
        #Text to text explanation
        checkpoint = "Salesforce/codet5p-2b"



        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint,
                                              torch_dtype=torch.float16,
                                              low_cpu_mem_usage=True,
                                              trust_remote_code=True).to(device)

        tokenizer.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")
        model.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")

        tokenizer = AutoTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")

        userSentence = "Optimize the given Python program to improve the speed of execution: {def calc( num1, num2):    result = 0    for i in range(num1, num2):       result += ((i+1) * (i+2))    return result}"
        userCode = """{def calc( num1, num2):    
        result = 0    
        for i in range(num1, num2):       
        result += ((i+1) * (i+2))    
            return result}"""

        print(torch.cuda.memory_allocated()/1024**2)
        
        encoding = tokenizer([userSentence], truncation=True, max_length=args.max_len, return_tensors="pt").to(device)
        encoding_decoder = tokenizer(["Optimize the given Python program to improve the speed of execution:" + userCode], truncation=True, max_length=args.max_len, return_tensors="pt").to(device)
        outputs = model.generate(**encoding,
                                        decoder_input_ids=encoding_decoder['input_ids'],
                                        max_length=args.max_len,
                                        do_sample=True,
                                        temperature=args.temperature,
                                        eos_token_id=tokenizer.eos_token_id,
                                        top_p=0.95,
                                        encoder_repetition_penalty=0.7,
                                        top_k=args.max_len, #fix
                                        decoder_start_token_id=tokenizer.pad_token_id,
                                        min_length=10)
        sentenceOutput = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(str.strip(re.sub("'''", '',re.sub(userSentence,'', sentenceOutput))))
        print(torch.cuda.mem_get_info())

    case 5:
        checkpoint = 'Salesforce/codet5-large'

        tokenizer = RobertaTokenizer.from_pretrained(checkpoint)
        
        model = T5ForConditionalGeneration.from_pretrained('Salesforce/codet5-base-codexglue-refine-medium',
                                                        torch_dtype=torch.float16,
                                                        low_cpu_mem_usage=True).to(device)

        tokenizer.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeRefine")
        model.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeRefine")
        tokenizer = RobertaTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeRefine")
        

        userSentence = '''python```i = 3
j = 5
k = 15
sumof3 = 0
sumof5 = 0
sumof15 = 0

while(i < 1000):
	sumof3 = sumof3 + i
	i = i + 3

while(j < 1000):
	sumof5 = sumof5 + j
	j = j + 5

while(k < 1000):
	sumof15 = sumof15 + k
	k = k + 15

print(sumof3 + sumof5 - sumof15)```'''
        

        encoding = tokenizer(userSentence, return_tensors="pt").to(device)
        outputs = model.generate(**encoding,
                                    max_length=args.max_len,
                                    do_sample=True,
                                    temperature=args.temperature,
                                    eos_token_id=tokenizer.eos_token_id,
                                    top_p=0.95)
        sentenceOutput = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(sentenceOutput)
        print(torch.cuda.mem_get_info())
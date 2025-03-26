import sys
import argparse
import torch
from transformers import T5ForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM,RobertaTokenizer
import re
import pprint
from collections import OrderedDict

#parse arguments
parser = argparse.ArgumentParser()

parser.add_argument('--output_path', type=str, help="")
parser.add_argument('--start_index', type=int, default=0, help="")
parser.add_argument('--end_index', type=int, default=164, help="")
parser.add_argument('--temperature', type=float, default=0.5, help="")
parser.add_argument('--N', type=int, default=200, help="")
parser.add_argument('--max_len', type=int, default=600, help="")
parser.add_argument('--decoding_style', type=str, default='sampling', help="")
parser.add_argument('--num_seqs_per_iter', type=int, default=50, help='')
parser.add_argument('--overwrite', action='store_true', help='')


args = parser.parse_args()

argsdict = vars(args)
print(pprint.pformat(argsdict))


# initialization of the model for generateCodeGeneral()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

currDevice = "cpu"
dtype = torch.float32
currDevice1 = device
dtype1 = torch.float16
currDevice2 = "cpu"
dtype2 = torch.float32
    
checkpoint = "Salesforce/codet5p-770m-py"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = T5ForConditionalGeneration.from_pretrained(checkpoint,
                                                   torch_dtype=dtype,
                                                   low_cpu_mem_usage=True).to(currDevice) # and a setting to alternate between cpu and gpu

tokenizer.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")
model.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")

tokenizer = AutoTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/HuggingFaceSaves")

# initialization of the model for codeQuestion()
checkpoint1 = "Salesforce/codet5p-2b"

tokenizer1 = AutoTokenizer.from_pretrained(checkpoint1)
model1 = AutoModelForSeq2SeqLM.from_pretrained(checkpoint1,
                                              torch_dtype=dtype1,
                                              low_cpu_mem_usage=True,
                                              trust_remote_code=True).to(currDevice1)

tokenizer1.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")
model1.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")

tokenizer1 = AutoTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/CodeT5p")

# initialization of the model for codeSummarize()
checkpoint2 = 'Salesforce/codet5-base-multi-sum'

tokenizer2 = RobertaTokenizer.from_pretrained(checkpoint2)
model2 = T5ForConditionalGeneration.from_pretrained(checkpoint2,
                                                        torch_dtype=dtype2,
                                                        low_cpu_mem_usage=True).to(currDevice2)

tokenizer2.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")
model2.save_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")

tokenizer2 = RobertaTokenizer.from_pretrained("/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/MultiSum")
####################################################################

# generate code general
def generateCodeGeneral(userSentence):
    encoding = tokenizer(userSentence, truncation=True, max_length=args.max_len, return_tensors="pt").to(currDevice)
    encoding['decoder_input_ids'] = encoding['input_ids'].clone()
    outputs = model.generate(**encoding, 
                            max_length=args.max_len,
                            temperature=args.temperature,
                            #eos_token_id=tokenizer.eos_token_id,
                            top_p=0.95,
                            do_sample=True)
    sentenceOutput = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return str.strip(re.sub("'''", '',re.sub(userSentence,'', sentenceOutput)))
    #return sentenceOutput
print("done generating")


# progrmaming questions
def codeQuestion(userSentence):
    encoding = tokenizer1(userSentence, truncation=True, max_length=args.max_len, return_tensors="pt").to(currDevice1)
    encoding['decoder_input_ids'] = encoding['input_ids'].clone()
    outputs = model1.generate(**encoding,
                                    max_length=args.max_len//2,
                                    do_sample=True,
                                    temperature=args.temperature,
                                    eos_token_id=tokenizer.eos_token_id,
                                    top_p=0.95,
                                    encoder_repetition_penalty=0.5,
                                    top_k=args.max_len, #fix
                                    num_return_sequences=2,
                                    #decoder_start_token_id=tokenizer.pad_token_id,
                                    min_length=10)
    sentenceOutput = (tokenizer1.decode(outputs[0], skip_special_tokens=True))
    check =  str.strip(re.sub('"', '',re.sub(userSentence,'', sentenceOutput)))
    return "\n".join(list(OrderedDict.fromkeys(check.split("\n"))))

#Summarizing code
def codeSummarize(userCode):
    encoding = tokenizer2(userCode, truncation=True, max_length=args.max_len, return_tensors="pt").to(currDevice2)

    outputs = model2.generate(**encoding,
                                    max_length=args.max_len,
                                    do_sample=True,
                                    temperature=args.temperature,
                                    eos_token_id=tokenizer.eos_token_id,
                                    top_p=0.95,
                                    top_k=args.max_len, 
                                    num_return_sequences=10,
                                    no_repeat_ngram_size=2,
                                    early_stopping=True,
                                    min_length=10)
    sentenceOutput = tokenizer2.decode(outputs[0], skip_special_tokens=True)
    return sentenceOutput

#Optimizing code
def codeOptimize(userSentence, userCode): #This probably doesn't work... :(
    encoding = tokenizer1(userSentence, truncation=True, max_length=args.max_len, return_tensors="pt").to(device)
    encoding_decoder = tokenizer([userSentence + userCode], truncation=True, max_length=args.max_len, return_tensors="pt").to(device)
    outputs = model1.generate(**encoding,
                                decoder_input_ids=encoding_decoder['input_ids'],
                                max_length=args.max_len,
                                do_sample=True,
                                temperature=args.temperature,
                                eos_token_id=tokenizer.eos_token_id,
                                top_p=0.95,
                                #encoder_repetition_penalty=0.6,
                                #top_k=args.max_len, #fix
                                decoder_start_token_id=tokenizer.pad_token_id,
                                min_length=10)
    sentenceOutput = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return str.strip(re.sub("'''", '',re.sub(userSentence,'', sentenceOutput)))

#must run on gpu default
def codeCompletion(text, leng): #add len
    print(leng)
    match leng:
        case 0:
            maxLen = 200
        case 1:
            maxLen = 100
        case 2:
            maxLen = 400
        case 3:
            maxLen = 600
    
    encoding = tokenizer(text, truncation=True, max_length=maxLen, return_tensors="pt").to(currDevice)
    encoding['decoder_input_ids'] = encoding['input_ids'].clone()
    outputs = model.generate(**encoding, 
                            max_length=maxLen,
                            #temperature=args.temperature,
                            #eos_token_id=tokenizer.eos_token_id,
                            top_p=0.95,
                            do_sample=True)
    sentenceOutput = tokenizer.decode(outputs[0], skip_special_tokens=True)
    #return str.strip(re.sub("'''", '',re.sub(text,'', sentenceOutput)))
    return sentenceOutput

def commentGeneration(text, leng):
    print(leng)
    match leng:
        case 0:
            maxLen = 200
        case 1:
            maxLen = 100
        case 2:
            maxLen = 400
        case 3:
            maxLen = 600


    encoding = tokenizer1(text, truncation=True, max_length=maxLen, return_tensors="pt").to(currDevice1)
    encoding['decoder_input_ids'] = encoding['input_ids'].clone()
    outputs = model1.generate(**encoding,
                                    max_length=maxLen,
                                    do_sample=True,
                                    temperature=args.temperature,
                                    eos_token_id=tokenizer.eos_token_id,
                                    top_p=0.95,
                                    encoder_repetition_penalty=0.5,
                                    top_k=args.max_len, #fix
                                    num_return_sequences=2,
                                    #decoder_start_token_id=tokenizer.pad_token_id,
                                    min_length=10)
    sentenceOutput = (tokenizer1.decode(outputs[0], skip_special_tokens=True))
    check =  str.strip(re.sub('"', '',re.sub(text,'', sentenceOutput)))
    return "\n".join(list(OrderedDict.fromkeys(check.split("\n"))))

#Explore multiline docstring 
def autoDoc(text, leng):
    print(leng)
    match leng:
        case 0:
            maxLen = 200
        case 1:
            maxLen = 100
        case 2:
            maxLen = 400
        case 3:
            maxLen = 600
    
    encoding = tokenizer2(text, truncation=True, max_length=maxLen, return_tensors="pt").to(currDevice2)

    outputs = model2.generate(**encoding,
                                    max_length=maxLen,
                                    do_sample=True,
                                    temperature=args.temperature,
                                    eos_token_id=tokenizer.eos_token_id,
                                    top_p=0.95,
                                    top_k=args.max_len, 
                                    num_return_sequences=10,
                                    no_repeat_ngram_size=2,
                                    early_stopping=True,
                                    min_length=10)
    sentenceOutput = tokenizer2.decode(outputs[0], skip_special_tokens=True)
    return f"'''\n  {sentenceOutput}\n'''"

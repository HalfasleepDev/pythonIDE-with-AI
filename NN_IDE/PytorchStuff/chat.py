import random
import json
import torch
from model import NeuralNetwork
from nltkUtils import bagOfWords, tokenize
from generateCode import generateCodeGeneral, codeQuestion, codeSummarize, codeOptimize
#import generateCodeClass
from concurrent.futures import ThreadPoolExecutor #Background ThreadPoolExecutor


executor = ThreadPoolExecutor()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#print(device)

with open('/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/intents.json', 'r') as f:
    intents = json.load(f)

FILE = "/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff/data.pth"
data = torch.load(FILE)

inputSize = data["inputSize"]
hiddenSize = data["hiddenSize"]
outputSize = data["outputSize"]
allWords = data["allWords"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetwork(inputSize, hiddenSize, outputSize).to(device)
model.load_state_dict(model_state)
model.eval()

#chat

botName = "AI"



def getResponse(userSentence, codeText):
    strCodeText = codeText
    strSentence = userSentence
    QCSentenceList = userSentence.split()[:2]
    QCSentenceR = " ".join(QCSentenceList)
    print(QCSentenceR)

    sentence = tokenize(userSentence)
    X = bagOfWords(sentence, allWords)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]


    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                print(tag)
                match tag:
                    case 'generate':
                        return generateCodeGeneral(strSentence)
                    case 'explain':
                        return codeQuestion(strSentence)
                    case 'summarize':
                        if strCodeText != "":
                            return codeSummarize(strCodeText)
                        else:
                            return random.choice(intent['responses'])
                    case 'OptimiseInput':
                        if strCodeText != "":
                            return codeOptimize(strSentence, strCodeText)
                        else:
                            return random.choice(intent['responses'])
                    case _:
                        return random.choice(intent['responses'])
                    
    sentence = tokenize(QCSentenceR)
    X = bagOfWords(sentence, allWords)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]


    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                print("Two word tag: "+ tag)
                match tag:
                    case 'generate':
                        return generateCodeGeneral(strSentence)
                    case 'explain':
                        return codeQuestion(strSentence)
                    case 'summarize':
                        if strCodeText != "":
                            return codeSummarize(strCodeText)
                        else:
                            return random.choice(intent['responses'])
                    case 'OptimiseInput':
                        if strCodeText != "":
                            return codeOptimize(strSentence, strCodeText)
                        else:
                            return random.choice(intent['responses'])
                    case _:
                        return random.choice(intent['responses'])
          
    return "I do not understand..."

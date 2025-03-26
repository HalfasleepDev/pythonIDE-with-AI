import json
from nltkUtils import tokenize, stem, bagOfWords
import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from model import NeuralNetwork

with open('intents.json', 'r') as f:
    intents = json.load(f)

allWords = []
tags = []
xy = []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        allWords.extend(w)
        xy.append((w, tag))

ignoreWords = ['?', '!', '.', ',', '...', '/']
specialWords = [':']
allWords = [stem(w) for w in allWords if w not in ignoreWords]
allWords = sorted(set(allWords))
tags = sorted(set(tags))
print(tags)

xTrain = []
yTrain = []
for (patternSentence, tag) in xy:
    bag = bagOfWords(patternSentence, allWords)
    xTrain.append(bag)

    label = tags.index(tag)
    yTrain.append(label) #CrossEntropyLoss

xTrain = np.array(xTrain)
yTrain = np.array(yTrain)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(xTrain)
        self.x_data = xTrain
        self.y_data = yTrain

    #dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples

#hyperparameters   
batch_size = 8

hiddenSize = 202
outputSize = len(tags)
inputSize = len(xTrain[0])
learningRate = 0.001
numEpochs = 1500
#print(inputSize, len(allWords))
#print(outputSize, tags)
#print(len(xTrain[0]))

dataset = ChatDataset()
trainLoader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#print(device)
model = NeuralNetwork(inputSize, hiddenSize, outputSize).to(device)

# loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)

for epoch in range(numEpochs):
    for (words, labels) in trainLoader:
        words = words.to(device)
        labels = labels.type(torch.LongTensor)
        labels = labels.to(device)

        #forward
        outputs = model(words)
        loss = criterion(outputs, labels)

        #backward and optimizer
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'epoch {epoch + 1}/{numEpochs}, loss={loss.item():.4f}')

print(f'final loss, loss={loss.item():.4f}')

#print(vars(model))

data = {
    "model_state": model.state_dict(),
    "inputSize": inputSize,
    "outputSize": outputSize,
    "hiddenSize": hiddenSize,
    "allWords": allWords,
    "tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'training complete. File saved to {FILE}')

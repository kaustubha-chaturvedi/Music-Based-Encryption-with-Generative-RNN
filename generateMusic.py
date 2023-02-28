import os
import keras
from keras import layers as ls
from keras import models as md
import pandas as pd
import numpy as np

def createSeqModel(ch):
    model = md.Sequential()
    
    model.add(ls.Embedding(input_dim = ch, output_dim = 512, batch_input_shape = (1, 1))) 
  
    model.add(ls.LSTM(256, return_sequences = True, stateful = True))
    model.add(ls.Dropout(0.2))
    
    model.add(ls.LSTM(256, return_sequences = True, stateful = True))
    model.add(ls.Dropout(0.2))
    
    model.add(ls.LSTM(256, stateful = True)) 
    model.add(ls.Dropout(0.2))
    
    model.add((ls.Dense(ch)))
    model.add(ls.Activation("softmax"))
    
    return model

def generateSeq(seqSize, modelName,indexChar):
    ch = len(indexChar)
    model = createSeqModel(ch)
    model.load_weights(f'{modelName}.h5')
     
    ind = [0]
    
    for _ in range(seqSize):
        batch = np.zeros((1, 1))
        batch[0, 0] = ind[-1]
        
        predictedProbs = model.predict_on_batch(batch).ravel()
        sample = np.random.choice(range(ch), size = 1, p = predictedProbs)
        
        ind.append(sample[0])
    
    seq = ''.join(indexChar[c] for c in ind)
    
    cnt = 0
    for i in seq:
        cnt += 1
        if i == "\n":
            break
    seq = seq[cnt:]
    cnt = 0
    for i in seq:
        cnt += 1
        if i == "\n" and seq[cnt] == "\n":
            break
    seq = seq[:cnt]
    return seq

file=open(r'./data/input.txt','r')
data=file.read()
file.close()
indexChar = {i: ch for (i, ch) in enumerate(sorted(list(set(data))))}
def generateMusic(length=65):
    l=[]
    while len(l)<=length: l+=generateSeq(length*9,"modelV1",indexChar).split(' | ')[1:]
    return " | ".join(l)
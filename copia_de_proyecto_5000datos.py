# -*- coding: utf-8 -*-



import numpy as np
import pandas as pd

datos_train=pd.read_csv('D:/Desktop/Protecto_AI_spam/train_data')
df = pd.DataFrame(index=range(3680,3680+400))
h=datos_train.append(df)
print(h)

#h.info()
print(len(h))


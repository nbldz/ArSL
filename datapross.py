# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:14:24 2024

@author: nbl
"""

from modules import *
from folderstup import *




classes = {label:num for num, label in enumerate(actions)}
res=np.zeros(78)

sequences, labels = [], []
for action in actions:
    #for sequence in range(1,2):
        window = []
        for frame_num in range(1,3):
            res1 =np.loadtxt(os.path.join(DATA_PATH, str(action), "{}.txt".format('IDRiD_'+str("%02d" %frame_num)+'_HE')))
            z = res1.shape
            res[:z[0]]=res1
            
            window.append(res)
        sequences.append(window)
        labels.append(classes[action])

# X and y variables 
X = np.array(sequences)
y= to_categorical(labels).astype(int)

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:13:41 2024

@author: nbl
"""

from Code.modules import *
import pandas as pd
import numpy as np

DATA_PATH = os.path.join('retina2') 
file_errors_location = r'D:\sharjah\sign\nblsignvideo\Code\retina.xlsx'
df = pd.read_excel(file_errors_location)
ss=df.loc[:,"Retinopathy grade"]
actions=np.array(ss)
#actions=['2','3','4']

#actions = np.array(['نبيل', 'هزيل', 'نعم'])

number_sequences = 22
#sequence_length = 30

for action in actions: 
    for sequence in range(1,number_sequences):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass
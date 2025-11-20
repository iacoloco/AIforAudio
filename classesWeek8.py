#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:09:46 2025

@author: armandoiachini
"""

"data.py file "

"create a class sapundclass(DtaSet)"

import numpy as np
from numpy.random import permutation
from torch.utils.data import Dataset

import librosa as lr



class Drums(Dataset):
    def __init__(self):
        pass
        
        
        
        
        
        
        
    def __len__(self):
        return self.num_example
    
    
    def __getitme__(self, idx):
        random_index = self.indices[idx]
        return(
            self.data[random_index,:].astype(np.float32),
            self.labels[random_index,None].astype(np.float32)
            )

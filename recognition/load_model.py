import pickle
from PIL import Image
import PIL.ImageOps 
import numpy as np
from pathlib import Path

directory = Path(__file__).resolve().parent

def recog_digit_insult(f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10):
    with open(directory/"xgboost_309_5_en.pickle", 'rb') as f:
        clf_load = pickle.load(f)
    input_List = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
    np_List = np.array(input_List)
    data = np_List.reshape((1,-1))
    return clf_load.predict(data)

def recog_digit_defamation(f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10):
    with open(directory/"xgboost_310_5_en.pickle", 'rb') as f:
        clf_load = pickle.load(f)
    input_List = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
    np_List = np.array(input_List)
    data = np_List.reshape((1,-1))
    return clf_load.predict(data)

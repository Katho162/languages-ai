import os
import pickle

def load_pickle():
    absolute_path = os.path.dirname(__file__)
    path = os.path.join(absolute_path, '../model/nlmt.pkl')
    with open(path, 'rb') as f:
        pickle.load(f)
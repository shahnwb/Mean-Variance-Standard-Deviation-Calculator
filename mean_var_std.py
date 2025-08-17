import numpy as np

def calculate(list):
    
    if len(list) < 9:
        calculations = print('ValueError: List must contain nine numbers.')
    else:
        ar = np.array(list)
        mat = ar.reshape(3,3)
        fl = mat.flatten()
        calculations = {
            'mean':[mat.mean(axis=0),mat.mean(axis=1),fl.mean()],
            'variance':[mat.var(axis=0),mat.var(axis=1),fl.var()],
            'standard deviation':[mat.std(axis=0),mat.std(axis=1),fl.std()],
            'max':[mat.max(axis=0),mat.max(axis=1),fl.max()],
            'min':[mat.min(axis=0),mat.min(axis=1),fl.min()],
            'sum':[mat.sum(axis=0),mat.sum(axis=1),fl.sum()]
        }

    return calculations

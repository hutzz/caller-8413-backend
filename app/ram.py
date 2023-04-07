import numpy as np
import pandas as pd
import dataframe_image as dfi

def megatransfers(initial_ls: int=2133, max_ls: int=6000):
    ls = []
    count = 0
    if initial_ls % 100 == 0: count = 0
    elif initial_ls % 100 == 33: count = 1
    else: count = 2
    ls.append(initial_ls)
    while initial_ls < max_ls:
        count += 1
        if count % 3 != 0:
            initial_ls += 133
            ls.append(initial_ls)
        else:
            initial_ls += 134
            ls.append(initial_ls)
    return np.asarray(ls)

cas_latency = lambda i=10,m=15 : np.arange(i, m+1)

ns = lambda c,m : c*2000/m

def twodim(mt,cas):
    ls = []
    for y in cas:
        for x in mt:
            ls.append(ns(y,x))
    return np.asarray(ls)

def rammap(mt_array, cas_array):
    body = twodim(mt_array,cas_array).reshape(len(cas_array),len(mt_array))
    df = pd.DataFrame(body, columns=mt_array, index=cas_array)
    df_styled = df.style.background_gradient(axis=None)
    dfi.export(df_styled, 'ram.png')
    return '../caller-8413-backend/ram.png'
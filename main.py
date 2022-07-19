import pandas as pd
import numpy as np
from pprint import pprint

dataset = pd.read_csv('Skin_NonSkin.txt', sep='\t', names=['B', 'G', 'R', 'Skin', ])
df = pd.DataFrame(dataset)
# print(df)
prob_B = pd.DataFrame(columns=["p_b"])
prob_G = pd.DataFrame(columns=["p_g"])
prob_R = pd.DataFrame(columns=["p_r"])
total_prob = pd.DataFrame(columns=["total"])
# print(df)
skin_prob = df.groupby('Skin').size().div(len(df))
prob_B = df.groupby(['B', 'Skin']).size().div(len(df)).div(skin_prob, axis=0, level='Skin')
prob_G = df.groupby(['G', 'Skin']).size().div(len(df)).div(skin_prob, axis=0, level='Skin')
prob_R = df.groupby(['R', 'Skin']).size().div(len(df)).div(skin_prob, axis=0, level='Skin')
# print(prob_B)
# print(prob_G)
# print(prob_R)
# frames = [prob_B, prob_G, prob_R]
# result = pd.concat(frames, axis=1)
print(prob_B)

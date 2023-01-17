import numpy as np
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/Q2_bollywood.csv')
df.duplicated()
df.duplicated().any()
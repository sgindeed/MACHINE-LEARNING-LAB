import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('/content/drive/MyDrive/Q2_bollywood.csv')
sns.pairplot(df)
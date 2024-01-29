import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


path = 'Lab1_tutorial\Gas Turbine Dataset'
file_name = Path(path).glob('*.csv')
gt_df = pd.concat((pd.read_csv(file) for file in file_name), ignore_index=True)
print(f"\ndataframe shape: {gt_df.shape}\n")
print(f"dataframe size: {gt_df.size}\n")
print(f"Head:\n{gt_df.head()}\n")
print(f"info: {gt_df.info()}\n")
print(f"statistical description:\n {gt_df.describe()}\n")
print(f"{gt_df.mode()}\n")
hist = plt.hist(gt_df, bins=100)
plt.plot(hist)



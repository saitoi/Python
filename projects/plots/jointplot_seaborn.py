import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

print(tips.head())
sns.jointplot(data=tips, x='tip', y='total_bill', kind='hex')
plt.show()
sns.kdeplot(data=tips, x='tip', y='total_bill', kind='scatter')
plt.show()

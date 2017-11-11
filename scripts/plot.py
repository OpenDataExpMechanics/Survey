import numpy as np
import pandas as pd
import matplotlib as mpl
from  matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

import seaborn as sns

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams.update({'text.usetex':True})

sns.set(color_codes=True)

sns.set(style="darkgrid")

data = pd.read_csv('data.csv')
data['Year'] = data['Year'].astype(int)
data['Data'] = data['Data'].astype(int)

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=12)
plt.tight_layout()

plt.xticks( data['Year'], rotation=35 )

sns.regplot(x="Year", y="Data", data=data)

plt.ylabel("Data available")
plt.savefig("Data_available.pdf")

plt.clf()

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=12)

plt.xticks( data['Year'], rotation=35 )

sns.regplot(x="Year", y="Bounce", data=data)
plt.savefig("Bounce.pdf")

plt.clf()

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=12)

plt.xticks( data['Year'], rotation=35 )

sns.regplot(x="Year", y="Reply", data=data)
plt.savefig("Reply.pdf")

plt.clf()

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=12)

plt.xticks( data['Year'], rotation=35 )

sns.regplot(x="Year", y="No reply", data=data)
plt.savefig("No_Reply.pdf")






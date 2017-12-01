import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams.update({'text.usetex':True})

import seaborn as sns

sns.set(color_codes=True)

sns.set(style="darkgrid")

data = pd.read_csv('data.csv')

data['Data'] = data['Data'] / data['Reply'] * 100.
data['b'] = data['a'] / data['Reply'] * 100.
data['c'] = data['c'] / data['Reply'] * 100.
data['Reply'] = data['Reply'] / 11. * 100.
data['Data'] = (data['Data']*data['Reply']) / (data['Data']*data['Reply'] + (1.-data['Data'])*data['Reply'])
data['b'] = (data['b']*data['Reply']) / (data['b']*data['Reply'] + (1.-data['b'])*data['Reply'])
data['c'] = (data['c']*data['Reply']) / (data['c']*data['Reply'] + (1.-data['c'])*data['Reply'])

# Probability that one got an reply

sns.regplot(x='Year', y='Reply', data=data)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.xticks( data['Year'], rotation=35 )
plt.xlabel('Year')
plt.ylabel(r'$P($ get reply $)$')

plt.ylim(0,100)
plt.savefig("Reply_probability.pdf")


plt.clf()

# Probability that data is available for the reply

sns.regplot(x='Year', y='Data', data=data)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.xticks( data['Year'], rotation=35 )
plt.xlabel('Year')
plt.ylabel(r'$P($ data available $\vert$ get reply $)$')

plt.ylim(0,100)
plt.savefig("Data_probability.pdf")

plt.clf()

# Probability that data is confidential for the reply

sns.regplot(x='Year', y='Data', data=data)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.xticks( data['Year'], rotation=35 )
plt.xlabel('Year')
plt.ylabel(r'$P($ data available $\vert$ get reply $)$')

plt.ylim(0,100)
plt.savefig("Data_confidential.pdf")

plt.clf()

# Probability that a reference is provided for the reply

sns.regplot(x='Year', y='c', data=data)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.xticks( data['Year'], rotation=35 )
plt.xlabel('Year')
plt.ylabel(r'$P($ reference is provided $\vert$ get reply $)$')

plt.ylim(0,100)
plt.savefig("Data_reference.pdf")

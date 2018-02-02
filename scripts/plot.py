# Script for plotting the linear regression with the
# confidence level of the collected data
# @author Open Data in Experimental Mechanics 

# Packages
import numpy as np
import pandas as pd
import matplotlib as mpl
from  matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

import seaborn as sns
######

# Use LaTeX for rendering
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams.update({'text.usetex':True})
######

# Seaborn setting
sns.set(color_codes=False)
sns.set(style="ticks")
sns.set(font_scale=1.5)
#####


data = pd.read_csv('data.csv')

# Linear regression for the available data sets
data['Year'] = data['Year'].astype(int)
data['Data'] = data['Data'].astype(int)

sns.set(style="ticks")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.tight_layout()

ticks = np.arange(2000,2017,4)
plt.xticks( ticks, rotation=35 )
plt.xlim(1999,2017)
sns.regplot(x="Year", y="Data", data=data, color='black')

plt.ylabel("Data available")
plt.savefig("Data_available.pdf")

plt.clf()

# Linear rgeresison for the bounced e-mails
sns.set(style="ticks")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=8)

ticks = np.arange(2000,2017,4)
plt.xticks( ticks, rotation=35 )
plt.xlim(1999,2017)

sns.regplot(x="Year", y="Bounce", data=data, color='black')
plt.savefig("Bounce.pdf")

plt.clf()

#Linear regresison for the replies
sns.set(style="ticks")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=6)

ticks = np.arange(2000,2017,4)
plt.xticks( ticks, rotation=35 )
plt.xlim(1999,2017)

sns.regplot(x="Year", y="Reply", data=data, color='black')
plt.savefig("Reply.pdf")

plt.clf()

#Linear regression for the non replies
sns.set(style="ticks")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=12)

ticks = np.arange(2000,2017,4)
plt.xticks( ticks, rotation=35 )
plt.xlim(1999,2017)

sns.regplot(x="Year", y="No reply", data=data, color='black')
plt.savefig("No_Reply.pdf")


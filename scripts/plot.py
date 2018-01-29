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
sns.set(color_codes=True)
sns.set(style="darkgrid")
#####


data = pd.read_csv('data.csv')

# Linear regression for the available data sets
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

# Linear rgeresison for the bounced e-mails
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=12)

plt.xticks( data['Year'], rotation=35 )

sns.regplot(x="Year", y="Bounce", data=data)
plt.savefig("Bounce.pdf")

plt.clf()

#Linear regresison for the replies
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=12)

plt.xticks( data['Year'], rotation=35 )

sns.regplot(x="Year", y="Reply", data=data)
plt.savefig("Reply.pdf")

plt.clf()

#Linear regression for the non replies
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylim(ymax=12)

plt.xticks( data['Year'], rotation=35 )

sns.regplot(x="Year", y="No reply", data=data)
plt.savefig("No_Reply.pdf")


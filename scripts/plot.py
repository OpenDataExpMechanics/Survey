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

data = pd.read_csv('data.csv')

# Linear regression for the available data sets
data['Year'] = data['Year'].astype(int)
data['Data'] = data['Data'].astype(int)

sns.set(font_scale=1.5,style="ticks")
plt.tight_layout()

xticks = np.arange(2000,2017,2)
yticks = np.arange(min(data['Data']),max(data['Data'])+1,1)
plt.xticks( xticks, rotation=35 )
plt.yticks( yticks)
plt.xlim(1999,2017)
sns.regplot(x="Year", y="Data", data=data, color='black',ci=None)

plt.ylabel("Number of available data sets")
plt.savefig("Data_available.pdf",dpi=800)

plt.clf()

# Linear rgeresison for the bounced e-mails
sns.set(font_scale=1.5,style="ticks")

yticks = np.arange(min(data['Bounce']),max(data['Bounce'])+1,1)
plt.xticks( xticks, rotation=35 )
plt.yticks( yticks)
plt.xlim(1999,2017)

sns.regplot(x="Year", y="Bounce", data=data, color='black',ci=None)
plt.ylabel(r"Number of bounced e-mails")
plt.savefig("Bounce.pdf",dpi=800)

plt.clf()

#Linear regresison for the replies
sns.set(font_scale=1.5,style="ticks")

yticks = np.arange(min(data['Reply']),max(data['Reply'])+1,1)
plt.xticks( xticks, rotation=35 )
plt.yticks ( yticks)
plt.xlim(1999,2017)

sns.regplot(x="Year", y="Reply", data=data, color='black',ci=None)
plt.ylabel("Number of replies to sent e-mail")
plt.savefig(r"Reply.pdf",dpi=800)

plt.clf()

#Linear regression for the non replies
sns.set(font_scale=1.5,style="ticks")


yticks = np.arange(min(data['No reply']),max(data['No reply'])+1,1)
plt.xticks( xticks, rotation=35 )
plt.yticks ( yticks )
plt.xlim(1999,2017)

sns.regplot(x="Year", y="No reply", data=data, color='black',ci=None)
plt.ylabel(r"Number of non replies")
plt.savefig("No_Reply.pdf",dpi=800)


# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 23:18:49 2016

@author: zhangsheng
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import seaborn as sns; sns.set()

name=raw_input('Enter file name:')
csv='\data'+name+'.csv'
df_raw=pd.read_csv(csv,keep_default_na=False)
df_qn=df_raw.copy()

total_questions=len(df_raw.columns.values)
total_response=len(df_raw)

for i in range(4,total_questions):   # relabelling of questions with numbers
    df_qn.columns.values[i]='q'+str(i-3)

df_qn.Class=df_qn.Class.str.replace('\,.+','')  # removal of responses with double selection of classes

for i in range(1,6):
    df_qn['q'+str(i)]=df_qn['q'+str(i)].str.replace('\,.+','') # removal of responses with double selections
	

df_qn.to_csv('C:/Users/Kira/Desktop/elearning/output/df_clean.csv') #saving of cleaned data
print 'csv saved to C:/Users/Kira/Desktop/elearning/output', '\n'

summary_1_to_6=[]
summary_6_to_21=[]
tutorial_grps=sorted(df_qn.Class.unique())

for i in range(1,6):
	df_summary=df_qn.pivot_table('Name',index='q'+str(i),columns='Class',aggfunc='count',fill_value=0,margins=True)
	df_summary_ord=df_summary.reindex(['Frequently','Sometimes','Seldom','Never','NA','All','SPACE'],fill_value=0)
	df_sot=df_summary_ord.transpose()
	#print df_summary_ord
	df_sot_pct=df_sot.div(df_sot.All,axis='index')*100
	sum_and_pct=[df_sot,df_sot_pct]
	summary_1_to_6.append(pd.concat(sum_and_pct, axis = 1))

for i in range(6,22):
	df_summary=df_qn.pivot_table('Name',index='q'+str(i),columns='Class',aggfunc='count',fill_value=0,margins=True)
	df_summary_ord=df_summary.reindex([5,4,3,2,1,0,'All','SPACE'],fill_value=0)
	df_sot=df_summary_ord.transpose()
	#print df_summary_ord, '\n' ,df_summary
	df_sot_pct=df_sot.div(df_sot.All,axis='index')*100
	sum_and_pct=[df_sot,df_sot_pct]
	summary_6_to_21.append(pd.concat(sum_and_pct, axis = 1))
'''
print summary_1_to_6

print 'Subject: ', name, '\n'

stats_1=pd.concat(summary_1_to_6,axis = 0)
#stats_1.to_csv('C:/Users/laizs/Desktop/eLearning Survey/output/stats1.csv')	
print 'Response and Percentages for Question 1 to 6 is saved to stats_1.csv', '\n'

stats_2=pd.concat(summary_6_to_21,axis = 0)
#stats_2.to_csv('C:/Users/laizs/Desktop/eLearning Survey/output/stats2.csv')	
print 'Response and Percentages for Question 6 to 21 is saved to stats_2.csv'
'''

stats_1=pd.concat(summary_1_to_6,axis = 0)
stats_2=pd.concat(summary_6_to_21,axis = 0)

summary_1_to_6_class=[]
summary_6_to_21_class=[]

for i in tutorial_grps:
	tut = stats_1.ix[i]
	summary_1_to_6_class.append(tut)
	
for i in tutorial_grps:
	tut = stats_2.ix[i]
	summary_6_to_21_class.append(tut)
	
print 'Subject: ', name, '\n'


stats_1_class=pd.concat(summary_1_to_6_class,axis = 0)
stats_1_class.to_csv('C:/Users/Kira/Desktop/elearning/output/stats1.csv')	
print 'Response and Percentages for Question 1 to 6 by class is saved to stats_1.csv', '\n'

stats_2_class=pd.concat(summary_6_to_21_class,axis = 0)
stats_2_class.to_csv('C:/Users/Kira/Desktop/elearning/output/stats2.csv')	
print 'Response and Percentages for Question 6 to 21 by class is saved to stats_2.csv'



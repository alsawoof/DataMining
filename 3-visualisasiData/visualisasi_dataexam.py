# -*- coding: utf-8 -*-
"""Visualisasi_DataExam.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PODw2w_zhwTUK_RHoY6FrAZJYqZRN4W_
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("exams1.csv")
data.head()

data.info()

data['race/ethnicity'].unique()

lunchform = 'free/reduced'
data[data['lunch']==lunchform]

"""untuk menampilkan math score dengan mencari rata-rata(mean) dan juga nilai tengah(median) tiap *level of education*"""

unique_mathsc = data[data.math_score>70]['parental level of education'].unique()
unique_mathsc.sort()
unique_mathsc

math_score_mean = []
for i in unique_mathsc:
  math_score_mean.append(data[data.math_score>0][data['parental level of education']==i][data['lunch']==lunchform].math_score.mean())

print(set(zip(unique_mathsc, math_score_mean)))

math_score_med = []
for i in unique_mathsc:
  math_score_med.append(data[data.math_score>0][data['parental level of education']==i][data['lunch']==lunchform].math_score.median())

print(set(zip(unique_mathsc, math_score_med)))

"""*untuk perbandingan reading score > 70 dengan writing score > 99*"""

unique_readsc = data[data.reading_score>70]['parental level of education'].unique()
unique_readsc.sort()
unique_readsc

"""untuk writing score > 99 hanya menampilkan 5 level education, sementara reading > 70 menampilkan 6"""

unique_writesc = data[data.writing_score>99]['parental level of education'].unique()
unique_writesc.sort()
unique_writesc

read_score_mean = []
for i in unique_readsc:
  read_score_mean.append(data[data.reading_score>0][data['parental level of education']==i][data['lunch']==lunchform].reading_score.mean())

write_score_mean = []
for i in unique_writesc:
  write_score_mean.append(data[data.writing_score>0][data['parental level of education']==i][data['lunch']==lunchform].writing_score.mean())

"""untuk perbandingan mean yang dihitung pada writing score (menampilkan 5 level education) dengan reading score (menampilkan 6 level education)"""

print(set(zip(unique_writesc, write_score_mean)))

print(set(zip(unique_readsc, read_score_mean)))

nan_indices = []
for i in range(len(unique_mathsc)):
  if type(unique_mathsc[i])==float:
    nan_indices.append(i)

unique_mathsc = list(unique_mathsc)
math_score_med = list(math_score_med)

for i in nan_indices:
  unique_mathsc.pop(i)
  math_score_med.pop(i)

unique_mathsc

"""untuk menampilkan grafik nilai tengah (median) dari math score"""

plt.barh(unique_mathsc, math_score_med)
plt.show()

plt.pie(math_score_med)
plt.legend(unique_mathsc, loc='best')
plt.show()

"""untuk membuat grafik dari rata-rata yang diperoleh tiap level of education dari writing score."""

plt.barh(unique_writesc, write_score_mean)
plt.show()

plt.pie(write_score_mean)
plt.legend(unique_writesc, loc='best')
plt.show()

"""untuk membuat grafik dari rata-rata(mean) read score"""

plt.barh(unique_readsc, read_score_mean)
plt.show()

plt.pie(read_score_mean)
plt.legend(unique_readsc, loc='best')
plt.show()
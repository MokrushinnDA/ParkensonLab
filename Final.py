import pandas as pd
import matplotlib.pyplot as plt
from math import degrees, acos
'import numpy as np'

i, j = 0, 0
time = []
result = []
ang = []
a = []
b = []
c = []
c1 = []
ang1 = []

T = []

df = pd.read_csv ('C:\\raw_data_0ce5753d-c156-11ec-a112-e82aea2c97f4.csv')
THUMB_TIP = df[["THUMB_TIP.x","THUMB_TIP.y","THUMB_TIP.z"]].values
INDEX_FINGER_TIP = df[["INDEX_FINGER_TIP.x","INDEX_FINGER_TIP.y","INDEX_FINGER_TIP.z"]].values
WRIST = df[['WRIST.x','WRIST.y','WRIST.z']].values
TIME = df['TIME'].values
index = df.shape[0]
#print(INDEX_FINGER_TIP)
for i in range(index):
    vector_4_8 = (INDEX_FINGER_TIP - THUMB_TIP)**2
    i =+ 1    

for _ in vector_4_8:
    result.append((sum(_)**(0.5)))
df['Амплитуда']=result
#print(df)
#print(result)

for i in range (index):         
    vector_0_4 = (THUMB_TIP - WRIST) #для вектора 0-4 
    vector_0_4_pow = vector_0_4 ** 2 
    
    vector_0_8 = (INDEX_FINGER_TIP - WRIST) #для вектора 0-8
    vector_0_8_pow = vector_0_8 ** 2
    
    c = vector_0_4 * vector_0_8
    
    i =+ 1    
    
for _ in vector_0_4_pow:            #для вектора 0-4
    a.append((sum(_)**(0.5)))

for _ in vector_0_8_pow:            #для вектора 0-8
    b.append((sum(_)**(0.5)))

for _ in c:            
    c1.append(sum(_))

for j in range(index):
    ang.append(acos(c1[j]/(a[j]*b[j])))
    ang1.append(degrees(ang[j]))
df['Angle']=ang1
#print(ang)
#print(ang1)
int_ang1=list(map(int,ang1))
for i in range(index-1):
    if ang1[i] > ang1[i+1] and ang1[i] > ang1[i-1]:
        if (int_ang1[i]==int_ang1[i+1]):
            continue
        time.append(TIME[i]) 
a = len(time)
for i in range(a-1):
    T.append(time[i+1] - time[i])
    i+=2
print(T)
print(len(T))
Data_T = pd.Series(T)
print(Data_T)
df.plot(y="Амплитуда", x="TIME")
df.plot(y="Angle", x="TIME")
plt.show

Data_T.to_excel('C:\\period of etalon.xls')

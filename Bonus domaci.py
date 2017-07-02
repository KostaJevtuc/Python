# -*- coding: utf-8 -*-
korpus = "Ovde mi je baš lepo. Džunglu ne volim. Ne bih volela da sam tamo. Moje mesto je tu. Tu se osećam kao da sam kod kuće. Stavila sam svoju šoljicu kafe desno, e baš tu."
ovde=0
tamo=0
desno=0
negde=0
tu=0
x=korpus.split(" ")

for i in x:
    i=i.lower()
    i=i.strip(",.")
    if i=="ovde":
        ovde+=1 
    elif i=="tamo":
        tamo+=1
    elif i=="desno":
        desno+=1
    elif i=="negde":
        negde+=1
    elif i=="tu":
        tu+=1
print("Broj javljanja reči ovde:", ovde)
print("Broj javljanja reči tamo:", tamo)
print("Broj javljanja reči desno:", desno)
print("Broj javljanja reči negde:", negde)
print("Broj javljanja reči tu:", tu)
       
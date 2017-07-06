# -*- coding: utf-8 -*-
d = "Oj, dodole, mili Bože\noj, dodo, dodole\nNaša doda Boga moli\noj, dodo, dodole\nSitna kiša da zarosi\noj, dodo, dodole\nNaša polja da potopi\noj, dodo, dodole\nI da rodi bel' pšenica\noj, dodo, dodole\nI kukuruz sa dva klasa\noj, dodo, dodole\nŠto molila umolila\noj, dodo, dodole\nSitna kiša zarosila\noj, dodo, dodole\nNaša polja potopila\noj, dodo, dodole\nI rodila bel' pšenica\noj, dodo, dodole\nI kukuruz sa dva klasa\noj, dodo, dodole"
x=d.split("\n")
x.insert(0,"Niska za zrtvovanje") #posto mi se uvek brise prva niska, samo sam odlucio da dodam jednu na pocetak
for i in range(len(x)-1,0,-1): #ako stavim da je range  (len(x),0,-1) dobijam poruku da je index out of range. Zasto? Ima li to neke veze sa time sto mi se brise prva niska?
    s=x[i].split(" ")
    s.insert(0,"Jos jedna niska za zrvovanje")
    stih=[]
    for d in range(len(s)-1,0,-1):
        if len(stih)<len(s):                        
         stih.append(s[d])
        else: 
         stih.append("\n")
    m=" ".join(stih)
    m1=m.lower()
    m2=m1.capitalize()
    m3=m2.split(" ")
    if "boga" in m3:
       m3 = [word.replace('boga',"Boga") for word in m3] #da,  izguglao sam ovo, don't judge
   
    m4=" ".join(m3) #nisam uradio super domaci... jer nisam super ayyyy
    print(m4)
    
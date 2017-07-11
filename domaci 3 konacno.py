d = "Oj, dodole, mili Bože\noj, dodo, dodole\nNaša doda Boga moli\noj, dodo, dodole\nSitna kiša da zarosi\noj, dodo, dodole\nNaša polja da potopi\noj, dodo, dodole\nI da rodi bel' pšenica\noj, dodo, dodole\nI kukuruz sa dva klasa\noj, dodo, dodole\nŠto molila umolila\noj, dodo, dodole\nSitna kiša zarosila\noj, dodo, dodole\nNaša polja potopila\noj, dodo, dodole\nI rodila bel' pšenica\noj, dodo, dodole\nI kukuruz sa dva klasa\noj, dodo, dodole"
x=d.split("\n")

for i in range(len(x)-1,-1,-1): 
    s=x[i].split(" ")
    
    stih=[]
    for d in range(len(s)-1,-1,-1):
        if s[d][-1]==",":
            s[d]=s[d][:-1]
            s[d-1]=s[d-1]+","
        if len(stih)<len(s):                        
         stih.append(s[d])
        else: 
         stih.append("\n")
        
    m=" ".join(stih)
    m1=m.lower()
    m2=m1.capitalize()
    m3=m2.split(" ")
    if "boga" in m3:
       m3 = [word.replace('boga',"Boga") for word in m3] 
   
    m4=" ".join(m3) 
    print(m4)

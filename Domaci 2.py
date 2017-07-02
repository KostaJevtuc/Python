# -*- coding: utf-8 -*-

recnik={"Sunce": {"Sinonimi":["Ra","Helios"], "Antonimi":["Luna","Artemida"]}, "Aniko": {"Sinonimi":["Lepa","Plavooka"], "Antonimi":["Losa programerka", "Unfashionable"]}, "Zima": {"Sinonimi":["Hladnoca","Zima"], "Antonimi":["Vrucina","Xotina"]}}
print(recnik["Aniko"]["Sinonimi"])
print(recnik["Sunce"]["Sinonimi"])
print(recnik["Zima"]["Sinonimi"])

print(recnik["Aniko"]["Antonimi"]) 
print(recnik["Sunce"]["Antonimi"]) 
print(recnik["Zima"]["Antonimi"]) 

print(recnik["Aniko"]["Sinonimi"][0])
print(recnik["Aniko"]["Antonimi"][1]) 

for i in recnik.keys():

    

    print("Rec: ", i) 

    sin = "Sinonimi: "

    ant = "Antonimi: "



    for sinonim in recnik[i]["Sinonimi"]:

        sin += sinonim + ", "

    print(sin[:-2])



    for antonim in recnik[i]["Antonimi"]:

        ant += antonim + ", "    

    print(ant[:-2] + "\n")




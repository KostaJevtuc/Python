# -*- coding: utf-8 -*-

q = "Živele u jednoj bari tri žabe. Svađale su se oko toga koja od njih najbolje peva, čiji je glas najlepši. Njihovoj svađi nikad ne bi došao kraj da nisu odlučile da organizuju takmičenje da se vidi ko je najbolji. To je za stanovnike bare i okoline bio veliki događaj. Sve žabe, i velike i male, su došle da svojim prisustvom pomognu odluku žirija. Ali pred sam početak svi shvatiše da nisu izabrali žiri. Mnogo njih je želelo da odlučuju koja od tri žabe najlepše peva i zato je bila takva galama da niko nikog nije čuo šta govori. Roda, patka i zmija čuju kreketanje (a taj zvuk ih je neodoljivo privlačio) i požure da vide šta se događa. Žabe, ne razmišljajući mnogo, zamole rodu, patku i zmiju da budu članovi žirija. One pristanu i takmičenje poče. Tri žabe su naizmenično pevale sve dok nisu iscrple svoj bogati repertoar i dok nisu promukle. Publika je bila oduševljena. Članovi žirija zamoliše za tišinu i rekoše takmičarkama da priđu bliže da im čestitaju i proglase pobednicu. I žabe priđoše umorne i sretne. Možemo zamisliti šta se dogodilo takmičarkama. A i publici iz prvih redova. Te večeri su roda, patka i zmija imale obilnu večeru. Žabama nije bilo do pesme. Celu noć su razmišljale i šaputale. Nikad više nisu se svađale koja najlepše peva."

print(len(q))
qlast= " Nikad više nisu se svađale koja najlepše peva."
print(len(qlast))

qcut= q[0:1210]
print(qcut)

r="Zabe ne umeju da govore, to smo naucili na prvom seminaru. Kao ni druge zivotinje, tako da je ova situacija jako nerealna. I zasto nisu mogle samo da stave svoje razlike po strani i drze se zajedno like wtf zabe. Pomislio bi covek da su dovoljno pametna da skapiraju da im je bolje da se drze zajedno or smth."

p= qcut+" "+r
print(p)

s=p.split(". ")
print(len(s))


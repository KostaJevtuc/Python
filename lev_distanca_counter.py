rec1=input('Napisite prvo rec ')
rec2=input('Napisite pseudo rec ')
raz_slova=0
rec1=rec1.lower()
rec2=rec2.lower()
if len(rec1)!=len(rec2):
    print('\nRec i pseudorec moraju biti iste duzine')
else:
    for slovo in range(len(rec1)):
        if not rec1[slovo]==rec2[slovo]:
            raz_slova+=1
    print('\nlevenstajnova distanca: ',raz_slova)

#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))

#k=1

#while True:
#    if vastus!=o_vastus:
#        print("Viga! Sisesta Õige vastus on ...", )
#        vastus=int(input("Sisesta vastus ..."))
#        k+=1
#    else:
#        break
#print("Õige vastus! Katsed oli ...",k )


#x=0

#while True:
#   if x<30:
#        if x%2==1:
#            print(x, end=" ")
#        x+=1
#   else:
#        break


#for x in range(1,31,2):
#        print(x, end=" ")



print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisesta täisarv => ")))   # Sulud ei olnud lõpuni suletud.
        break
    except ValueError:
         print("See pole täisarv.")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi teha.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju on paaris- ja mitu paaritut numbrit")
    print()
    c=b=a
    paaris = 0 #Oli kaks =
    paaritu = 0 #Oli kaks =
    while b > 0:    # Oli vale semicolon
            if b % 2 == 0:
                    paaris += 1
            else:
                    paaritu += 1
            b = b // 10     #Kõrvaldan üleliigse taganemise

    print("Paaris numbrid:", paaris)
    print("Paaritu numbrid:", paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake* sisestatud arv")
    print()
    b=0
    while a > 0: #Ei olnud semicolon
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #oli üleliigne tühik
    print("*Pööratud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Uurime Syracuse hüpoteesi") #Eemaldasin üleliigse sulguri

    print()
    if c % 2 == 0:
        print(c ,"- Paaris arv. Jagame 2.") #muutuja oli vale kohal
    else:
        print(c ,"- Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")   #muutuja oli vale kohal
    while c != 1:
            if c % 2 == 0:  #Ei ole tühik
                    c = c / 2  #Ei ole tühik
            else:
                    c = (3*c + 1) / 2
            print   (int(c), end="")    #Seissid valed topeltjutumärgid
    print()
    print("Гипотеза верна") #Seissid valed topeltjutumärgid

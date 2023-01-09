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



print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisesta täisarv => ")))   #Скобки были не до конца закрыты
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
    paaris = 0 #Было два =
    paaritu = 0 #Было два =
    while b > 0:    # Стояло неправильное двоеточие.
            if b % 2 == 0:
                    paaris += 1
            else:
                    paaritu += 1
            b = b // 10     #Убрал лишний отступ

    print("Paaris numbrid:", paaris)
    print("Paaritu numbrid:", paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake* sisestatud arv")
    print()
    b=0
    while a > 0: #Не было двоеточия
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #был лишний пробел
    print("*Pööratud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Uurime Syracuse hüpoteesi") #Убрал лишнюю скобку

    print()
    if c % 2 == 0:
        print(c ,"- Paaris arv. Jagame 2.") #переменная не там стояла
    else:
        print(c ,"- Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")   #переменная не там стояла
    while c != 1:
            if c % 2 == 0:  #Не хватало пробела
                    c = c / 2  #Не хватало пробела
            else:
                    c = (3*c + 1) / 2
            print   (int(c), end="")    #Стояли неправильные двойные кавычки
    print()
    print("Гипотеза верна") #Стояли неправильные двойные кавычки
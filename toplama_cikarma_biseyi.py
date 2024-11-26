import random

c = int(input("Please choose your operation (1 for summation, 2 for multiplication): "))
while c!=1 and c!=2:
    print("Please enter a valid value.")
    c=int(input("Please choose your operation (1 for summation, 2 for multiplication): "))
a=0
b=0
valid=False
while not valid:
    a=int(input("Please enter the lower limit: "))
    b=int(input("Please enter the upper limit: "))
    if 1<=a<=b<=100:
        valid=True
    else:
        print("Please enter a valid range.")

dogru_cikarsa=["Congratulations !","Well done !","That's right !"]
yanlis_cikarsa=["Well, not really…","Sorry, that is wrong…","Ughh… not quite right."]

toplam_soru=0
dogru_cevap=0
quize_devam_et=True
while quize_devam_et:
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    if c == 1:
        islem = "+"
        gercek_sonuc = num1 + num2
    else:
        islem ="x"
        gercek_sonuc = num1 * num2

    print("What is "+str(num1) + str(islem) + str(num2))
    kullanıcı_sonucu = int(input("Your answer: "))
    toplam_soru+=1

    if kullanıcı_sonucu==gercek_sonuc:
        print(random.choice(dogru_cikarsa))
        dogru_cevap+=1
    else:
        print(random.choice(yanlis_cikarsa))
        print("The correct answer is "+str(gercek_sonuc))

    tekrar=input("Continue ?(1-yes; any other number-no): ")
    if tekrar!="1":
        quize_devam_et=False
if toplam_soru>0:
    yuzdelik=((dogru_cevap/toplam_soru)*100)
    print("You answered "+str(yuzdelik)+"% of the questions correctly.")



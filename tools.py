import os, sys, time

def ClearText():
    os.system("clear")
    
def menu():
    
    print("#################################")
    print("## TOOLS BY MAGISKPEOPLE       ##")
    print("## PLS DON'T USE TERMUX        ##")
    print("## RECCOMEND USE KALI_LINUX    ##")
    print("#################################")
    time.sleep(3)
    print("")
    print("[1] Sharelock Location")
    print("[2] LITEDDOS")
    print("[3] SpiderBot")
    print("[4] LITETOOLS")
    print("[0] Exit")
    time.sleep(2)
    print("")
    tools = input("Select Number : ")
    if tools =="1":
        print("Please wait for second!")
        time.sleep(3)
        os.system("cls")
        time.sleep(3)
        os.system("git clone https://github.com/sherlock-project/sherlock.git")
        print("𝙳𝚘𝚗𝚎 𝙸𝚗𝚜𝚝𝚊𝚕𝚕 >>>>>>> 𝟷𝟶𝟶%")
        time.sleep(3)
    
    if tools =="2":
        os.system("apt update && apt upgrade")
        os.system("pkg install git")
        os.system("pkg install python2")
        os.system("git clone https://github.com/4L13199/LITEDDOS")
        os.system("clear")
        os.system("cd LITEDDOS")
        time.sleep(3)
        os.system("python2 LITEDDOS.py")
        time.sleep(2)
        print("𝙳𝚘𝚗𝚎 𝙸𝚗𝚜𝚝𝚊𝚕𝚕 >>>>>>> 𝟷𝟶𝟶%")
        time.sleep(1)

    if tools =="3":
        os.system("apt update && apt upgrade")
        os.system("apt install php")
        os.system("apt install git")
        os.system("git clone https://github.com/Cvar1984/SpiderBot.git")
        os.system("cd SpiderBot")
        time.sleep(3)
        os.system("clear")
        time.sleep(3)
        print("Tinggal Dijalankan Ya, Seperti Hubunganmu :)")
        time.sleep(2)
        print("Contoh Saya Ingin Pakai Botkomen")
        time.sleep(2)
        print("Ketik: php botkoment.php")
        time.sleep(1)
        print("𝙳𝚘𝚗𝚎 𝙸𝚗𝚜𝚝𝚊𝚕𝚕 >>>>>>> 𝟷𝟶𝟶%")

    if tools =="4":
        os.system("pkg update && pkg upgrade")
        os.system("pkg install git")
        os.system("git clone https://github.com/4L13199/LITETOOLS")
        os.system("clear")
        os.system("cd LITETOOLS")
        time.sleep(3)
        os.system("sh LITETOOLS.isl")
        time.sleep(2)
        print("𝙳𝚘𝚗𝚎 𝙸𝚗𝚜𝚝𝚊𝚕𝚕 >>>>>>> 𝟷𝟶𝟶%")

    elif tools =="0":
        os.system("cls")
        print("Please Wait 3s")
        time.sleep(3)
        os.system("exit")
    else:
        print("𝙿𝚕𝚎𝚊𝚜𝚎 𝙸𝚗𝚙𝚞𝚝 𝙽𝚞𝚖𝚋𝚎𝚛 𝚅𝚊𝚕𝚒𝚍 !!!")
        time.sleep(4)
        sys.exit()
menu()

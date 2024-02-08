import random

liste = ["tas", "kagit", "makas"]

def oyun():
    while True:
        secim = input("Tas kagit makas oyununa hos geldin. Lutfen birini sec (tas, kagit, makas): ")
        if secim in liste:
            rastgele = random.choice(liste)
            if secim == "tas":
                if rastgele == "tas":
                    print(f"Berabere. Ben de {rastgele}'i secmistim.")
                elif rastgele == "kagit":
                    print(f"Ben kazandim {rastgele}'i secmistim.")
                else:
                    print(f"Sen kazandin {rastgele}'i secmistim.")
            elif secim == "kagit":
                if rastgele == "kagit":
                    print(f"Berabere. Ben de {rastgele}'i secmistim.")
                elif rastgele == "makas":
                    print(f"Ben kazandim {rastgele}'i secmistim.")
                else:
                    print(f"Sen kazandin {rastgele}'i secmistim.")
            else:
                if rastgele == "makas":
                    print(f"Berabere. Ben de {rastgele}'i secmistim")
                elif rastgele == "tas":
                    print(f"Ben kazandim {rastgele}'i secmistim.")
                else:
                    print(f"Sen kazandin {rastgele}'i secmistim.")
            break
        else:
            print("lutfen gecerli bir islem gir.")

oyun()

while True:
    tekrar = input("Tekrar oynamak istiyor musun: (e/h) ")
    if tekrar.lower() == "e":
        oyun()
    elif tekrar.lower() == "h":
        break
    else:
        print("Lutfen gecerli bir girdi gir.")

def prim(tall):

    for i in range(2, tall):
        if tall % i == 0:
            print(f"{tall} er ikke et primtall")
            return
    
    print(f"{tall} er et primtall")

if __name__ =="__main__":
    tall = int(input("Skriv inn et heltall:  "))
    prim(tall)
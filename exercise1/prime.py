test_tall = int(input("Skriv inn et heltall:  "))

def primtall(tall):
    # tall mellom 2 og test_tall
    liste = []
    for i in range(2, tall):
         liste.append(i)
    
    count = 0
    
    while True:
         for p in liste: 
            count += 1

            if tall % p == 0:
                print(f"{tall} er ikke et primtall")
                return False
            
            elif count >= len(liste):
                print(f"{tall} er et primtall")
                return False

if __name__ == "__main__":
     primtall(test_tall)


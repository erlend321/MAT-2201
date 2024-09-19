import math
import matplotlib.pyplot as plt


forrige_verdi = None
nåværende_verdi = 0.9
verdier = []
iterasjoner = []
iterasjons_teller = 0



while True:

    nåværende_verdi = math.cos(nåværende_verdi)
    verdier.append(nåværende_verdi)

    iterasjoner.append(iterasjons_teller)
    iterasjons_teller += 1

   
    print(f"cos({forrige_verdi}) = {nåværende_verdi}")

    if forrige_verdi == nåværende_verdi:
        print(f"Verdiene er like {nåværende_verdi}")
        break
        
    forrige_verdi = nåværende_verdi


# Plot the convergence
plt.plot(iterasjoner, verdier, marker='o')
plt.title("Cosinus konvergens plot")
plt.xlabel("Iterasjon")
plt.ylabel("Verdi av cos(x)")
plt.grid(True)
plt.show()

    


    
    

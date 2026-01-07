class Paino:
    def __init__(self, paivamaara, kilo: float):
        self.paivamaara = paivamaara
        self.kilo = kilo
    
    def __str__(self):
        return f"{self.paivamaara}: {self.kilo} kg"
    
    def sanakirjaksi(self):
        return {"paivamaara": self.paivamaara,"kilo": self.kilo}
    
    @classmethod
    def sanakirjasta(cls, d):
        return cls(d["paivamaara"], d["kilo"])

class Juoksu:
    def __init__(self, paivamaara, matka_km: float, aika_min: float, vauhti_min_per_km: float, kommentti: str):
        self.paivamaara = paivamaara
        self.matka_km = matka_km
        self.aika_min = aika_min
        self.vauhti_min_per_km = vauhti_min_per_km
        self.kommentti = kommentti
        

    def __str__(self):
        return f"{self.paivamaara}: {self.matka_km} km, {self.aika_min} min, vauhti {self.vauhti_min_per_km:.2f} min/km, kommentti: {self.kommentti}"
    
    def sanakirjaksi(self):
        return {"paivamaara": self.paivamaara,"matka_km": self.matka_km,"aika_min": self.aika_min,"vauhti_min_per_km": self.vauhti_min_per_km,"kommentti": self.kommentti}

    @classmethod
    def sanakirjasta(cls, d):
        return cls(d["paivamaara"], float(d["matka_km"]), float(d["aika_min"]), float(d["vauhti_min_per_km"]), d["kommentti"])



class Salitreeni:
    def __init__(self, paivamaara, kommentti: str):
        self.paivamaara = paivamaara
        self.kommentti = kommentti

    def __str__(self):
        return f"{self.paivamaara}, kommentti: {self.kommentti}"
    
    def sanakirjaksi(self):
        return {"paivamaara": self.paivamaara,"kommentti": self.kommentti}

    @classmethod
    def sanakirjasta(cls, d):
        return cls(d["paivamaara"], d["kommentti"])
    

import json
import matplotlib.pyplot as plt
class HarjoitusPaivakirja:
    def __init__(self):
        self.painot = []
        self.juoksut = []
        self.salitreenit = []
             
             
    def ohje(self):
        print("Komennot: ")
        print("0 Lopetus")
        print("1 Painon lisäys")
        print("2 Näytä painot")
        print("3 Juoksulenkin lisäys")
        print("4 Näytä juoksulenkit")
        print("5 Salitreenin lisäys")
        print("6 Naytä salitreenit")
        print("7 Näytä painokäyrä")
        print("8 Näytä juoksuvauhtikäyrä")



    def lisaa_paino(self):
        paivamaara = input("Anna päivämäärä (YYYY-MM-DD): ")
        kilo = float(input("Anna paino: "))

        uusi_paino = Paino(paivamaara, kilo)
        self.painot.append(uusi_paino)

        print("Paino lisätty")
        self.tallenna_painot()
    
    def nayta_painot(self):
        if not self.painot:
            print("Ei painomerkintöjä")
            return
        for paino in self.painot:
            print(paino)

    def tallenna_painot(self):
        data = [p.sanakirjaksi() for p in self.painot]
        with open ("painot.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def lataa_painot(self):
        try:
            with open("painot.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return  # eka käynnistys, tiedostoa ei ole

        self.painot = [Paino.sanakirjasta(d) for d in data]


    def lisaa_juoksulenkki(self):
        paivamaara = input("Anna päivämäärä (YYYY-MM-DD): ")
        matka_km = float(input("Anna lenkin pituus:"))
        aika_min = float(input("Kaunko lenkkiin meni aikaa: "))
        vauhti_min_per_km = float(input("Mikä oli lenkin kilometrivauhti:"))
        kommentti = input("Kommentti reenistä: ")

        uusi_lenkki = Juoksu(paivamaara, matka_km, aika_min, vauhti_min_per_km, kommentti)
        self.juoksut.append(uusi_lenkki)

        print("Lenkki lisätty")
        self.tallenna_juoksut()

    def nayta_juoksut(self):
        if not self.juoksut:
            print("Ei juoksulenkkejä")
            return
        
        for lenkki in self.juoksut:
            print(lenkki)

    def tallenna_juoksut(self):
        data = [j.sanakirjaksi() for j in self.juoksut]
        with open("juoksut.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def lataa_juoksut(self):
        try:
            with open("juoksut.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        self.juoksut = [Juoksu.sanakirjasta(d) for d in data]


    def lisaa_salitreeni(self):
        paivamaara = input("Anna päivämäärä (YYYY-MM-DD): ")
        kommentti = input("Kommentti reenistä: ")

        uusi_salitreeni = Salitreeni(paivamaara, kommentti)
        self.salitreenit.append(uusi_salitreeni)

        print("Salitreeni lisätty")
        self.tallenna_salitreenit()

    def nayta_salitreenit(self):
        if not self.salitreenit:
            print("Ei salitreenejä")
            return
        for salitreeni in self.salitreenit:
            print(salitreeni)

    def tallenna_salitreenit(self):
        data = [s.sanakirjaksi() for s in self.salitreenit]
        with open("salitreenit.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def lataa_salitreenit(self):
        try:
            with open("salitreenit.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        self.salitreenit = [Salitreeni.sanakirjasta(d) for d in data]


    
    def nayta_painokayra(self):
        if not self.painot:
            print("Ei painomerkintöjä.", flush=True)
            return

        painot_jarjestyksessa = sorted(self.painot, key=lambda p: p.paivamaara)
        paivat = [p.paivamaara for p in painot_jarjestyksessa]
        kilot = [p.kilo for p in painot_jarjestyksessa]

        muutos = kilot[-1] - kilot[0]

        fig, ax = plt.subplots()
        ax.plot(paivat, kilot, marker="o")
        ax.set_xlabel("Päivä")
        ax.set_ylabel("Paino (kg)")
        ax.set_title(f"Painon kehitys (muutos alusta {muutos:+.1f} kg)")
        ax.tick_params(axis="x", rotation=45)
        fig.tight_layout()
        plt.show()

    def nayta_juoksuvauhtikaayra(self):
        if not self.juoksut:
            print("Ei juoksulenkkejä.")
            return

        juoksut_jarjestyksessa = sorted(self.juoksut, key=lambda j: j.paivamaara)

        paivat = [j.paivamaara for j in juoksut_jarjestyksessa]
        vauhdit = [j.vauhti_min_per_km for j in juoksut_jarjestyksessa]

        fig, ax = plt.subplots()
        ax.plot(paivat, vauhdit, marker="o")

        ax.set_xlabel("Päivä")
        ax.set_ylabel("Vauhti (min/km)")
        ax.set_title("Juoksuvauhdin kehitys")
        ax.tick_params(axis="x", rotation=45)

        fig.tight_layout()
        plt.show()





    def suorita(self):
        self.lataa_painot()
        self.lataa_juoksut()
        self.lataa_salitreenit()
        self.ohje()

        while True:
            print("")
            komento = input("komento: ").strip()

            if komento == "0":
                break
            elif komento == "1":
                self.lisaa_paino()
            elif komento == "2":
                self.nayta_painot()
            elif komento == "3":
                self.lisaa_juoksulenkki()
            elif komento == "4":
                self.nayta_juoksut()
            elif komento == "5":
                self.lisaa_salitreeni()
            elif komento == "6":
                self.nayta_salitreenit()
            elif komento == "7":
                self.nayta_painokayra()
            elif komento == "8":
                self.nayta_juoksuvauhtikaayra()
            else:
                self.ohje()

if __name__ == "__main__":
    paivakirja = HarjoitusPaivakirja()
    paivakirja.suorita()
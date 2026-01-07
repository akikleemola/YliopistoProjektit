class Pankkitili:
    def __init__(self, omistaja: str, saldo: int):
        self.omistaja = omistaja
        self.saldo = saldo

    def hae_saldo(self):
        return self.saldo

    def talleta(self, maara):
        if maara > 0:
            self.saldo += maara
    
    def nosta(self, maara):
        if self.saldo >= maara:
            self.saldo -= maara

    def __str__(self):
        return f"Pankkitili: {self.omistaja}, saldo {self.saldo} euroa"
    
[luku * 2 for luku in luvut if luku % 2 == 0] #listakooste

[luku + 100 if luku % 2 == 0 else luku + 1 for luku in luvut]#listakooste

positiiviset = [luku for luku in filter(lambda luku: luku > 0, luvut)] #listakooste + filter. filter kun halutaan "filtteröidä" listan alkiota. 

kerrottuna_3 = [luku for luku in map(lambda luku: luku * 3, luvut)] #listakooste + map. map kun halutaan tehdä listan alkiolle jotain

class Henkilo:
    def __init__(self, nimi: str, ika: int):
        self.nimi = nimi
        self.ika = ika

    def hae_ika(self):
        return self.ika

    def aseta_ika(self, uusi_ika):
        if uusi_ika >= 0 and uusi_ika <= 120:
            self.ika = uusi_ika
    
    def on_taysi_ikainen(self):
        if self.ika >= 18:
            return True
        else:
            return False

    def __str__(self):
        return f"Henkilö: {self.nimi}, {self.ika} vuotta"

class Auto:
    def __init__(self, merkki: str, nopeus: int):
        self.merkki = merkki
        self.nopeus = nopeus
    
    def kiihdyta(self, maara):
        if maara > 0:
            self.nopeus += maara

    def hae_nopeus(self):
        return self.nopeus
    
    def __str__(self):
        return f"Auto: {self.merkki} nopeus {self.nopeus} km/h"

class Sahkoauto(Auto): #perintää !!!
    def __init__(self, merkki, nopeus, akun_varaustaso: int):
        super().__init__(merkki, nopeus)
        self.akun_varaustaso = akun_varaustaso
    
    def lataa(self, maara):
        if maara > 0:
            self.akun_varaustaso += maara
            if self.akun_varaustaso > 100:
                self.akun_varaustaso = 100

    def __str__(self):
        return f"Sähköauto: {self.merkki}, nopeus {self.nopeus}, akku {self.akun_varaustaso}%"
    
#Generaattori: yeild    
def parilliset(n):
    luku = 0
    while luku <= n:
        yield luku
        luku += 2

class Piste:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, toinen):
        uusi_x = self.x + toinen.x
        uusi_y = self.y + toinen.y
        return Piste(uusi_x, uusi_y) #MITEN OLIO TEHDÄÄN!!!!

    def __str__(self):
        return f"({self.x}, {self.y})"


class Henkilo:
    def __init__(self, nimi: str):
        self.nimi = nimi
        
    def kuvaus(self):
        return f"Henkilö {self.nimi}"
    
class Opiskelija(Henkilo):
    def __init__(self, nimi, opintopisteet: int):
        super().__init__(nimi)
        self.opintopisteet = opintopisteet

    def kuvaus(self):
        return f"Opiskelija: {self.nimi}, op {self.opintopisteet}"
    
def tulosta_kuvaukset(lista: list): #polyformiaaa!!!!!!!!
    for olio in lista:
        print(olio.kuvaus())
        

class Muoto:
    def __init__(self, nimi: str):
        self.nimi = nimi

    def ala(self):
        return 0
    
    def __str__(self):
        return f"Muoto: {self.nimi}"
    
class Suorakulmio(Muoto):
    def __init__(self, nimi, leveys: int, korkeus: int):
        super().__init__(nimi)
        self.leveys = leveys
        self.korkeus = korkeus

    def ala(self):
        ala = self.leveys * self.korkeus
        return ala
    
    def __str__(self):
        return f"Suorakulmio: {self.nimi}, ala {self.ala()}"
    
    def __add__(self, toinen): #ylikuormitusta!!
        uusi_leveys = self.leveys + toinen.leveys
        uusi_korkeus = self.korkeus + toinen.korkeus
        yhdistelmä = self.nimi
        return Suorakulmio(yhdistelmä, uusi_leveys, uusi_korkeus)
    
def tulosta_alat(lista: list):
    for olio in lista:
        print(olio.ala())

#NOPPAPELI.    
import random
class Noppa:
    def __init__(self, sivujen_maara: int = 6):
        self.__sivujen_maara = sivujen_maara


    def heita_noppaa(self, kerrat: int):
        tulokset = []
        for i in range(kerrat):
            luku = random.randint(1, self.__sivujen_maara)
            tulokset.append(luku)
        return tulokset


    def __str__(self):
        return f"{self.__sivujen_maara}-sivuinen noppa"

class Noppapeli():
    def __init__(self, noppa_olio):
        self.__noppa_olio = noppa_olio

    def heita_kerran(self):
        lista = sorted(self.__noppa_olio.heita_noppaa(5)) #miten saa tulokset toisesta luokasta!
        if lista[0] == lista[-1]:
            print("Yatzy!")
        else:
            print(lista)
    
    def heita_viisi_samaa(self):
        laskuri = 0
        while True:
            laskuri += 1
            lista = sorted(self.__noppa_olio.heita_noppaa(5))
            if lista[0] == lista[-1]:
                print(laskuri)
                break


    def __str__(self):
        return f"Pelin tarkoitus on saada noppia heittämällä 5 samaa lukua. Käytössä on 6-sivuinen noppa."
        



class Auto:
    def __init__(self, automerkki: str, ostovuosi: int, osto_hinta: int):
        self.automerkki = automerkki
        self.ostovuosi = ostovuosi
        self.osto_hinta = osto_hinta
        self.ajettu_matka = 0 #auto muistaa paljonko sillä on ajettu
        self.kulut = 0 #auto muistaa paljonkot kuluja on kertynyt

    def aseta_vuosi(self, luku: int):
        self.ostovuosi = luku

    def aja(self, ajettu_matka: int, hinta_per_kilometri: float):
        self.ajettu_matka += ajettu_matka
        kustannus = ajettu_matka * hinta_per_kilometri
        self.kulut += kustannus



    def lisaa_kulu(self, luku: int):
        self.kulut += luku

    def autolla_ajettu(self):
        return self.ajettu_matka

    def arvo_nyt(self):

    def kustannus_per_kilometri(self):
        if self.ajettu_matka == 0:
            return 0
        arvon_aleneminen = self.osto_hinta - self.arvo_nyt()#käytetään toista metodia!
        kokonaiskulut = self.kulut + arvon_aleneminen
        kustannus_rahana = kokonaiskulut / self.ajettu_matka
        return kustannus_rahana

    def __str__(self):
        return f"{self.automerkki}: ostovuosi {self.ostovuosi}, arvo {self.arvo_nyt()}"
        
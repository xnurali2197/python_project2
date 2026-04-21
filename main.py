class Kitob:
    def __init__(self, nomi, muallifi, sahifalari, narxi):
        self.nomi = nomi
        self.muallifi = muallifi
        self.sahifalari = sahifalari
        self.narxi = narxi

    def kitob_haqida(self):
        print(f"Kitobning nomi: {self.nomi}")
        print(f"Kitobning muallifi: {self.muallifi}")
        print(f"Kitobning sahifalari: {self.sahifalari}")
        print(f"Kitobning narxi: {self.narxi}")

    def narxni_ozgartirish(self, yangi_narx):
        self.narxi = yangi_narx
        print(f"Kitobning yangi narxi: {self.narxi}")

class Do_kon:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def kitob_haqida_chop(self):
        for kitob in self.kitoblar:
            kitob.kitob_haqida()

kitob1 = Kitob("Olma", "G'afur G'ulom", 300, 20000)
kitob2 = Kitob("Qizil olma", "Shukrullo", 250, 25000)

do_kon = Do_kon("Savol", "Toshkent")
do_kon.kitob_qoshish(kitob1)
do_kon.kitob_qoshish(kitob2)

kitob1.narxni_ozgartirish(22000)
do_kon.kitob_haqida_chop()
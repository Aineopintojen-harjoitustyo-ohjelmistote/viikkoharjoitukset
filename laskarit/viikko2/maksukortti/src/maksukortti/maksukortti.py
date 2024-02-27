# pylint: disable = missing-module-docstring, missing-class-docstring, missing-function-docstring
class Maksukortti:
    def __init__(self, alkusaldo):
        self.saldo = alkusaldo

    def saldo_euroina(self):
        return self.saldo / 100

    def syo_maukkaasti(self):
        if self.saldo >= 400:
            self.saldo -= 400

    def syo_edullisesti(self):
        if self.saldo >= 250:
            self.saldo -= 250

    def lataa_rahaa(self, summa):
        self.saldo += summa
        self.saldo = min(self.saldo, 15000)

    def __str__(self):
        return f"Kortilla on rahaa {self.saldo/100:.2f} euroa"

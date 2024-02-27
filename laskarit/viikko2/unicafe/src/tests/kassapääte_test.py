import unittest
from kassapääte import Kassapääte
from maksukortti import Maksukortti

class TestKassapääte(unittest.TestCase):
    def setUp(self):
        self.kassapääte = Kassapääte()

    def test_luokan_luominen_onnistuu(self):
        self.assertNotEqual(self.kassapääte, None)

    def test_uudella_luokalla_oikea_määrä_rahaa_ja_myytyjä(self):
        self.assertEqual(self.kassapääte.kassassa_rahaa, 100_000)
        self.assertEqual(self.kassapääte.edulliset, 0)
        self.assertEqual(self.kassapääte.maukkaat, 0)
        
    def test_edullisen_lounaan_ostamien_käteisellä_onnistuu(self):
        raha = 1000
        raha = self.kassapääte.syö_edullisesti_käteisella(raha)
        self.assertEqual(self.kassapääte.edulliset, 1)
        self.assertEqual(raha, 760)

    def test_edullisen_lounaan_ostamien_vähällä_käteisellä_ei_onnistu(self):
        raha = 200
        raha = self.kassapääte.syö_edullisesti_käteisella(raha)
        self.assertEqual(self.kassapääte.edulliset, 0)
        self.assertEqual(raha, 200)

    def test_maukkaan_lounaan_ostamien_käteisellä_onnistuu(self):
        raha = 1000
        raha = self.kassapääte.syö_maukkaasti_käteisella(raha)
        self.assertEqual(self.kassapääte.maukkaat, 1)
        self.assertEqual(raha, 600)

    def test_maukkaan_lounaan_ostamien_vähällä_käteisellä_ei_onnistu(self):
        raha = 200
        raha = self.kassapääte.syö_maukkaasti_käteisella(raha)
        self.assertEqual(self.kassapääte.maukkaat, 0)
        self.assertEqual(raha, 200)

    def test_edullisen_lounaan_ostaminen_kortilla_onnistuu(self):
        kortti = Maksukortti(400)
        self.assertTrue(self.kassapääte.syö_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapääte.edulliset, 1)
        self.assertEqual(self.kassapääte.kassassa_rahaa, 100_000)
        self.assertEqual(kortti.saldo, 160)

    def test_maukkaan_lounaan_ostaminen_kortilla_onnistuu(self):
        kortti = Maksukortti(400)
        self.assertTrue(self.kassapääte.syö_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassapääte.maukkaat, 1)
        self.assertEqual(self.kassapääte.kassassa_rahaa, 100_000)
        self.assertEqual(kortti.saldo, 0)

    def test_edullisen_lounaan_ostaminen_katteettomalla_kortilla(self):
        kortti = Maksukortti(100)
        self.assertFalse(self.kassapääte.syö_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapääte.edulliset, 0)
        self.assertEqual(self.kassapääte.kassassa_rahaa, 100_000)
        self.assertEqual(kortti.saldo, 100)

    def test_maukkaan_lounaan_ostaminen_katteettomalla_kortilla(self):
        kortti = Maksukortti(100)
        self.assertFalse(self.kassapääte.syö_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassapääte.maukkaat, 0)
        self.assertEqual(self.kassapääte.kassassa_rahaa, 100_000)
        self.assertEqual(kortti.saldo, 100)

    def test_kortin_lataaminen_onnistuu(self):
        kortti = Maksukortti(100)
        self.assertFalse(self.kassapääte.lataa_rahaa_kortille(kortti,1_000))
        self.assertEqual(self.kassapääte.kassassa_rahaa, 101_000)
        self.assertEqual(kortti.saldo, 1100)

    def test_kortin_lataaminen_negatiivisellä_ei_tee_mitään(self):
        kortti = Maksukortti(0)
        self.assertFalse(self.kassapääte.lataa_rahaa_kortille(kortti,-100))
        self.assertEqual(self.kassapääte.kassassa_rahaa, 100_000)
        self.assertEqual(kortti.saldo, 0)

    def test_kassassa_rahaa_euroina_palauttaa_oikein(self):
        self.assertEqual(self.kassapääte.kassassa_rahaa_euroina(), 1000)

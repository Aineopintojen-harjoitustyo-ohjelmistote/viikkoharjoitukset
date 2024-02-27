import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikein_aluksi(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kortin_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_rahan_ottaminen_vähentää_saldoa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 500)
        
    def test_rahan_ottaminen_ei_onnistu_ilman_saldoa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo, 1000)
        
    def test_rahan_ottaminen_palauttaa_oikein(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))
        self.assertTrue(self.maksukortti.ota_rahaa(500))
        self.assertFalse(self.maksukortti.ota_rahaa(500))
        

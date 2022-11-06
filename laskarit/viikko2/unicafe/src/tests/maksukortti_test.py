import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")

    def test_raha_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 20.00 euroa")

    def test_rahan_ottaminen_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")

    def test_kortin_saldo_ei_vahene_jos_rahaa_ei_ole(self):
        maksukortti = Maksukortti(200)
        maksukortti.ota_rahaa(250)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 2.00 euroa")

    def test_metodi_palauttaa_oikean_totuusarvon(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
        self.assertEqual(self.maksukortti.ota_rahaa(15000), False)

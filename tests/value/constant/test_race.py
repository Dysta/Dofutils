from unittest import TestCase

from dofutils.value.constant import Race


class TestRace(TestCase):
    def test_by_id(self):
        for i in range(13):
            self.assertEqual(Race(i), Race.by_id(i))

    def test_by_id_wrong_param(self):
        self.assertRaises(ValueError, Race.by_id, race_id=-1)
        self.assertRaises(ValueError, Race.by_id, race_id=13)
        self.assertRaises(ValueError, Race.by_id, race_id="5")
        self.assertRaises(ValueError, Race.by_id, race_id="95")

    def test_eq_operator(self):
        assert Race.FECA == Race.by_id(1)
        assert Race.OSAMODAS == Race.by_id(2)
        assert Race.ENUTROF == Race.by_id(3)
        assert Race.SRAM == Race.by_id(4)
        assert Race.XELOR == Race.by_id(5)
        assert Race.ECAFLIP == Race.by_id(6)
        assert Race.ENIRIPSA == Race.by_id(7)
        assert Race.IOP == Race.by_id(8)
        assert Race.CRA == Race.by_id(9)
        assert Race.SADIDA == Race.by_id(10)
        assert Race.SACRIEUR == Race.by_id(11)
        assert Race.PANDAWA == Race.by_id(12)

    def test_str_operator(self):
        assert str(Race.FECA) == "FECA"
        assert str(Race.OSAMODAS) == "OSAMODAS"
        assert str(Race.ENUTROF) == "ENUTROF"
        assert str(Race.SRAM) == "SRAM"
        assert str(Race.XELOR) == "XELOR"
        assert str(Race.ECAFLIP) == "ECAFLIP"
        assert str(Race.ENIRIPSA) == "ENIRIPSA"
        assert str(Race.IOP) == "IOP"
        assert str(Race.CRA) == "CRA"
        assert str(Race.SADIDA) == "SADIDA"
        assert str(Race.SACRIEUR) == "SACRIEUR"
        assert str(Race.PANDAWA) == "PANDAWA"

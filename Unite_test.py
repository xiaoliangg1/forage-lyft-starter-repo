import unittest
from engine import capulet_engine as ce
from engine import sternman_engine as se
from engine import willoughby_engine as we
from battery import nubbinBattery as nb
from battery import spindlerBattery as sb

class TestEngine(unittest.TestCase):

    def test_capulet_engine_true(self):
        engine = ce.CapuletEngine(0, 30001, 0)
        self.assertTrue(engine.engine_should_be_serviced())


    def test_capulet_engine_false(self):
        engine = ce.CapuletEngine(0, 30000, 0)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_sternman_engine_true(self):
        engine = se.SternmanEngine(0, True)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_sternman_engine_false(self):
        engine = se.SternmanEngine(0, False)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_willoughby_engine_true(self):
        engine = we.WilloughbyEngine(0, 60001, 0)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_willoughby_engine_false(self):
        engine = we.WilloughbyEngine(0, 60000, 0)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_nubbinBattery_true(self):
        engine = nb.NubbinBattery(0, 30001)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_nubbinBattery_false(self):
        engine = nb.NubbinBattery(0, 30000)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_spindlerBattery_true(self):
        engine = sb.SpindlerBattery(0, 60001)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_spindlerBattery_false(self):
        engine = sb.SpindlerBattery(0, 60000)
        self.assertTrue(engine.engine_should_be_serviced())

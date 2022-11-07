from unittest import TestCase

from ordersystem import OrderSystem


class TestOrderSystem(TestCase):
    def test_process(self):
        a = OrderSystem()
        res = a.process("k")
        assert res == ""

        res = a.process("\n")
        text = res[0:15]
        assert text == "\r\nWe sell we de", f"Wrong text: {text}"

        res = a.process("q\n")
        text = res[0:15]
        assert text == "\r\nWe sell we de", f"Wrong text: {text}"

        res = a.process("a")
        assert res == ""

        res = a.process("\n")
        text = res[0:15]
        assert text == "\r\nyou want a, t", f"Wrong text: {text}"

        res = a.process("banan\n")
        text = res[0:30]
        assert text == "a ordered to team banan thank ", f"Wrong text: {text}"

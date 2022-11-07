from unittest import TestCase

from Processor import Processor


class TestProcessor(TestCase):
    def test_process(self):
        pro = Processor({"a":"baba", "c":"blablabla"})
        ret = pro.process("g")
        assert ret == ""

        ret = pro.process("\n")
        assert ret == "Bad cmd."

        ret = pro.process("h\n")
        assert ret == "Bad cmd."

        ret = pro.process("a\n")
        assert ret == "baba"
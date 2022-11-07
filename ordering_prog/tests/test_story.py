from unittest import TestCase

from story import Story


class TestStory(TestCase):
    def test_process(self):
        s = [{"story": "we ain't up to no good", "forward": "bad mojo"},
             {"story": "no shit sherlock", "down": "heyheyhey"},
             {"story": "blabla", "sideways": "whatupnow"},
             {"story": "somthn", "search": "tada"}]

        story = Story(s)

        ret = story.process("agblkfadfb\n")

        assert ret == s[0]["story"], f"wrong story: {ret}"

        ret = story.process("forward")

        assert ret == ""

        ret = story.process("\n")
        assert ret == s[0]["forward"], f"wrong story: {ret}"

        ret = story.process("blabla\n")
        assert ret == s[1]["story"], f"wrong story: {ret}"

        ret = story.process("down\n")
        assert ret == s[1]["down"], f"wrong story: {ret}"

        ret = story.process("sideways\n")
        assert ret == s[2]["sideways"], f"wrong story: {ret}"

        ret = story.process("balbal\n")
        assert ret == s[3]["story"], f"wrong story: {ret}"

        ret = story.process("back\n")
        assert ret == s[2]["story"], f"wrong story: {ret}"

        ret = story.process("back\n")
        assert ret == s[1]["story"], f"wrong story: {ret}"


class Processor:

    def __init__(self, commands):
        self.input = ""
        self.commands = commands

    def process(self, data):

        if "\n" not in data:
            self.input += data
            return ""
        if len(data) > 1:
            self.input += data.strip()

        if self.input in self.commands:

            ret = self.commands[self.input]
            self.input = ""
            return ret

        else:
            self.input = ""
            return "Bad cmd."
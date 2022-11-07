
class Story:
    def __init__(self, story):
        self.story = story
        self.story_entry = 0
        self.go_back = ["return", "back", "exit", "break", "run"]
        self.input = ""

    def process(self, data):

        if "\n" not in data:
            self.input += data
            return ""
        if len(data) > 1:
            self.input += data.strip()

        if self.input in self.story[self.story_entry]:

            ret = self.story[self.story_entry][self.input]
            self.input = ""
            self.story_entry += 1
            if self.story_entry >= len(self.story):
                self.story_entry = 0
            return ret
        elif self.input in self.go_back:
            self.input = ""
            self.story_entry -= 1
            if self.story_entry < 0:
                self.story_entry = 0
            ret = self.story[self.story_entry]["story"]
            return ret
        else:
            self.input = ""
            return self.story[self.story_entry]["story"]
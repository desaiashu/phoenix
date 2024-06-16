from analyzer import Analyzer

class Audio:
    def __init__(self, handlers):
        self.analyzer = Analyzer()
        self.values = None

    def read(self):
        return self.values

    def update(self):
        self.values = self.analyzer.ReadFreq()
        print(self.values)
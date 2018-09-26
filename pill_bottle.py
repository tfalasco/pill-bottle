from random import seed
from random import randint
from datetime import datetime

class Bottle:
    def __init__(self, pill_count):
        seed(datetime.now())
        self.wholes = pill_count
        self.halves = 0

    def consumeHalfPill(self):
        self.total_pills = self.wholes + self.halves
        self.pill = randint(1, self.total_pills)                   # pick a random pill
        if self.pill > self.wholes:                                # if it's a half pill, take it
            self.halves -= 1
        else:                                                      # otherwise cut it in half and put half back
            self.wholes -= 1
            self.halves += 1

    def getPillCounts(self):
        self.counts_dictionary = {
            "wholes": self.wholes,
            "halves": self.halves
        }
        return self.counts_dictionary


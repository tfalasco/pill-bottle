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
        self.pill = randint(1, self.total_pills)          # pick a random pill
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


def main():
    print("pill bottle")

    output_file = open("./pill_bottle_output.csv", "w+")
    output_file.write("Day, Whole pills, Half pills, Difference\n")

    day = 0
    pill_bottle = Bottle(275)
    counts = pill_bottle.getPillCounts()
    total_pills = counts["wholes"] + counts["halves"]
    difference = counts["wholes"] - counts["halves"]
    daily_record = [day, counts["wholes"], counts["halves"], difference]
    daily_records = [daily_record]

    while total_pills > 0:
        day += 1
        pill_bottle.consumeHalfPill()
        counts = pill_bottle.getPillCounts()

        #create a new daily record
        total_pills = counts["wholes"] + counts["halves"]
        difference = counts["wholes"] - counts["halves"]
        daily_record = [day, counts["wholes"], counts["halves"], difference]
        daily_records.append(daily_record)

    for record in daily_records:
        for i in range(4):
            output_file.write(str(record[i]))
            if i < 3:
                output_file.write(", ")
            else:
                output_file.write("\n")

if __name__ == "__main__":
    main()

from random import seed
from random import randint
from datetime import datetime

def main():
    print("pill bottle")

    output_file = open("./pill_bottle_output.csv", "w+")
    output_file.write("Day, Whole pills, Half pills, Difference\n")

    seed(datetime.now())
    day = 0
    wholes = 275
    halves = 0
    total_pills = wholes + halves
    difference = wholes - halves
    daily_record = [day, wholes, halves, difference]
    daily_records = [daily_record]

    while total_pills > 0:
        day += 1
        pill = randint(1, total_pills)          # pick a random pill

        if pill > wholes:                       # if it's a half pill, take it
            halves -= 1
        else:                                   # otherwise cut it in half and put half back
            wholes -= 1
            halves += 1

        #create a new daily record
        total_pills = wholes + halves
        difference = wholes - halves
        daily_record = [day, wholes, halves, difference]
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

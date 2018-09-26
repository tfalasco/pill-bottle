from pill_bottle import Bottle

def consume_one_bottle(number_of_pills_per_bottle):
    day = 0
    pill_bottle = Bottle(number_of_pills_per_bottle)
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

    return daily_records


def main():
    output_file = open("./pill_bottle_output.csv", "w+")
    output_file.write("Day, Whole pills, Half pills, Difference\n")

    number_of_runs = 100
    number_of_pills_per_bottle = 275

    for run in range(number_of_runs):

        daily_records = consume_one_bottle(number_of_pills_per_bottle)

        if run == 0:
            total_daily_records = daily_records
        else:
            for record_num in range(len(daily_records)):
                total_daily_records[record_num][1] += daily_records[record_num][1]
                total_daily_records[record_num][2] += daily_records[record_num][2]
                total_daily_records[record_num][3] += daily_records[record_num][3]


    for record in total_daily_records:
        record[1] /= number_of_runs
        record[2] /= number_of_runs
        record[3] /= number_of_runs
        for i in range(4):
            output_file.write(str(record[i]))
            if i < 3:
                output_file.write(", ")
            else:
                output_file.write("\n")

if __name__ == "__main__":
    main()
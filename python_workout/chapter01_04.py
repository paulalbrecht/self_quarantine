
total_runs = 0
total_mins = 0

while True:
    run_time = input("How long did the run take: ")

    if run_time == "q":
        break
    else:
        total_runs += 1
        total_mins += int(run_time)


average_runtime = total_mins / total_runs
print(f"Average time was {average_runtime} over {total_runs}")


def truncate_float(f, before, after):
    t = str(f).split(".")
    print(f"{t[0][-before:]}.{t[1][:after]}")

truncate_float(1234.5678, 2, 2)

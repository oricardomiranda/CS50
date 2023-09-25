def main():
    time = input("What time is it? (HH:MM or H:MM): ")
    total_time = convert(time)

    if 7.0 <= total_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= total_time <= 13.0:
        print("lunch time")
    elif 18.0 <= total_time <= 19.0:
        print("dinner time")

def convert(time):
    if ":" in time:
        hours, minutes = map(int, time.split(":"))
    else:
        if len(time) == 3:
            hours = int(time[0])
            minutes = int(time[1:])
        elif len(time) == 4:
            hours = int(time[:2])
            minutes = int(time[2:])
        else:
            return "Invalid time format"

    total_time = hours + minutes / 60
    return total_time

if __name__ == "__main__":
    main()

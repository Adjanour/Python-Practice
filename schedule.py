def get_activity(time_slot):
    """Prompts the user for an activity for the given time slot"""
    return input(f"Enter activity for {time_slot}: ")

def build_schedule():
    """Dynamically builds the schedule dictionary"""
    schedule = {}
    while True:
        day = input("Enter day (or type 'done' to finish): ")
        if day.lower() == "done":
            break  

        schedule[day] = {}
        while True:
            time_slot = input("Enter time slot (or type 'done'): ")
            if time_slot.lower() == "done":
                break

            activity = get_activity(time_slot)
            schedule[day][time_slot] = activity

    return schedule

# Build the schedule dynamically
schedule = build_schedule()

# The rest of the code remains the same:
def write_schedule(schedule_data):
    """Generates a schedule.txt file with provided schedule information"""

    with open("schedule.txt", "w") as file:
        for day, activities in schedule_data.items():
            file.write(f"{day}\n")
            for time_slot, activity in activities.items():
                file.write(f"{time_slot}: {activity}\n")
            file.write("\n")  # Add an empty line to separate days

write_schedule(schedule) 

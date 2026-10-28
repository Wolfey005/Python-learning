# Try 8.2.1: Amusement park ride reservation system.

# Full screen
# The following (unfinished) program implements a digital line queuing system for an amusement park ride. The system allows a rider to reserve a place in line without actually having to wait. The rider simply enters a name into a program to reserve a place. Riders that purchase a VIP pass get to skip past the common riders up to the last VIP rider in line. VIPs board the ride first. (Considering the average wait time for a Disneyland ride is about 45 minutes (Disneyland Crowd Levels), this might be a useful program.) For this system, an employee manually selects when the ride is dispatched (thus removing the next riders from the front of the line).

# Complete the following program, as described above. Once finished, add the following commands:

# The rider can enter a name to find the current position in line. (Hint: Use the list.index() method.)
# The rider can enter a name to remove the rider from the line.



riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ("(1) Reserve place in line.\n"  # Add rider to line
        "(2) Reserve place in VIP line.\n"  # Add VIP
        "(3) Dispatch riders.\n"  # Dispatch next ride car
        "(4) Find rider.\n"  # Find a rider's current position in line
        "(5) Remove rider.\n"  # Remove a rider from the line
        "(6) Print riders.\n"
        "(7) Exit.\n\n")

user_input = input(menu).strip().lower()

while user_input != "7":
    if user_input == "1":  # Add rider
        name = input("Enter name: ").strip().lower()
        print(name)
        line.append(name)

    elif user_input == "2":  # Add VIP
        print("Add new VIP")
        name = input("Enter name: ").strip().lower()
        print(name)
        # Add new rider behind last VIP in line
        line.insert(num_vips, name)
        # Don't forget to increment num_vips.
        num_vips += 1

    elif user_input == "3":  # Dispatch ride
        print(f"{line[0]} is now on the ride")
        # Remove last riders_per_ride from front of line.
        line.pop(0)
        # Don't forget to decrease num_vips, if necessary.
        if num_vips > 0:
            num_vips -= 1

    elif user_input == "4":  # Find a rider's current position in line
        name = input("Enter name to find: ").strip().lower()
        if name in line:
            print(f"{name} is in line at position {str(line.index(name))}")
        else:
            print(f"{name} is not in line")

    elif user_input == "5":  # Remove a rider from the line
        name = input("Enter name to remove: ").strip().lower()
        if name in line:
            num = line.index(name)
            if num < num_vips:
                num_vips -= 1
            line.remove(name)
            print(f"{name} was removed from the line")
        else:
            print(f"{name} was not in line")

    elif user_input == "6":  # Print riders waiting in line
        print(f"{len(line)} person(s) waiting: {line}")

    else:
        print("Unknown menu option")

    user_input = input("Enter command: ").strip().lower()
    print(user_input)



    ################################################test output ######
#     (1) Reserve place in line.
# (2) Reserve place in VIP line.
# (3) Dispatch riders.
# (4) Find rider.
# (5) Remove rider.
# (6) Print riders.
# (7) Exit.

# 1
# Enter name: jenny
# jenny
# Enter command: 1
# 1
# Enter name: ryan
# ryan
# Enter command: 1
# 1
# Enter name: alex
# alex
# Enter command: 1
# 1
# Enter name: olivia
# olivia
# Enter command: 4
# 4
# Enter name to find: olivia
# olivia is in line at position 3
# Enter command: 2
# 2
# Add new VIP
# Enter name: connie
# connie
# Enter command: 3
# 3
# connie is now on the ride
# Enter command: 3
# 3
# jenny is now on the ride
# Enter command: 6
# 6
# 3 person(s) waiting: ['ryan', 'alex', 'olivia']
# Enter command: 5
# 5
# Enter name to remove: connie
# connie was not in line
# Enter command: 6
# 6
# 3 person(s) waiting: ['ryan', 'alex', 'olivia']
# Enter command:


river_num = int(input())
 
# Major rivers (1-99)
if (river_num >= 1) and (river_num <= 99):
    if river_num % 2 == 0:
        direction = "east/west"
    else:
        direction = "north/south"
 
    print(f"River-{river_num} is a major river, flowing {direction}.")
 
# Creeks (100-999)
elif (100 <= river_num <= 999):
    parent_river = river_num % 100
 
    if parent_river == 0:
        print(f"River-{river_num} is not a valid river number.")
    else:
        if parent_river % 2 == 0:
            direction = "east/west"
        else:
            direction = "north/south"
 
        print(
            f"Creek-{river_num} flows into River-{parent_river}, flowing {direction}."
        )
 
# Invalid number
else:
    print(f"{river_num} is not a valid river number.")

    ##why wont you save
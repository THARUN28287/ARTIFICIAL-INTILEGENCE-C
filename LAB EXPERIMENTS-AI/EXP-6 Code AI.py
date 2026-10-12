
def vacuum_cleaner():
    room = {'A': 1, 'B': 1}
    position = 'A'

    while 1 in room.values():
        print("Vacuum at", position)

        if room[position] == 1:
            room[position] = 0
            print("Room", position, "cleaned")
        else:
            print("Room", position, "is clean")

        if position == 'A':
            position = 'B'
        else:
            position = 'A'

    print("All rooms are clean")

vacuum_cleaner()

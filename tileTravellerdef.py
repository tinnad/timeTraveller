def move():
    if direction == 'n' or direction == 'N':
        location += 1
    elif direction == 's' or direction == 'S':
        location -= 1
    elif direction == 'e' or direction == 'E':
        location += 10
    elif direction == 'w' or direction == 'W':
        location -= 10
    return location

def get_direction():
    if location == 11 or location == 21:
        print('You can travel: (N)orth.')
    if location == 12:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
    if location == 13:
        print('You can travel: (E)ast or (S)outh.')
    if location == 23:
        print('You can travel: (E)ast or (W)est.')
    if location == 33 or location == 22:
        print('You can travel: (W)est or (S)outh.')
    if location == 32:
        print('You can travel: (N)orth or (S)outh.')
    if location == 32:
        print('Victory!')

location = 11
direction = input('direction: ' )
while location != 31:
    get_direction(location)
    direction = input('Direction: ')
    move()

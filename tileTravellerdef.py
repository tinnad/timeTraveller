def tile11(direction):
    while direction != 'N':
        direction = str(input("Direction: ")).upper()
        if direction == 'N':
            return 1.2
        else:
            print('Not a valid direction!')

def tile12(direction):
    while direction != 'N' and direction != 'S' and direction != 'E':
        direction = str(input("Direction: ")).upper()
        if direction == 'N':
            return 1.3
        elif direction == 'E':
            return 2.2
        elif direction == 'S':
            return 1.1
        else:
            print('Not a valid direction!')
def tile13(direction):
    while direction != 'E' and direction != 'S':
        direction = str(input("Direction: ")).upper()
        if direction == 'E':
            return 2.3
        elif direction == 'S':
            return 1.2
        else:
            print('Not a valid direction!')

def tile21(direction):
    while direction != 'N':
        direction = str(input("Direction: ")).upper()
        if direction == 'N':
            return 2.2
        else:
            print('Not a valid direction!')

def tile22(direction):
    while direction != 'W' and direction != 'S':
        direction = str(input("Direction: ")).upper()
        if direction == 'S':
            return 2.1
        elif direction == 'W':
            return 1.2
        else:
            print('Not a valid direction!')
def tile23(direction):
            while direction != 'E' and direction != 'W':
                direction = str(input("Direction: ")).upper()
                if direction == 'E':
                    return 3.3
                elif direction == 'W':
                    return 1.3
                else:
                    print('Not a valid direction!')

def tile32(direction):
    while direction != 'N' and direction != 'S':
        direction = str(input("Direction: ")).upper()
        if direction == 'N':
            return 3.3
        elif direction == 'S':
            return 3.1
        else:
            print('Not a valid direction!')

def tile33(direction):
    while direction != 'S' and direction != 'W':
        direction = str(input("Direction: ")).upper()
        if direction == 'S':
            return 3.2
        elif direction == 'W':
            return 2.3
        else:
            print('Not a valid direction!')

location = 1.1

while location != 3.1:
    if location == 1.1:
        print('You can travel: (N)orth.')
        direction = ''
        location = tile11(direction)

    if location == 1.2:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
        direction = 'W'
        location = tile12(direction)

    if location == 1.3:
        print('You can travel: (E)ast or (S)outh.')
        direction = ''
        location = tile13(direction)

    if location == 2.1:
        print('You can travel: (N)orth.')
        direction = ''
        location = tile21(direction)

    if location == 2.2:
        print('You can travel: (S)outh or (W)est.')
        direction = ''
        location = tile22(direction)

    if location == 2.3:
        print('You can travel: (E)ast or (W)est.')
        direction = ''
        location = tile23(direction)

    if location == 3.2:
        print('You can travel: (N)orth or (S)outh.')
        direction = ''
        location = tile32(direction)
    
    if location == 3.3:
        print('You can travel: (S)outh or (W)est.')
        direction = ''
        location = tile33(direction)

print('Victory!')
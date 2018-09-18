# attir = print('You can travel: ')
# direction = input('Direction: ')
location = 11

while location != 31:
    # direction = input('Direction: ')
    # if direction == 'n' or direction == 'N':
    #     location += 1
    # elif direction == 'e' or direction == 'E':
    #     location += 10
    # elif direction == 'w' or direction == 'W':
    #     location -= 10
    # elif direction == 's' or direction == 'S':
    #     location -= 1
    # else:
    #     print('Not a valid direction!')
    #     direction = input('Direction: ')

    if location == 11 or location == 21:
        print('You can travel: (N)orth.')
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location += 1
            break
        else:
        #elif direction != 'n' or direction != 'N':
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 12:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
        direction = input('Direction: ')
        if direction == 's' or direction == 'S':
            location -= 1
        elif direction == 'e' or direction == 'E':
            location += 10
        elif direction == 'n' or direction == 'N':
            location += 1
        else:
        #elif direction != 'n' or direction != 'N' or direction != 's' or direction != 'S' or direction != 'E' or direction != 'e':
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 13:
        print('You can travel: (E)ast or (S)outh.')
        direction = input('Direction: ')
        if direction == 's' or direction == 'S':
            location -= 1
        elif direction == 'e' or direction == 'E':
            location += 10
        else:
        #elif direction != 'e' or direction != 'E' or direction != 's' or direction != 'S':
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 23:
        print('You can travel: (E)ast or (W)est.')
        direction = input('Direction: ')
        if direction == 'e' or direction == 'E':
            location += 10
        elif direction == 'w' or direction == 'W':
            location -= 10
        else:
        #elif direction != 'e' or direction != 'E' or direction != 'W' or direction != 'w':
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 33 or location == 22: 
        print('You can travel: (W)est or (S)outh.')
        direction = input('Direction: ')
        if direction == 'w' or direction == 'W':
            location -= 10
        elif direction == 's' or direction == 'S':
            location -= 1
        else:
        #elif direction != 's' or direction != 'S' or direction != 'w' or direction != 'W':
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 32:
        print('You can travel: (N)orth or (S)outh.')
        direction = input('Direction: ')
        if direction == 'N' or direction == 'n':
            location += 1
        elif direction == 's' or direction == 'S':
           location -= 1
        else:
        #elif direction != 'n' or direction != 'N' or direction != 's' or direction != 'S':
            print('Not a valid direction!')
            direction = input('Direction: ')

    if direction == 31:
        print('Victory')
        break


    
  




                
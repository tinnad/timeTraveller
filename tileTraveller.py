location = 11
invalidinput = False
while location != 31:

    if location == 11 or location == 21:
        if invalidinput == False:
            print('You can travel: (N)orth.')
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location += 1
        else:
            invalidinput = True
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 12:
        if invalidinput == False:
            print('You can travel: (N)orth or (E)ast or (S)outh.')
        direction = input('Direction: ')
        if direction == 's' or direction == 'S':
            location -= 1
        elif direction == 'e' or direction == 'E':
            location += 10
        elif direction == 'n' or direction == 'N':
            location += 1
        else:
            invalidinput = True
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 13:
        if invalidinput == False:
            print('You can travel: (E)ast or (S)outh.')
        direction = input('Direction: ')
        if direction == 's' or direction == 'S':
            location -= 1
        elif direction == 'e' or direction == 'E':
            location += 10
        else:
            invalidinput = True
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 23:
        if invalidinput == False:
            print('You can travel: (E)ast or (W)est.')
        direction = input('Direction: ')
        if direction == 'e' or direction == 'E':
            location += 10
        elif direction == 'w' or direction == 'W':
            location -= 10
        else:
            invalidinput = True
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 33 or location == 22: 
        if invalidinput == False:
            print('You can travel: (W)est or (S)outh.')
        direction = input('Direction: ')
        if direction == 'w' or direction == 'W':
            location -= 10
        elif direction == 's' or direction == 'S':
            location -= 1
        else:
            invalidinput = True
            print('Not a valid direction!')
            direction = input('Direction: ')

    if location == 32:
        if invalidinput == False:
            print('You can travel: (N)orth or (S)outh.')
        direction = input('Direction: ')
        if direction == 'N' or direction == 'n':
            location += 1
        elif direction == 's' or direction == 'S':
           location -= 1
        else:
            invalidinput = True
            print('Not a valid direction!')
            direction = input('Direction: ')

print('Victory')


    
  




                
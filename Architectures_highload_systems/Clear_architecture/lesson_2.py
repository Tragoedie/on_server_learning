from math import sin, cos, radians

WATER = 'water'
SOAP = 'soap'
BRUSH = 'brush'

MOVE = 'move'
TURN = 'turn'
SET = 'set'
START = 'start'
STOP = 'stop'


def execute(*command_string):
    angle = 0
    pos_x = 0.0
    pos_y = 0.0
    state = ''
    for command in command_string:
        if command.find(MOVE) != -1:
            move_distance = command.split()[1]
            try:
                val = float(move_distance)
                pos_y -= val * sin(radians(angle))
                pos_x += val * cos(radians(angle))
                print('POS {0},{1}'.format(pos_x, pos_y))
            except ValueError:
                print('Wrong move distance - {0}!'.format(move_distance))
        elif command.find(TURN) != -1:
            turn_angle = command.split()[1]
            try:
                val = int(turn_angle)
                angle += val
                print('ANGLE {0}'.format(angle))
            except ValueError:
                print('Wrong turn angle - {0}!'.format(turn_angle))
        elif command.find(SET) != -1:
            new_state = command.split()[1]
            if new_state != WATER and new_state != BRUSH and new_state != SOAP:
                print('Wrong state - {0}!'.format(new_state))
            else:
                state = new_state
                print('STATE ', state)
        elif command == START:
            if state == '':
                print('Starting error! Please, enter state first!')
            else:
                print('START WITH ', state)
        elif command == STOP:
            print('STOP')
        else:
            print('Unknown command - {0}!'.format(command))


execute('move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop')

"""
lesson_1: 
не использовала 'школьный' стиль, после прохождения прошлых курсов, попыталсь сразу написать решение через класс. 
"""
from math import sin, cos, radians
from collections import namedtuple

RobotState = namedtuple("RobotState", "x y angle state")

WATER = 'water'
SOAP = 'soap'
BRUSH = 'brush'


def pring_msg(message):
    print(message)


def __move(distance, state):
    pring_msg('Position: {0}, {1}'.format(state.x + distance * cos(radians(state.angle)),
                                          state.y - distance * sin(radians(state.angle))))
    return RobotState(state.x + distance * cos(radians(state.angle)), state.y - distance * sin(radians(state.angle)),
                      state.angle, state.state)


def __turn(turn_angle, state):
    pring_msg('Angle: {0}'.format(state.angle + turn_angle))
    return RobotState(state.x, state.y, state.angle + turn_angle, state.state)


def __set_state(new_state, state):
    pring_msg('State: {0}'.format(new_state))
    return RobotState(state.x, state.y, state.angle, new_state)


def __start(state):
    pring_msg('Start with {0}'.format(state.state))
    return state


def __stop(state):
    pring_msg('Stop')
    return state


def __translate_command(command, state):
    if command[0] == 'move':
        return __move(int(command[1]), state)
    elif command[0] == 'turn':
        return __turn(int(command[1]), state)
    elif command[0] == 'set':
        return __set_state(command[1], state)
    elif command[0] == 'start':
        return __start(state)
    elif command[0] == 'stop':
        return __stop(state)


def __execute(code, start_index, state):
    if len(code) > start_index:
        __execute(code, start_index + 1, __translate_command(code[start_index].split(), state))


def make(code):
    __execute(code, 0, RobotState(0.0, 0.0, 0, WATER))


make(('move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop'))

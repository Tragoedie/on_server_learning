from math import sin, cos, radians

WATER = 'water'
SOAP = 'soap'
BRUSH = 'brush'

MOVE = 'move'
TURN = 'turn'
SET = 'set'
START = 'start'
STOP = 'stop'


class RobotJanitor:
    def __init__(self, pos_x=0.0, pos_y=0.0):
        self.angle = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.state = ''

    def __move(self, distance):
        self.pos_y -= distance * sin(radians(self.angle))
        self.pos_x += distance * cos(radians(self.angle))
        print('POS {0},{1}'.format(self.pos_x, self.pos_y))

    def __turn(self, angle):
        self.angle += angle
        print('ANGLE {0}'.format(self.angle))

    def __set(self, state=WATER):
        self.state = state
        print('STATE ', state)

    def __start(self):
        if self.state == '':
            print('Starting error! Please, enter state first!')
        else:
            print('START WITH ', self.state)

    def __stop(self):
        print('STOP')

    def execute(self, *command_string):
        for command in command_string:
            command_args = command.split()
            if command_args[0] == MOVE:
                move_distance = command_args[1]
                try:
                    val = float(move_distance)
                    self.__move(val)
                except ValueError:
                    print('Wrong move distance - {0}!'.format(move_distance))
            elif command_args[0] == TURN:
                turn_angle = command_args[1]
                try:
                    val = int(turn_angle)
                    self.__turn(val)
                except ValueError:
                    print('Wrong turn angle - {0}!'.format(turn_angle))
            elif command_args[0] == SET:
                state = command_args[1]
                if state != WATER and state != BRUSH and state != SOAP:
                    print('Wrong state - {0}!'.format(state))
                else:
                    self.__set(state)
            elif command_args[0] == START:
                self.__start()
            elif command_args[0] == START:
                self.__stop()
            else:
                print('Unknown command - {0}!'.format(command))


robot = RobotJanitor()
robot.execute('move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop')
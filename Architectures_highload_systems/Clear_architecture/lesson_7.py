from math import cos, sin, radians

WATER = 'water'
SOAP = 'soap'
BRUSH = 'brush'

MOVE = 'move'
TURN = 'turn'
SET = 'set'
START = 'start'
STOP = 'stop'


class MoveEngine:
    def __init__(self, pos_x: float, pos_y: float, angle: int):
        self.PosX = pos_x
        self.PosY = pos_y
        self.Angle = angle

    def move(self, distance):
        self.PosX += distance * cos(radians(self.Angle))
        self.PosY -= distance * sin(radians(self.Angle))
        print('Position: {0}, {1}'.format(self.PosX, self.PosY))

    def turn(self, turn_angle):
        self.Angle += turn_angle
        print('Angle: {0}'.format(self.Angle))


class RobotJanitor:
    def __init__(self, coords: MoveEngine, state):
        self.Coords = coords
        self.State = state

    def set_state(self, state):
        print('State: {0}'.format(state))
        self.State = state

    def start(self):
        print('Start with {0}'.format(self.State))

    def stop(self):
        print('Stop')


class Player:
    def __init__(self, robot: RobotJanitor, command_str):
        self.Robot = robot
        self.make(command_str)

    def make(self, command_string):
        for command in command_string:
            command_args = command.split()
            if command_args[0] == MOVE:
                move_distance = command_args[1]
                try:
                    val = float(move_distance)
                    self.Robot.Coords.move(val)
                except ValueError:
                    print('Wrong move distance - {0}!'.format(move_distance))
            elif command_args[0] == TURN:
                turn_angle = command_args[1]
                try:
                    val = int(turn_angle)
                    self.Robot.Coords.turn(val)
                except ValueError:
                    print('Wrong turn angle - {0}!'.format(turn_angle))
            elif command_args[0] == SET:
                state = command_args[1]
                if state != WATER and state != BRUSH and state != SOAP:
                    print('Wrong state - {0}!'.format(state))
                else:
                    self.Robot.set_state(state)
            elif command_args[0] == START:
                self.Robot.start()
            elif command_args[0] == STOP:
                self.Robot.stop()
            else:
                print('Unknown command - {0}!'.format(command))


if __name__ == "__main__":
    Player(
        robot=RobotJanitor(
            coords=MoveEngine(
                pos_x=0.0,
                pos_y=0.0,
                angle=0
            ),
            state=WATER
        ),
        command_str=('move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop')
    )

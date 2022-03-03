import on_server_learning.Architectures_highload_systems.Clear_architecture.lesson_5_pure_robot as api


class RobotJanitor:
    def __init__(self, pos_x=0.0, pos_y=0.0, angle=0, state=api.WATER):
        self.state = api.RobotState(pos_x, pos_y, angle, state)
        self.exec_func = api.transfer_to_cleaner

    def make(self, code):
        for command in code:
            cmd = command.split(' ')
            if cmd[0] == 'move':
                state = api.move(self.exec_func, int(cmd[1]), self.state)
            elif cmd[0] == 'turn':
                state = api.turn(self.exec_func, int(cmd[1]), self.state)
            elif cmd[0] == 'set':
                state = api.set_state(self.exec_func, cmd[1], self.state)
            elif cmd[0] == 'start':
                state = api.start(self.exec_func, self.state)
            elif cmd[0] == 'stop':
                state = api.stop(self.exec_func, self.state)
        return state

# rbt = RobotJanitor()
# rbt.make(('move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop'))

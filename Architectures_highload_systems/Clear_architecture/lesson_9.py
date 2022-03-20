import on_server_learning.Architectures_highload_systems.Clear_architecture.lesson_5_pure_robot as pr


def get_maker(transfer=pr.transfer_to_cleaner):
    def maker(code, state):
        return execute(transfer, code, state)
    return maker


def execute(transfer, command, state):
    cmd = command.split(' ')
    if cmd[0] == 'move':
        state = pr.move(transfer, int(cmd[1]), state)
    elif cmd[0] == 'turn':
        state = pr.turn(transfer, int(cmd[1]), state)
    elif cmd[0] == 'set':
        state = pr.set_state(transfer, cmd[1], state)
    elif cmd[0] == 'start':
        state = pr.start(transfer, state)
    elif cmd[0] == 'stop':
        state = pr.stop(transfer, state)
    return state


class RobotApi:
    def setup(self, maker):
        self.maker = maker
        self.cleaner_state = None

    def __call__(self, command):
        if not self.cleaner_state:
            self.cleaner_state = pr.RobotState(0.0, 0.0, 0, pr.WATER)
        for cmd in command:
            self.cleaner_state = self.maker(cmd, self.cleaner_state)
        return self.cleaner_state


if __name__ == "__main__":
    api = RobotApi()
    api.setup(get_maker(pr.transfer_to_cleaner))

api(('move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop'))

import on_server_learning.Architectures_highload_systems.Clear_architecture.lesson_5_pure_robot as pr


def execute(command):
    state = pr.RobotState(0.0, 0.0, 0, pr.WATER)
    param = 0.0
    for val in command.split(' '):
        if val == 'move':
            state = pr.move(pr.transfer_to_cleaner, float(param), state)
        elif val == 'turn':
            state = pr.turn(pr.transfer_to_cleaner, int(param), state)
        elif val == 'set':
            state = pr.set_state(pr.transfer_to_cleaner, param, state)
        elif val == 'start':
            state = pr.start(pr.transfer_to_cleaner, state)
        elif val == 'stop':
            state = pr.stop(pr.transfer_to_cleaner, state)
        else:
            param = val
    return state


def translate(command):
    str_array = []
    for cmd in command:
        val = cmd.split(' ')
        if len(val) > 1:
            str_array.append(val[1])
        str_array.append(val[0])
    return " ".join(str_array)


execute(translate(('move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop')))
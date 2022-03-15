import on_server_learning.Architectures_highload_systems.Clear_architecture.lesson_5_pure_robot as pr


def execute_command(cmd, robot_state, cmd_param):
    if cmd == 'move':
        return pr.move(pr.transfer_to_cleaner, int(cmd_param[0]), robot_state)
    if cmd == 'stop':
        return pr.stop(pr.transfer_to_cleaner, robot_state)
    if cmd == 'turn':
        return pr.turn(pr.transfer_to_cleaner, int(cmd_param[0]), robot_state)
    if cmd == 'start':
        return pr.start(pr.transfer_to_cleaner, robot_state)
    if cmd == 'set':
        return pr.set_state(pr.transfer_to_cleaner, cmd_param, robot_state)
    print('Wrong command: {0}'.format(cmd))
    return robot_state


def execute(cmd_array):
    state = pr.RobotState(0.0, 0.0, 0, pr.WATER)
    for command in cmd_array:
        command_args = command.split()
        state = execute_command(command_args[0], state, command_args[1:])


execute(('move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop'))
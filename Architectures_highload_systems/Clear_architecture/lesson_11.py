import on_server_learning.Architectures_highload_systems.Clear_architecture.lesson_5_pure_robot as pr


def monad_move(arg):
    def execute(state):
        return pr.move(pr.transfer_to_cleaner, arg, state)
    return execute


def monad_turn(arg):
    def execute(state):
        return pr.turn(pr.transfer_to_cleaner, arg, state)
    return execute


def monad_set_state(arg):
    def execute(state):
        return pr.set_state(pr.transfer_to_cleaner, arg, state)
    return execute


def monad_start():
    def execute(state):
        return pr.start(pr.transfer_to_cleaner, state)
    return execute


def monad_stop():
    def execute(state):
        return pr.stop(pr.transfer_to_cleaner, state)
    return execute


class Monad_PureRobot:
    def __init__(self):
        self.state = pr.RobotState(0.0, 0.0, 0, pr.WATER)

    def bind(self, command):
        self.state = command(self.state)
        return self

    def get_state(self):
        return self.state


if __name__ == "__main__":
    print((
        Monad_PureRobot()
        .bind(monad_move(100))
        .bind(monad_turn(-90))
        .bind(monad_set_state("soap"))
        .bind(monad_start())
        .bind(monad_move(50))
        .bind(monad_stop())
        .get_state()
    ))

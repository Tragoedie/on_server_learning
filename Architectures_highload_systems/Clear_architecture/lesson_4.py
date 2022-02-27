from on_server_learning.Architectures_highload_systems.Clear_architecture.lesson_4_robot_janitor import RobotJanitor

robot = RobotJanitor()
robot.execute('move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop')

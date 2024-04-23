import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class GroupController(Node):
    def __init__(self):
        super().__init__('ti_rlsk_group_controller')
        # Crear un publisher por cada robot
        self.robot1_cmd_vel_publisher = self.create_publisher(Twist, '/robot1/cmd_vel', 10)
        # Repetir para robot2, robot3, robot4...

    def send_group_command(self, linear, angular):
        # Crea el mensaje Twist
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = linear
        cmd_vel_msg.angular.z = angular
        # Publicar comandos para cada robot
        self.robot1_cmd_vel_publisher.publish(cmd_vel_msg)
        # Repetir para robot2, robot3, robot4...

def main(args=None):
    rclpy.init(args=args)
    group_controller = GroupController()
    rclpy.spin(group_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class IndividualController(Node):
    def __init__(self):
        super().__init__('ti_rlsk_individual_controller')
        self.publisher_ = self.create_publisher(Odometry, '/ti_rlsk_robot_state', 10)
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.velocity_callback,
            10)
        self.subscription  # prevent unused variable warning

    def velocity_callback(self, msg):
        # Aquí enviarías el comando de velocidad al robot
        pass

    def publish_state(self):
        # Aquí publicarías el estado del robot
        msg = Odometry()
        # Rellena el mensaje con el estado del robot
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    individual_controller = IndividualController()
    rclpy.spin(individual_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

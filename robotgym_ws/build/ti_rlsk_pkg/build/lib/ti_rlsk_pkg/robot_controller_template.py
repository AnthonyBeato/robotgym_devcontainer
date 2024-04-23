import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        # Crear un publicador para enviar comandos de movimiento
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Configurar un temporizador para llamar a timer_callback cada 0.1 segundos
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        # Crear un mensaje Twist para mover el robot
        twist = Twist()
        twist.linear.x = 0.5  # Mover hacia adelante
        twist.angular.z = 0.5  # Girar ligeramente

        # Publicar el comando de movimiento
        self.publisher_.publish(twist)
        self.get_logger().info('Publicando comando de movimiento')

def main(args=None):
    rclpy.init(args=args)
    robot_controller = RobotController()
    rclpy.spin(robot_controller)
    # Destrucción del nodo explícita
    robot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

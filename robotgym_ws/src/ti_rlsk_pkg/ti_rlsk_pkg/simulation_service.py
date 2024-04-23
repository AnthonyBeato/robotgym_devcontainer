import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class SimulationServiceNode(Node):
    def __init__(self):
        super().__init__('simulation_service_node')
        self.srv = self.create_service(Empty, 'reset_simulation', self.reset_simulation_callback)

    def reset_simulation_callback(self, request, response):
        # Código para reiniciar la simulación
        # Por ejemplo, si estás usando Gazebo, podrías llamar a un servicio de Gazebo para resetear la simulación
        self.get_logger().info('Reiniciando la simulación...')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SimulationServiceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

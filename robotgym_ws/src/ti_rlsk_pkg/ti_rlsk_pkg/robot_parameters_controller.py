import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult

class RobotControllerNode(Node):
    def __init__(self):
        super().__init__('robot_controller')
        # Define los parámetros con valores por defecto
        self.declare_parameter('max_speed', 1.0)
        self.declare_parameter('use_sim_time', True)

        # Utiliza los parámetros en el nodo
        self.max_speed = self.get_parameter('max_speed').get_parameter_value().double_value
        self.use_sim_time = self.get_parameter('use_sim_time').get_parameter_value().bool_value

        # Registrar un callback para cambios de parámetros
        self.add_on_set_parameters_callback(self.parameters_callback)

    def parameters_callback(self, params):
        for param in params:
            if param.name == 'max_speed' and param.type_ == param.Type.DOUBLE:
                self.max_speed = param.value
                self.get_logger().info(f'Nuevo max_speed: {self.max_speed}')
            elif param.name == 'use_sim_time' and param.type_ == param.Type.BOOL:
                self.use_sim_time = param.value
                self.get_logger().info(f'Nuevo use_sim_time: {self.use_sim_time}')
        return SetParametersResult(successful=True)

def main(args=None):
    rclpy.init(args=args)
    node = RobotControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

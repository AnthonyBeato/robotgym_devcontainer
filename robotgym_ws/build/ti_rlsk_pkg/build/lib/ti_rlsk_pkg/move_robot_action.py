import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from action_msgs.msg import GoalStatus
from geometry_msgs.msg import Pose
from nav2_msgs.action import NavigateToPose
import time  

class MoveRobotActionServer(Node):

    def __init__(self):
        super().__init__('move_robot_action_server')
        self._action_server = ActionServer(
            self,
            NavigateToPose,
            'navigate_to_pose',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Moviendo el robot hacia una nueva pose...')
        feedback_msg = NavigateToPose.Feedback()

        # Aquí iría la lógica para mover el robot.
        # Puedes publicar en el topic /cmd_vel y monitorear la posición del robot para saber cuándo ha llegado.
        
        # Simulamos que el robot está en movimiento
        for i in range(1, 11):
            feedback_msg.current_pose.pose.position.x = goal_handle.request.pose.pose.position.x * i / 10.0
            feedback_msg.current_pose.pose.position.y = goal_handle.request.pose.pose.position.y * i / 10.0
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.5)  # Usamos time.sleep para pausar la ejecución temporalmente
        
        goal_handle.succeed()

        result = NavigateToPose.Result()
        return result

def main(args=None):
    rclpy.init(args=args)
    action_server = MoveRobotActionServer()
    rclpy.spin(action_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

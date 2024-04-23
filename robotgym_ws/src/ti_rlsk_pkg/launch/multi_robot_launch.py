from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution

def generate_launch_description():
    # Define argumentos que se pueden pasar al lanzador (launch system)
    declare_robot_name_argument = DeclareLaunchArgument(
        'robot_name',
        default_value=TextSubstitution(text='robot'),
        description='Nombre del robot para las instancias múltiples')

    declare_robot_namespace_argument = DeclareLaunchArgument(
        'namespace',
        default_value=LaunchConfiguration('robot_name'),
        description='Espacio de nombres ROS para esta instancia del robot')

    declare_robot_urdf_argument = DeclareLaunchArgument(
        'urdf_file',
        description='Archivo URDF/Xacro para la descripción del robot')

    # Nodo para el estado del robot
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=LaunchConfiguration('namespace'),
        output='screen',
        parameters=[{'robot_description': LaunchConfiguration('urdf_file')}]
    )

    # Nodo para la simulación en Gazebo
    gazebo_node = Node(
        package='gazebo_ros',
        executable='gazebo',
        arguments=['-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    # Crear y devolver la descripción de lanzamiento
    return LaunchDescription([
        declare_robot_name_argument,
        declare_robot_namespace_argument,
        declare_robot_urdf_argument,
        robot_state_publisher_node,
        gazebo_node
    ])

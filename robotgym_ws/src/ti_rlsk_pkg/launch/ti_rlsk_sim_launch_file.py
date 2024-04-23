from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
import os
import xacro

def generate_launch_description():
# Especificar el nombre del paquete y el path al xacro file
    pkg_name = 'ti_rlsk_pkg'
    urdf_file_path = os.path.join(get_package_share_directory(pkg_name), 'urdf', 'ti_rlsk_robot.urdf.xacro')
    robot_description_raw = xacro.process_file(urdf_file_path).toxml()

    declare_namespace_argument = DeclareLaunchArgument(
        'namespace',
        default_value='ti_rlsk',
        description='Namespace del robot')

    # Configrar el nodo
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw,
                     'use_sim_time': True}] 
    )

    node_joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen',
        name='joint_state_publisher_gui'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
    )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py', arguments=['-topic', 'robot_description', '-entity', 'ti_rlsk'], output='screen')

    #Correr el nodo
    return LaunchDescription([
        declare_namespace_argument,
        gazebo,
        node_robot_state_publisher,
        node_joint_state_publisher_gui,
        spawn_entity
    ])

from setuptools import find_packages, setup
import os

package_name = 'ti_rlsk_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/ti_rlsk_sim_launch_file.py']),
        ('share/' + package_name + '/urdf', [os.path.join('urdf', 'ti_rlsk_robot.urdf.xacro')]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Anthony Beato',
    maintainer_email='axba0001@ce.pucmm.edu.do',
    description='Paquete para el robot TI-RLSK-MAX con Python',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ti_rlsk_node = ti_rlsk_pkg.ti_rlsk_node:main',
            'move_robot_action_server = ti_rlsk_pkg.move_robot_action:main',
            'robot_controller_template = ti_rlsk_pkg.robot_controller_template:main'
        ],
    },
)

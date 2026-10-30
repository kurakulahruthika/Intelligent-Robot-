import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_mm_desc = get_package_share_directory('mm_description')
    urdf_file = os.path.join(pkg_mm_desc, 'urdf', 'mm_robot.urdf')
    
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        # Robot State Publisher node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),
        # Spawn robot entity in Gazebo Harmonic
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-name', 'mm_robot',
                '-file', urdf_file,
                '-z', '0.05'
            ],
            output='screen'
        ),
        # Clock and Sensor Topic Bridge
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
                '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
                '/camera/image_raw@sensor_msgs/msg/Image[gz.msgs.Image'
            ],
            output='screen'
        )
    ])
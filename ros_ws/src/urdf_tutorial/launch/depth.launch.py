import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    package_name = "urdf_tutorial"

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory(package_name), "launch", "robot_6.launch.py")]
        ),
        launch_arguments={"use_sim_time": "true"}.items(),
    )

    # Include the Gazebo launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py")]
        ),
    )

    # Spawn the first robot
    spawn_entity_1 = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "robot_description",
            "-entity", "robot1",
            "-x", "0", "-y", "0", "-z", "0"
        ],
        output="screen",
    )

    # Spawn the second robot at a different location
    spawn_entity_2 = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "robot_description",
            "-entity", "robot2",
            "-x", "2", "-y", "2", "-z", "0"
        ],
        output="screen",
    )

    # Launch them all!
    return LaunchDescription(
        [
            rsp,
            gazebo,
            spawn_entity_1,
            spawn_entity_2,
        ]
    )


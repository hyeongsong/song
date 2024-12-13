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
            [os.path.join(get_package_share_directory(package_name), "launch", "robot_4.launch.py")]
        ),
        launch_arguments={"use_sim_time": "true"}.items(),
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py")]
        ),
    )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "robot_description",  # 로봇 모델 데이터 (URDF/Xacro)
            "-entity", "with_robot",       # 로봇 이름
            "-x", "0.0",                   # 초기 X 좌표
            "-y", "8.0",                   # 초기 Y 좌표
            "-z", "0.5",                   # 초기 Z 좌표
            "-R", "0.0",                   # 초기 Roll 값
            "-P", "0.0",                   # 초기 Pitch 값
            "-Y", "1.57"                   # 초기 Yaw 값 (라디안)
        ],
        output="screen",
    )
    # Launch them all!
    return LaunchDescription(
        [
            rsp,
            gazebo,
            spawn_entity,
        ]
    )
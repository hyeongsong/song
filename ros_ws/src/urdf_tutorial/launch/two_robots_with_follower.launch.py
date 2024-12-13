from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # 첫 번째 로봇의 teleop_twist_keyboard
    robot1_teleop = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='robot1_teleop',
        namespace='robot1',
        remappings=[('/cmd_vel', '/robot1/cmd_vel')]
    )

    # 두 번째 로봇의 follower 노드
    robot2_follower = Node(
        package='urdf_tutorial',  # follower 노드가 포함된 패키지
        executable='robot_follower',
        name='robot2_follower',
        namespace='robot2'
    )

    return LaunchDescription([
        robot1_teleop,
        robot2_follower,
    ])


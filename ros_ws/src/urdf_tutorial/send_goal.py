import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class SendGoal(Node):
    def __init__(self):
        super().__init__('send_goal')
        self.publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.timer = self.create_timer(2.0, self.publish_goal)

    def publish_goal(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.header.stamp = self.get_clock().now().to_msg()

        goal.pose.position.x = 2.0  # 목표 X 좌표
        goal.pose.position.y = 3.0  # 목표 Y 좌표
        goal.pose.orientation.w = 1.0  # 방향

        self.publisher.publish(goal)
        self.get_logger().info('Goal Published!')

def main(args=None):
    rclpy.init(args=args)
    node = SendGoal()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

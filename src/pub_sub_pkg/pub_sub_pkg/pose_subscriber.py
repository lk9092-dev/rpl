import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class pose_subscriber(Node):

    def __init__(self):
        super().__init__("my_subscriber_node")
        self.pose_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10)
        self.get_logger().info("pose subscriber node is created")

    def pose_callback(self, msg):
        self.get_logger().info(
            f"turle pose-x:{msg.x},pose-y:{msg.y}, theta:{msg.theta}")


def main(args=None):
    rclpy.init(args=args)
    my_Node = pose_subscriber()
    rclpy.spin(my_Node)
    my_Node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

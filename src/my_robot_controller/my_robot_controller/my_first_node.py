import rclpy
from rclpy.node import Node


class mynode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("hello ros2")


def main(args=None):
    rclpy.init(args=args)
    node=mynode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class my_node(Node):

    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        timer_period=0.1
        self.timer=self.create_timer(timer_period, self.send_velocity)
        self.get_logger().info("aamai circle is started")

    def send_velocity(self):
        msg=Twist()
        msg.linear.x=2.5
        msg.angular.z=1.0
        self.cmd_vel_pub.publish(msg)


        


def main(args=None):
    rclpy.init(args=args)
    my_Node=my_node()
    rclpy.spin(my_Node)
    my_Node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

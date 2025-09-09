import rclpy
import fromrclpy.node import node

class mynode(node):
        def _init_(self):
            super()._init_("first_node")
def main(args=None):
    rclpy.init(args=args)

    rclpy.shutdown()
if_name_=='_main_':
    main()

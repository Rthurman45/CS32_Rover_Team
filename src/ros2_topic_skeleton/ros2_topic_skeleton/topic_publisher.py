import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TopicPublisher(Node):

    def __init__(self):
        super().__init__('topic_publisher')

        self.publisher1 = self.create_publisher(
            String,
            'temp_topic_1',
            10
        )
        self.publisher2 = self.create_publisher(
            String,
            'temp_topic_2',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_messages)

        self.get_logger().info('Created topics:')
        self.get_logger().info('/temp_topic_1')
        self.get_logger().info('/temp_topic_2')

    def publish_messages(self):
        msg1 = String()
        msg1.data = 'Hello from topic 1'

        msg2 = String()
        msg2.data = 'Hello from topic 2'

        self.publisher1.publish(msg1)
        self.publisher2.publish(msg2)


def main(args=None):
    rclpy.init(args=args)

    node = TopicPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
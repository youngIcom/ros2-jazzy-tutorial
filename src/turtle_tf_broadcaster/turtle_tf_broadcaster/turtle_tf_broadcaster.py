#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose


class TurtleTfBroadcaster(Node):
    def __init__(self, turtle_name):
        super().__init__('turtle_tf_broadcaster_' + turtle_name)
        self.turtle_name = turtle_name
        
        # QoS profile untuk turtlesim
        qos_profile = QoSProfile(depth=10)
        
        self.tf_broadcaster = TransformBroadcaster(self)
        
        self.subscription = self.create_subscription(
            Pose,
            f'/{turtle_name}/pose',
            self.turtle_pose_callback,
            qos_profile)
        self.subscription  # prevent unused variable warning

    def turtle_pose_callback(self, msg):
        t = TransformStamped()
        
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'world'
        t.child_frame_id = self.turtle_name
        
        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0
        
        # Konversi sudut dari turtlesim (berlawanan jarum jam) ke quaternion
        q = self.euler_to_quaternion(0, 0, msg.theta)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        
        self.tf_broadcaster.sendTransform(t)
    
    def euler_to_quaternion(self, roll, pitch, yaw):
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)
        
        w = cy * cp * cr + sy * sp * sr
        x = cy * cp * sr - sy * sp * cr
        y = sy * cp * sr + cy * sp * cr
        z = sy * cp * cr - cy * sp * sr
        
        return (x, y, z, w)


def main(args=None):
    rclpy.init(args=args)
    
    broadcaster = TurtleTfBroadcaster('turtle1')
    rclpy.spin(broadcaster)
    
    broadcaster.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

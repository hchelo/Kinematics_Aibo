import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kubu/ROS2/ros2_ws/src/srvcli_matrix/install/srvcli_matrix'

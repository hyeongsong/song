import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yoohyeongsong/Workspace/ros_ws/install/urdf_tutorial'

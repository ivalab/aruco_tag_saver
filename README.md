# aruco_tag_saver
save ground truth with aruco tag (kinect, meta ports)

## USAGE

### Looking for a ROS version?
please check [aruco_tag_saver_ros](https://github.com/ivalab/aruco_tag_saver_ros)

### Aruco
1. see `/tags`, `466.jpg` is for reference on the table
2. see `/tags/DICT_6X6_250`, `3`, `4`, `5` are for end-effector, as shown in [this](https://github.com/ivalab/aruco_tag_saver/blob/master/imgs/pic_0001.png)
3. see `/tags/DICT_5X5_250`, `5x5_1000-7_8_9_10` are for target object

### using tcp/ip
1. run script
```
git clone https://github.com/ivalab/aruco_tag_saver.git
cd aruco_tag_saver
python camera_demo_arucoTag_5X5_250.py.py
```
2. default port is `2328`

### using Kinect
1. install [libfreenect](https://naman5.wordpress.com/2014/06/24/experimenting-with-kinect-using-opencv-python-and-open-kinect-libfreenect/) for kinect (warning: never do upgrade) 
2. [calibrate](http://rgbdemo.org/index.php/Documentation/KinectCalibrationTheory) kinect
3. run script
```
git clone https://github.com/ivalab/aruco_tag_saver.git
cd aruco_tag_saver
python camera_demo_arucoTag_kinect.py
```
4. press `s` to save rgb/depth/rawDepth images
5. press `t` or `g` to tilt up or down kinect
6. change the parameters:
```
# CHANGE-ABLE PARAMETERS
OBJECT_TYPE = "scoop"
CAM_POSE = 0
OBJ_POSE = 0
START_COUNT = 0

tmpPathGT_pose = './data/graspPositions.txt'
tmpPathGT_ar = './data/arucoPositions.txt'
tmpPathGT = './data/graspPoseLabels.txt'
```

### change tilt range for kinect
1. `tilt.c`:
```
#define MAX_TILT_ANGLE 91
#define MIN_TILT_ANGLE (-91)
```

2. `glview.c` (optional, only if you want to use this example):
```
	if (key == 'w') {
		freenect_angle++;
		if (freenect_angle > 30) {
			freenect_angle = 30;
		}
		tilt_changed++;
	}
...
	if (key == 'x') {
		freenect_angle--;
		if (freenect_angle < -30) {
			freenect_angle = -30;
		}
		tilt_changed++;
	}
```
3. remove `libfreenect.so` and `libfreenect_sync.so` under `/usr/lib/x86_64-linux-gnu/`
4. make and make install `libfreenect.so` and `libfreenect_sync.so` and load libraries
5. run Cython setup.py to generate module and link to new `.so`


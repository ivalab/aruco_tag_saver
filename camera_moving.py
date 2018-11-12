import freenect
import cv2
import numpy as np
import time
# function to get RGB image from kinect
def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array


# function to get depth image from kinect
def get_depth():
    array_raw, _ = freenect.sync_get_depth()
    array = array_raw.astype(np.uint8)
    return array, array_raw



TILT_MAX = 90
TILT_STEP = 5
TILT_MIN = -90
TILT = 0

# reset the camera tilt
ctx = freenect.init()
dev = freenect.open_device(ctx, freenect.num_devices(ctx) - 1)
freenect.set_tilt_degs(dev, TILT)
# python wrapper dont register for video/depth so pointer needs to be shutdown before inquiring video
freenect.shutdown(ctx)

while 1:
    # get a frame from RGB camera
    frame_current = get_video()
    # get a frame from depth sensor
    depth, depth_raw = get_depth()
    # display RGB image
    cv2.imshow('RGB image', frame_current)
    # display depth image
    cv2.imshow('Depth image', depth)


    # quit program when 'esc' key is pressed
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    elif k == ord('t'):
        # conflit registeration between video and tilt, annoying
        freenect.sync_stop()
        time.sleep(0.1)

        ctx = freenect.init()
        dev = freenect.open_device(ctx, freenect.num_devices(ctx) - 1)

        TILT = min(TILT + TILT_STEP, TILT_MAX)
        print "Setting TILT: ", TILT
        freenect.set_tilt_degs(dev, TILT)

        freenect.shutdown(ctx)
        time.sleep(0.1)


    elif k == ord('g'):
        # conflit registeration between video and tilt, annoying
        freenect.sync_stop()
        time.sleep(0.1)

        ctx = freenect.init()
        dev = freenect.open_device(ctx, freenect.num_devices(ctx) - 1)

        TILT = max(TILT - TILT_STEP, TILT_MIN)
        print "Setting TILT: ", TILT
        freenect.set_tilt_degs(dev, TILT)

        freenect.shutdown(ctx)
        time.sleep(0.1)

    elif k == ord('i'):
        # conflit registeration between video and tilt, annoying
        angle = input("What is your desired angle? ")
        print "Your angle is: ", angle
        type(angle)

        freenect.sync_stop()
        time.sleep(0.1)

        ctx = freenect.init()
        dev = freenect.open_device(ctx, freenect.num_devices(ctx) - 1)

        TILT = max(angle, TILT_MIN)
        print "Setting TILT: ", TILT
        freenect.set_tilt_degs(dev, TILT)

        freenect.shutdown(ctx)
        time.sleep(0.1)

cv2.destroyAllWindows()
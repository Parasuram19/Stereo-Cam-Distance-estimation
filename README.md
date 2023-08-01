**IMPORTANT:** If you are using a different version of OpenCV. The output from cv2.findContours may have changed. Go to `targeting_tools.py` lines 325-237 (the line the error will say) and change `frame3,contours,hierarchy` to `contours,hierarchy` (or the other way around).

## Single Camera Test

You can use `x_test_single_camera.py` if you want to test a single camera to make sure it is working and you know the correct address. It does everything the same as `triangulation.py` except not the triangulation and only on one camera.

## Other Testing

The file `x_testing.py` and other `x_` prefixed files are different tests I'm trying. They may or may not work.






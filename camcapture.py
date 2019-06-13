# purpose:
# Capture the video from any Webcam and then save to file under Windows Platform.
# date: 2019/06/13 23:35

import sys
import platform
import cv2
import datetime

if len(sys.argv) > 1:
    if sys.argv[1] == "--help":
        print("Usage: \n\t{0} [camera output size] e.g {1} 1280x720".format(sys.argv[0], sys.argv[0]))
        sys.exit(0)
    width, height = int(str(sys.argv[1]).split("x")[0]), int(str(sys.argv[1]).split("x")[1])
else:
    width, height = 640, 480


def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    if 'Windows' not in platform.system():
        print("This app does NOT support non-windows platform.")
        sys.exit(1)
    encode = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("camcapvid_" + f"{datetime.datetime.now():%Y%m%d_%H%M%S}" + ".avi" , encode, 20.0, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 0)
            out.write(frame)
            cv2.imshow("Press 'q' to exit and export the output.avi video file in current folder.", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

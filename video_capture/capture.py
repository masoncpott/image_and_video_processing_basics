import cv2, time

video = cv2.VideoCapture(0)

num_of_frames = 1

while True:
    num_of_frames = num_of_frames + 1
    check, frame = video.read()

    print(check)
    print(frame)

    cv2.imshow("capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print("NUMBER OF FRAMES: ", num_of_frames)
video.release()
cv2.destroyAllWindows()
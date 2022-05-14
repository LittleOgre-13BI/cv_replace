import cv2

cap = cv2.VideoCapture("./Videos/com.mp4")
size = (640, 480)
fps = 30
video_writer = cv2.VideoWriter("./Videos/resized.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

while True:
    success, frame = cap.read()
    if success:
        img = cv2.resize(frame, size)
        video_writer.write(img)
    else:
        print('break')
        break

video_writer.release()
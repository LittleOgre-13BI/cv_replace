import cv2


cap = cv2.VideoCapture('./Videos/resized.mp4')
green_lower = (35, 43, 46)
green_upper = (77, 255, 255)
bgr = cv2.imread('./Images/1.jpg')
size = (640, 480)
fps = 30
video_writer = cv2.VideoWriter("./Videos/rslt.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

while True:
    success, img = cap.read()
    fg_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(fg_hsv, green_lower, green_upper)
    fg_mask = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(img, img, mask=fg_mask)
    bg = cv2.bitwise_and(bgr, bgr, mask=mask)
    rslt = cv2.add(fg, bg)
    cv2.imshow("Result", rslt)
    video_writer.write(rslt)
    key = cv2.waitKey(10)
    if key == 27:  # exit on ESC
        break

video_writer.release()
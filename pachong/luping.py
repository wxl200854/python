from PIL import ImageGrab
import numpy as np
import cv2

screen = ImageGrab.grab()
length, width = screen.size
video_decode_style = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('a.avi', video_decode_style, 24, (length, width))
while True:
    im = ImageGrab.grab()
    imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    video.write(imm)
    if cv2.waitKey(100) & 0XFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
import numpy as np
import cv2

def string_to_video(message, stringSpeed):

   # Start params
    height = 100
    width = 100
    duration = 3
    fps = 30

   # Set the parameters of stream
    out = cv2.VideoWriter("result.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Creating frame with black background
    frame = np.zeros((height, width, 3),dtype=np.uint8)

    # Start coordinates of main ticker
    x = width // 2
    y = height // 2

    # Add text to each frame
    for t in range(duration * fps):

        # Frame clear before add new info
        frame.fill(0)

        # Update x coordinate
        x -= stringSpeed

        # Put text to frame with different fonts
        cv2.putText(frame, message, (x-50, y-30), cv2.AKAZE_DESCRIPTOR_KAZE_UPRIGHT, 0.7, (34,139,34)) # Top ticker
        cv2.putText(frame, message, (x, y), cv2.BORDER_REFLECT, 0.7, (255,0,0)) # Main ticker
        cv2.putText(frame, message, (x+50, y+30), cv2.QT_STYLE_ITALIC, 0.7, (255, 255, 153)) # Bot ticker

        out.write(frame)

    # Stop write info to stream
    out.release()

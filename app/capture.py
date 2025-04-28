import cv2

def capture_frame(video_path, output_image):
    cap = cv2.VideoCapture(video_path)

    cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
    ret, frame = cap.read()
    captured = False
    
    if ret:
        cv2.imwrite(output_image, frame)
        captured = True
    else:
        captured = False        

    cap.release()
    
    return captured

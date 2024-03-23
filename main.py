import cv2

from utils import detect_gesture, annotate_frame

def main(input_gesture_path, test_video_path, output_video_path):
   
    input_gesture = cv2.imread(input_gesture_path)
    if input_gesture is None:
        raise FileNotFoundError(f"Input gesture image '{input_gesture_path}' not found.")

 
    cap = cv2.VideoCapture(test_video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Test video '{test_video_path}' not found.")

   
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

   
    cv2.namedWindow('Annotated Frame', cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        
        gesture_detected, movement_contour = detect_gesture(input_gesture, frame)

        
        if gesture_detected:
            frame = annotate_frame(frame, movement_contour)

        
        out.write(frame)

        
        cv2.imshow('Annotated Frame', frame)
        
       
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    input_gesture_path = "src\\input_gesture.jpeg"
    test_video_path = "src\\test3.mp4"
    output_video_path = "output_video.avi"
    main(input_gesture_path, test_video_path, output_video_path)

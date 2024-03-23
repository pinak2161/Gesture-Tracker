import cv2
import numpy as np
def detect_gesture(input_gesture, frame):
  
    input_gesture_gray = cv2.cvtColor(input_gesture, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    res = cv2.matchTemplate(frame_gray, input_gesture_gray, cv2.TM_CCOEFF_NORMED)

    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    
    print("Max correlation value:", max_val)

   
    threshold = 0.1  

    
    if max_val > threshold:
       
        top_left = max_loc
        bottom_right = (top_left[0] + input_gesture.shape[1], top_left[1] + input_gesture.shape[0])

        
        movement_contour = np.array([[top_left[0], top_left[1]],
                                     [bottom_right[0], top_left[1]],
                                     [bottom_right[0], bottom_right[1]],
                                     [top_left[0], bottom_right[1]]])

        return True, movement_contour
    else:
        return False, None


def annotate_frame(frame, movement_contour):
    
    annotated_frame = frame.copy()
    cv2.putText(annotated_frame, "DETECTED", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)

    
    if movement_contour is not None:
        x, y, w, h = cv2.boundingRect(movement_contour)
        cv2.rectangle(annotated_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return annotated_frame




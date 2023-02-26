import pyautogui
from imageai.Detection import ObjectDetection
obj_detect = ObjectDetection()
obj_detect.setModelTypeAsYOLOv3()
obj_detect.setModelPath(r"G:/yolov3.pt")
obj_detect.loadModel()
import cv2
cam_feed = cv2.VideoCapture(0)
cam_feed.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
cam_feed.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)
while True:    
    ret, img = cam_feed.read()   
    detections = obj_detect.detectObjectsFromImage(input_image=img, minimum_percentage_probability=70)
    for x in detections:
        print(x['name'], x['percentage_probability'])
        if 'cell phone' in x['name']:
            print('minimizing')
            pyautogui.hotkey('win','m')
                      
    if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1)==27):
        break

cam_feed.release()
cv2.destroyAllWindows()

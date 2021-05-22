'''
To read the camer - Computer Vision
alarm sound package
'''
import cv2
import winsound
'''keeping index as 0 coz one came if multiple camera set as 1'''
camera = cv2.VideoCapture(0)
while camera.isOpened():
    '''
    Camera is reading two variable - retrive and frames
    To know the movement we are creating two frame(knowing difference)
    '''
    ret, frame1 = camera.read()
    ret, frame2 = camera.read()
    difference = cv2.absdiff(frame1, frame2)
    '''converting colour to grey colour and converting gray to blur using blur technique'''
    gray = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    '''
    To get rid of noise around
    after removing making it(necessary object) wider - dilate
    '''
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # threshold values and threshold type
    dilated = cv2.dilate(thresh, None, iterations=3)
    '''contours is box around us'''
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    '''green colour and 2-thickness'''
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    '''ignoring smaller movement and detecting bigger movement'''
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,250,0), 2) # colour of countours and thickness
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
    '''q is is break key like to stop the cam or like emergency wait key'''
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("Parthi's Cam", frame1)
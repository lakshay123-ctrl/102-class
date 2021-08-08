import cv2
import dropbox
import time
import random

start_time = time.time()
def takesnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        image_name = "img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        result = False
    return image_name  
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    print("snapshot taken")   
    

def upload_file(image_name):
    access_Token = 'sl.A2KPDgQ5V7tT14VBGNkjEHD1lHx6DdjKqkSvke7v3Emqs0amki41anvQtm1JyHhZdZqhE195Jdr0T9c0_jw3RGWo1qyhiQWH53ttsleHX5i54YEIvNKEv0AmFqH-92BiU0ft3SVb'
    file = image_name
    file_from = file
    file_to = "/testfolder/"+(image_name)
    dbx = dropbox.Dropbox(access_Token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
    while(True):
      if((time.time()-start_time)>=5):
          name = takesnapshot()
          upload_file(name)
        



main()
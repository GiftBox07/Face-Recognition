import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime


video_capture = cv2.VideoCapture(0)


jobs_image = face_recognition.load_image_file("jobs.jpeg")
jobs_encoding = face_recognition.face_encodings(jobs_image)[0]

musk_image = face_recognition.load_image_file("Elon Musk.jpeg")
musk_encoding = face_recognition.face_encodings(musk_image)[0]

fridmen_image = face_recognition.load_image_file("Lex Fridmen.jpeg")
fridmen_encoding = face_recognition.face_encodings(fridmen_image)[0]

known_face_recognition=[
jobs_encoding,
musk_encoding,
fridmen_encoding,
]

know_faces_names=[
"Steve Jobs",
"Elon Musk",
"Lex Fridmen"
]

students = known_faces_names.copy()

face_loacation = []
face_encodings = []
face_names = []
s=True


now = datetime.now()
current_time = now.striftime("%Y-%m-%d")


f = open(current_date+'.csv','w+',newline = '')
Inwriter = csv.writer(f)

def face_recognition():
    while True:
        _,frame = video_capture.read()
        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgb_small_frame = small_frame[:,:,::-1]
        if s:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_samll_frame,face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                name = ""
                face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_faces_name[best_match_index]

                face_names.append(name)
                if name in known_faces_names:
                    students.remove(name)
                    print(students)
                    current_time = now.striftime("%H-%M-%S")
                    Inwriter.writerow([nmae,current_time])
        cv2.imshow("attendence system",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destoryAIWindows()
    f.close()


from tkinter import *
top = Tk()
top.geometry("300x300")
top.title("Facial Recogniton Attendence System")
top['bg']= 'green'
redbutton = Label(top, text = "Facial Recogniton Attendence System", fg = "red") 
redbutton.place(x=100,y=20) 
redbutton = Button(top, text = "Live Capture",command='face_recognition', fg = "red") 
redbutton.place(x=100,y=50) 
#bluebutton = Button(top, text = "Show Attendance", fg = "blue") 
#bluebutton.place(x=100,y=100) 
top.mainloop()



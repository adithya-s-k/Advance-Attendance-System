from distutils.command.upload import upload
import cv2
import face_recognition as fc 
import numpy as np
import os
import face_recognition
import random

attendance = []
# image = fc.load_image_file("upload_photo/class_2.jpg")

def detect():
    img=os.listdir("upload_photo")[0]
    img="upload_photo\\"+img
    image = fc.load_image_file(str(img))
    image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

    face_locations = fc.face_locations(image)
    print(face_locations)

    for i in range(len(face_locations)):
        image = cv2.rectangle(image,(face_locations[i][3],face_locations[i][0]),(face_locations[i][1],face_locations[i][2]),(255,0,255),2)
        

    cv2.imshow("Class Room" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    face_detect_crop(img)
    for i in os.listdir("new_isolated_faces"):
        last_function("new_isolated_faces/"+i)
# detect("upload_photo\class_1.jpg")

def face_detect_crop(img):
    path = 'new_isolated_faces'
    image = fc.load_image_file(img)
    image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

    face_locations = fc.face_locations(image)
    print(len(face_locations))

    # Crop should be of the form y1:y2,x1:x2
    # converting the coordinates from the face recognition software crop will be of the form
    # [face_locations[0][0]:face_locations[0][2],face_locations[0][3]:face_locations[0][1]]

    for i in range(len(face_locations)):
        crop = image[face_locations[i][0]-40:face_locations[i][2]+20,face_locations[i][3]-20:face_locations[i][1]+20]
        cv2.imwrite(os.path.join(path , str(i+1)+".jpg"), crop)

# face_detect_crop("upload_photo\class_1.jpg")

def face_comparison(img1,img2):
    test_1 = face_recognition.load_image_file(str(img1))
    test_1 = cv2.cvtColor(test_1, cv2.COLOR_BGR2RGB)
    test_2 = face_recognition.load_image_file(str(img2))
    test_2 = cv2.cvtColor(test_2, cv2.COLOR_BGR2RGB)

    # finding face location

    faceLocation_test_1 = face_recognition.face_locations(test_1)[0]
    encode_test_1 = face_recognition.face_encodings(test_1)[0]
    cv2.rectangle(test_1, (faceLocation_test_1[3], faceLocation_test_1[0]), (faceLocation_test_1[1], faceLocation_test_1[2]), (255, 0, 255), 3)


    faceLocation_test_2 = face_recognition.face_locations(test_2)[0]
    encode_test_2 = face_recognition.face_encodings(test_2)[0]
    cv2.rectangle(test_2, (faceLocation_test_2[3], faceLocation_test_2[0]), (faceLocation_test_2[1], faceLocation_test_2[2]), (255, 0, 255), 3)

    results = face_recognition.compare_faces([encode_test_1], encode_test_2)
    
    match = face_recognition.face_distance([encode_test_1], encode_test_2)
    
    print(results)
    print(match)
    cv2.putText(test_1, f'{results}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255), 2 )


def face_comparison_1(img1,img2):
    
    strength = []
    
    test_1 = face_recognition.load_image_file(str(img1))
    test_1 = cv2.cvtColor(test_1, cv2.COLOR_BGR2RGB)
    test_2 = face_recognition.load_image_file(str(img2))
    test_2 = cv2.cvtColor(test_2, cv2.COLOR_BGR2RGB)

    # finding face location

    faceLocation_test_1 = face_recognition.face_locations(test_1)[0]
    encode_test_1 = face_recognition.face_encodings(test_1)[0]
    cv2.rectangle(test_1, (faceLocation_test_1[3], faceLocation_test_1[0]), (faceLocation_test_1[1], faceLocation_test_1[2]), (255, 0, 255), 3)


    faceLocation_test_2 = face_recognition.face_locations(test_2)[0]
    encode_test_2 = face_recognition.face_encodings(test_2)[0]
    cv2.rectangle(test_2, (faceLocation_test_2[3], faceLocation_test_2[0]), (faceLocation_test_2[1], faceLocation_test_2[2]), (255, 0, 255), 3)

    results = face_recognition.compare_faces([encode_test_1], encode_test_2)
    
    match = face_recognition.face_distance([encode_test_1], encode_test_2)
    
    return [results[0],float(match)]
    # face_comparision("a1.jpg","elon_musk.jpg")

def face_comparison_folder(img1):
    dir = str("final")
    for f in os.listdir(dir):
        a = face_comparison_1(img1,dir+"/"+f)
        if a[0] == True:
            attendance.append(f)
            return str(f)
# face_comparison_folder("DataBase_Trial/mark zuckerburg/th.png","final")

def face_comparison_folder_last(img1,folder,path):
    similarity = []
    strength = []
    dir = str(folder)
    for f in os.listdir(dir):
        a = face_comparison_1(img1,dir+"/"+f)
        similarity.append(a[0])
        strength.append(a[1])
    # if sum(strength)/len(strength) < 0.5:
        # for i in similarity:
        #     if i == True:
        #         pass
        #     elif i == False:
        #         print("1 photo doesnt match")
    image = fc.load_image_file(img1)
    image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

    cv2.imwrite(os.path.join(path , str(random.randint(0,100))+".jpg"), image)

def face_last(img1,name,dir):
    for f in os.listdir(dir):
        if str(f) == (str(name)[0:-4:1]):
            
            face_comparison_folder_last(img1,"DataBase_Trial"+"/"+f,"DataBase_Trial"+"/"+f)
    print(attendance)
def last_function(img_final):            
    face_last(img_final,face_comparison_folder(img_final),"DataBase_Trial")



import cv2
import face_recognition
import os
def face_comparison(img1,img2):
    
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
    
    # print(results)
    # print(match)
    
    return results
    # face_comparision("a1.jpg","elon_musk.jpg")

def face_comparison_folder(img1,folder):
    similarity = []
    strength = []
    dir = str(folder)
    for f in os.listdir(dir):
        print(face_comparison(img1,dir+"/"+f))

face_comparison_folder("elon_musk.jpg","DataBase_Trial/elon musk")
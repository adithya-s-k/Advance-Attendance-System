from fileinput import filename
from flask import Flask,render_template,request,redirect,flash
from werkzeug.utils import secure_filename
import os
import cv2
import face_recognition as fc 
import main


app=Flask(__name__)
app.config["UPLOAD_FOLDER"]="DataBase_Trial"#change pah
app.config["UPLOAD_FOLDER_1"]="final"
app.config["UPLOAD_CAPTURE"]="upload_photo"
app.config["MAX_CONTENT_PATH"]=2*1024
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
ALLOWED_EXTENSIONS = {'png', 'jpg'}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/teachers")
def teachers():
    return render_template("teacher.html")

@app.route("/studentupload")
def student_upload():
    return render_template("student_upload.html")

@app.route("/uploadimage",methods=["GET","POST"])
def upload_images():
    if request.method=="POST":
            images_lis=request.files.getlist("images")
            name=request.form.get("student_name")
            if name!="":

                    if len(images_lis)>=3:
                                for images in images_lis:
                                    if allowed_file((images.filename)):
                                        #images.save(os.path.join(app.config["UPLOAD_FOLDER"],images))

                                        folder=os.path.join(app.config['UPLOAD_FOLDER'],request.form.get("student_name").replace(" ","_"))
                                        print(folder)
                                        os.system("mkdir {}".format(folder))
                                        images.save(os.path.join(folder, images.filename))
                                        if images_lis.index(images)==1:
                                            # images.save(os.path.join(app.config["UPLOAD_FOLDER_1"],images.filename))
                                            image = fc.load_image_file(images)
                                            image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

                                            cv2.imwrite(os.path.join(app.config["UPLOAD_FOLDER_1"] , str(name)+".jpg"), image)
                            
                                    else:
                                        return render_template("student_upload_error.html")
                                return render_template("student_upload_success.html")
                    else:
                        return render_template("student_upload_error.html")
            else:
                return render_template("student_upload_error.html")
@app.route("/generate_attendence",methods=["GET","POST"])
def gen_attendence():
    if request.method=="GET":
        
            main.detect()
            post=main.attendance
            return render_template("present_students.html",post=post)    
    
@app.route("/upload_capture",methods=["GET","POST"])
def upload_capture():
    if request.method=="POST":
        image_lis=request.files.getlist("images")

        if image_lis:

            for images in image_lis:
                if allowed_file((images.filename)):
                    

                    images.save(os.path.join(app.config["UPLOAD_CAPTURE"],images.filename))
                else:
                    return render_template("capture_upload_error.html")
                return render_template("capture_upload_success.html")
        else:
            return render_template("capture_upload_error.html")


@app.route("/get_attendence",methods=["GET","POST"])
def get_attendence():
    if request.method=="GET":
        name=request.form.get("name")
        return name

        #finish this part







if __name__=="__main__":
    app.run(debug=True)

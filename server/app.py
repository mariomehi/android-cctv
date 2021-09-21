import  person  
import time
import json
import os
from flask import Flask, render_template, request
#from flask_json import FlaskJSON, JsonError, json_response, as_json
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/mr-rabbit/Documents/progetto/server'

app = Flask(__name__)
#json = FlaskJSON()
app.config['IMAGE_UPLOADS'] = '/home/mr-rabbit/Documents/progetto/server'

@app.route("/",methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        user = str(request.form.get('user'))
        dic = {"email": user, "ip":"192.168.1.1"}
        jstring = json.dumps(dic)
        jfile =  open('data.json','w')
        jfile.write(jstring)
        jfile.close

        

    return render_template('index.html')


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        if  request.files:           
            f = request.files["file"]
            f.save(os.path.join(app.config["IMAGE_UPLOADS"], f.filename))
            if (person.person()):
                time.sleep(120)

        
      
        

    return render_template('upload.html')
    

if __name__ == "__main__":
    app.run(debug=True)

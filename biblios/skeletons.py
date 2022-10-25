try:
    import os
except ImportError as eImp:
    print(f"The following error ocurred: {eImp}")

class Contents():
    def flaskApiContent(self):
        cont_run_app= '''try:
    from app import app
    from gevent.pywsgi import WSGIServer
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

if __name__== "__main__":
    try:
        # -----------------Dev mode-----------------
        app.run(host= "127.0.0.1", port= 5000, debug= True)
        # debug= True for apply changes made into the files without restarting the flask server

        # -----------------Prod mode----------------
        #appServer= WSGIServer(("127.0.0.1", 5000), app)
        #appServer.serve_forever()
    except Exception as eImp:
        print(f"The following import ERROR occurred in {__file__}: {eImp}")
    finally:
        print("Finishing program")'''

        cont_init= '''try:
    from flask import Flask
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

app = Flask(__name__)

from app import routes, admin_routes'''
        
        cont_routes= '''try:
    from app import app
    from flask import request, jsonify, make_response
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

# -------------Endpoints-------------
@app.route("/index", methods= ["GET"])
def index():
    resp_code = 200
    resp_json = {
        "responseCode": resp_code,
        "responseMessage": "Some message"
    }
    resp_json = make_response(jsonify(resp_json), resp_code)
    return resp_json'''

        cont_adminroutes= '''try:
    from app import app
    from flask import request, jsonify, make_response
    from werkzeug.security import generate_password_hash, check_password_hash
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

# ------------------Admin routes------------------

# -------------Endpoints-------------
@app.route("/admin_index", methods= ["GET"])
def admin_index():
    resp_code = 200
    resp_json = {
        "responseCode": resp_code,
        "responseMessage": "Some message"
    }
    resp_json = make_response(jsonify(resp_json), resp_code)
    return resp_json'''

        return [cont_run_app, cont_init, cont_routes, cont_adminroutes]

    def tkContent(self):
        contenido1= '''try:
    from biblios import tk_methods
except Exception as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")
    
if __name__== "__main__":
    try:
        met= tk_methods.tkClass()
        met.GUI()
    except Exception as ex:
        print(f"Ocurrió el ERROR: {ex}")
    except KeyboardInterrupt:
        print("Se presionó Ctrl + C")
    finally:
        print("Finalizando programa")
        '''

        contenido2= '''try:
    import os
    import sys
    import platform
    import tkinter as tk
    from tkinter.constants import CENTER
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

# -----------------Other methods-----------------
class extraMethods():
    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def commandSOShell(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema

# -----------------Tkinter widgets methods-----------------
class tkClass(extraMethods):
    fileIco= "name.ico"
    titleApp= "" # Title in the upper part of the main frame
    labelTitleApp= "" # Title in the label

    # -----------------Main window and their components-----------------
    def GUI(self):
        ven= tk.Tk()
        comando, sis= self.commandSOShell()
        os.system(comando)
        ven.title(self.titleApp)
        ven.columnconfigure(0, weight= 1)
        ven.resizable(width= False, height= False)
        try:
            iconImage= self.resource_path(self.fileIco)
            ven.iconbitmap(iconImage)
        except:
            ven.iconbitmap(self.fileIco)
        screenWidth = ven.winfo_screenwidth()# Ancho del área de visualización
        screenHeight = ven.winfo_screenheight()# Alto del área de visualización
        if sis== "Windows":
            width= 500
            height= 550
        else:
            width= 1000
            height= 1050
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        ven.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")

        #Label title of the application
        titleLabel= tk.Label(ven, fg= "red", text= self.labelTitleApp, font= ("jost", 25))
        titleLabel.place(relx= 0.5, y= 25, anchor= CENTER)

        ven.mainloop()
        '''

        contenido3= '__all__= ["tk_methods"]'

        return [contenido1, contenido2, contenido3]

    def flaskContent(self):
        contRunApp= '''try:
    from app import app
    from gevent.pywsgi import WSGIServer
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

if __name__== "__main__":
    try:
        # -----------------Dev mode-----------------
        app.run(host= "127.0.0.1", port= 5000, debug= True)
        # debug= True for apply changes made into the files without restarting the flask server

        # -----------------Prod mode----------------
        #appServer= WSGIServer(("127.0.0.1", 5000), app)
        #appServer.serve_forever()
    except Exception as eImp:
        print(f"The following import ERROR occurred in {__file__}: {eImp}")
    finally:
        print("Finishing program")'''

        contInit= '''try:
    from flask import Flask
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

app= Flask(__name__)

from app import routes, admin_routes'''
        
        contRoutes= '''try:
    import datetime as dt
    from app import app
    from flask import render_template
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

# -------------Context processor-------------
@app.context_processor
def dateNow():
    return {
        "now": dt.datetime.utcnow()
    }

# -------------Endpoints-------------
@app.route("/")# Welcome HTML template
def index():
    return render_template("welcome.html", pageTitle= "Home")'''

        contAdminRoutes= '''try:
    from flask import render_template
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

# ------------------Admin routes------------------
# Below define your admin routes'''

        contLayoutHtml= '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="{{url_for('static', filename= 'css/bootstrap/css/bootstrap.css')}}" type="text/css" />
	<link rel="stylesheet" href="{{url_for('static', filename= 'css/PerStyles.css')}}" type="text/css" />
    <title>{% block title %}{% endblock %}</title>
    
</head>

<body>
    {% include "includes/navbar.html" %}

    {% if imgback %}
        {% include "includes/backgroundStyle.html" %}
    {% endif %}

    {% block content %}{% endblock %}

    {% include "includes/footers.html" %}
    
</body>
</html>'''

        contFooters= '''<footer class="bg-dark absolute-bottom">
    Platform or project name &copy; Diego Martínez {{now.day}}-{{now.strftime("%B")}}-{{now.year}}
</footer>

<script src="{{url_for('static', filename= 'css/bootstrap/js/bootstrap.js')}}"></script>'''

        return [contRunApp, contInit, contRoutes, contAdminRoutes, contLayoutHtml, contFooters]

class Files(Contents):
    pathToKeep= ""
    projectName= ""

    def flask_api_files(self):
        arrFiles= [("run_app.py", "app"),#Main path
                   ("__init__.py", "routes.py", "admin_routes.py")]# Inside app folder
        arrContent= []
        mainProjectPath= f"{self.pathToKeep}/{self.projectName}"

        arrContent= self.flaskApiContent()

        os.makedirs(mainProjectPath)

        for main_index, direc in enumerate(arrFiles):
            for index, elem in enumerate(direc):
                if main_index == 0:
                    tempPath= f"{mainProjectPath}/{elem}"
                    if ".py" in elem or ".html" in elem:
                        with open(tempPath, "wt", encoding= "utf8") as file:
                            file.write(arrContent[0])
                    else:
                        os.makedirs(tempPath)
                elif main_index == 1:
                    tempPath= f"{mainProjectPath}/app/{elem}"
                    with open(tempPath, "wt", encoding= "utf8") as file:
                        file.write(arrContent[index+1])

    def tk_files(self):
        arrFiles= ["tk_main.py", "tk_methods.py", "__init__.py"]
        arrContent= []
        mainProjectPath= f"{self.pathToKeep}/{self.projectName}"
        libFolder= "biblios"

        arrContent= self.tkContent()

        os.makedirs(f"{mainProjectPath}/{libFolder}")

        for arch in range(len(arrFiles)):
            if arch== 0:
                with open(f"{mainProjectPath}/{arrFiles[arch]}", "wt", encoding="utf8") as file:
                    file.write(arrContent[0])

            else:
                with open(f"{mainProjectPath}/{libFolder}/{arrFiles[arch]}", "wt", encoding= "utf8") as file:
                    if "__init__" in arrFiles[arch]:
                        file.write(arrContent[2])
                    else:
                        file.write(arrContent[1])

    def flask_files(self):
        arrFiles= [("run_app.py", "app"),#Main path
                   ("__init__.py", "routes.py", "admin_routes.py", "templates", "static"),#Inside app folder
                   ("layout.html", "includes"),#Inside templates folder
                   ("navbar.html", "footer.html"),# Inside includes folder
                   ("css", "img")]#Inside static folder
        arrContent= [] #contRunApp, contInit, contRoutes, contLayoutHtml, contFooters
        mainProjectPath= f"{self.pathToKeep}/{self.projectName}"
        cont= 0

        arrContent= self.flaskContent()

        os.makedirs(mainProjectPath)

        for direc in arrFiles:
            for elem in direc:
                if cont== 0:
                    tempPath= f"{mainProjectPath}/{elem}"
                    if ".py" in elem or ".html" in elem:
                        with open(tempPath, "wt", encoding= "utf8") as file:
                            file.write(arrContent[0])
                    else:
                        os.makedirs(tempPath)

                elif cont== 1:
                    tempPath= f"{mainProjectPath}/app/{elem}"
                    if ".py" in elem or ".html" in elem:
                        if arrFiles[1][0]== elem:
                            with open(tempPath, "wt", encoding= "utf8") as file:
                                file.write(arrContent[1])

                        elif arrFiles[1][1]== elem:
                            with open(tempPath, "wt", encoding= "utf8") as file:
                                file.write(arrContent[2])

                        elif arrFiles[1][2]== elem:
                            with open(tempPath, "wt", encoding= "utf8") as file:
                                file.write(arrContent[3])
                    else:
                        os.makedirs(tempPath)

                elif cont== 2:
                    tempPath= f"{mainProjectPath}/app/templates/{elem}"
                    if ".py" in elem or ".html" in elem:
                        with open(tempPath, "wt", encoding= "utf8") as file:
                            file.write(arrContent[4])
                    else:
                        os.makedirs(tempPath)

                elif cont== 3:
                    tempPath= f"{mainProjectPath}/app/templates/includes/{elem}"
                    if arrFiles[3][0]== elem:
                        with open(tempPath, "wt", encoding= "utf8") as file:
                            file.write("{# your navbar code here #}")
                    else:
                        with open(tempPath, "wt", encoding= "utf8") as file:
                            file.write("{# your footer code here #}")
                            file.write(arrContent[5])

                elif cont== 4:
                    tempPath= f"{mainProjectPath}/app/static/{elem}"
                    os.makedirs(tempPath)
            cont+= 1
        tempPath= f"{mainProjectPath}/app/static/css/PerStyles.css"
        with open(tempPath, "wt") as file:
            file.write("/*Your css code here*/")

        arrContent= self.flaskContent()

    def coreFiles(self, projectType, pathToKeep, projectName):
        self.pathToKeep= pathToKeep
        self.projectName= projectName

        if projectType == "tkinter":
            self.tk_files()
        elif projectType == "flask":
            self.flask_files()
        elif projectType == "flask_api":
            self.flask_api_files()
try:
    import os
except ImportError as e_imp:
    print(f"The following error ocurred: {e_imp}")

class Contents():
    def flask_api_content(self):
        cont_run_app= '''try:
    from app import app
    # from gevent.pywsgi import WSGIServer
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

if __name__== "__main__":
    try:
        # -----------------Dev mode-----------------
        app.run(host= "127.0.0.1", port= 5000, debug= True)
        # debug= True for apply changes made into the files without restarting the flask server

        # -----------------Prod mode----------------
        # appServer= WSGIServer(("127.0.0.1", 5000), app)
        # appServer.serve_forever()
    except Exception as e_imp:
        print(f"The following import ERROR occurred in {__file__}: {e_imp}")
    finally:
        print("Finishing program")'''

        cont_init= '''try:
    from flask import Flask
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

app = Flask(__name__)

from app import routes, admin_routes'''
        
        cont_routes= '''try:
    from app import app
    from flask import Response, request, jsonify, make_response
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

# -------------Endpoints-------------
@app.route("/index", methods=["GET"])
def index() -> Response:
    resp_code = 200
    resp_json = {
        "responseCode": resp_code,
        "responseMessage": "Some message"
    }
    resp_json = make_response(jsonify(resp_json), resp_code)
    return resp_json'''

        cont_adminroutes= '''try:
    from app import app
    from flask import Response, request, jsonify, make_response
    from werkzeug.security import generate_password_hash, check_password_hash
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

# ------------------Admin routes------------------

# -------------Endpoints-------------
@app.route("/admin_index", methods=["GET"])
def admin_index() -> Response:
    resp_code = 200
    resp_json = {
        "responseCode": resp_code,
        "responseMessage": "Some message"
    }
    resp_json = make_response(jsonify(resp_json), resp_code)
    return resp_json'''

        return [cont_run_app, cont_init, cont_routes, cont_adminroutes]

    def tk_content(self):
        contenido1= '''try:
    from biblios import tk_methods
except Exception as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")
    
if __name__== "__main__":
    try:
        met= tk_methods.TkClass()
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
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

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
class TkClass(extraMethods):
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

    def flask_content(self):
        cont_run_app= '''try:
    from app import app
    # from gevent.pywsgi import WSGIServer
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

if __name__== "__main__":
    try:
        # -----------------Dev mode-----------------
        app.run(host= "127.0.0.1", port= 5000, debug= True)
        # debug= True for apply changes made into the files without restarting the flask server

        # -----------------Prod mode----------------
        # appServer= WSGIServer(("127.0.0.1", 5000), app)
        # appServer.serve_forever()
    except Exception as e_imp:
        print(f"The following import ERROR occurred in {__file__}: {e_imp}")
    finally:
        print("Finishing program")'''

        cont_init= '''try:
    from flask import Flask
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

app= Flask(__name__)

from app import routes, admin_routes'''
        
        cont_routes= '''try:
    from app import app
    from datetime import datetime as dt
    from flask import render_template, request
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

# -------------Context processor-------------
@app.context_processor
def dateNow():
    return {
        "now": dt.utcnow()
    }

# -------------Endpoints-------------
@app.route("/")# Welcome HTML template
def index():
    return render_template("welcome.html", page_title="Home")'''

        cont_admin_routes= '''try:
    from app import app
    from flask import render_template
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

# ------------------Admin routes------------------
# Below define your admin routes

# -------------Endpoints-------------
@app.route("/admin")# Admin index HTML template
def index_admin():
    return render_template("welcome.html", page_title="Home")'''

        cont_layout_html= '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="{{url_for('static', filename= 'css/bootstrap/css/bootstrap.css')}}" type="text/css" />
	<link rel="stylesheet" href="{{url_for('static', filename= 'css/per_styles.css')}}" type="text/css" />
    <title>{% block title %}{% endblock %}</title>
    
</head>

<body>
    {% include "includes/navbar.html" %}

    {% if imgback %}
        {% include "includes/background_style.html" %}
    {% endif %}

    {% block content %}{% endblock %}

    {% include "includes/footer.html" %}
    
</body>
</html>'''

        cont_footers= '''<footer class="bg-dark absolute-bottom">
    Platform or project name &copy; Diego Martínez {{now.day}}-{{now.strftime("%B")}}-{{now.year}}
</footer>

<script src="{{url_for('static', filename= 'css/bootstrap/js/bootstrap.js')}}"></script>'''

        return [cont_run_app, cont_init, cont_routes, cont_admin_routes, cont_layout_html, cont_footers]

class Files(Contents):
    path_to_keep= ""
    project_name= ""

    def flask_api_files(self):
        arr_files= [("run_app.py", "app"),#Main path
                   ("__init__.py", "routes.py", "admin_routes.py")]# Inside app folder
        main_project_path= f"{self.path_to_keep}/{self.project_name}"

        arr_content = self.flask_api_content()

        os.makedirs(main_project_path)

        for main_index, direc in enumerate(arr_files):
            for index, elem in enumerate(direc):
                if main_index == 0:
                    temp_path= f"{main_project_path}/{elem}"
                    if ".py" in elem or ".html" in elem:
                        with open(temp_path, "wt", encoding= "utf8") as file:
                            file.write(arr_content[0])
                    else:
                        os.makedirs(temp_path)
                elif main_index == 1:
                    temp_path = f"{main_project_path}/app/{elem}"
                    with open(temp_path, "wt", encoding= "utf8") as file:
                        file.write(arr_content[index+1])

    def tk_files(self):
        arr_files= ["tk_main.py", "tk_methods.py", "__init__.py"]
        main_project_path= f"{self.path_to_keep}/{self.project_name}"
        lib_folder= "biblios"

        arr_content = self.tk_content()

        os.makedirs(f"{main_project_path}/{lib_folder}")

        for index, arch in enumerate(arr_files):
            if index == 0:
                with open(f"{main_project_path}/{arch}", "wt", encoding="utf8") as file:
                    file.write(arr_content[0])

            else:
                with open(f"{main_project_path}/{lib_folder}/{arch}", "wt", encoding= "utf8") as file:
                    if "__init__" in arch:
                        file.write(arr_content[2])
                    else:
                        file.write(arr_content[1])

    def flask_files(self):
        arr_files= [("run_app.py", "app"),#Main path
                   ("__init__.py", "routes.py", "admin_routes.py", "templates", "static"),#Inside app folder
                   ("layout.html", "includes"),#Inside templates folder
                   ("navbar.html", "footer.html"),# Inside includes folder
                   ("css", "img")]#Inside static folder
        main_project_path= f"{self.path_to_keep}/{self.project_name}"

        arr_content= self.flask_content()

        os.makedirs(main_project_path)

        for cont, direc in enumerate(arr_files):
            for elem in direc:
                if cont== 0:
                    temp_path= f"{main_project_path}/{elem}"
                    if ".py" in elem or ".html" in elem:
                        with open(temp_path, "wt", encoding= "utf8") as file:
                            file.write(arr_content[0])
                    else:
                        os.makedirs(temp_path)

                elif cont== 1:
                    temp_path= f"{main_project_path}/app/{elem}"
                    if ".py" in elem or ".html" in elem:
                        if arr_files[1][0]== elem:
                            with open(temp_path, "wt", encoding= "utf8") as file:
                                file.write(arr_content[1])

                        elif arr_files[1][1]== elem:
                            with open(temp_path, "wt", encoding= "utf8") as file:
                                file.write(arr_content[2])

                        elif arr_files[1][2]== elem:
                            with open(temp_path, "wt", encoding= "utf8") as file:
                                file.write(arr_content[3])
                    else:
                        os.makedirs(temp_path)

                elif cont== 2:
                    temp_path= f"{main_project_path}/app/templates/{elem}"
                    if ".py" in elem or ".html" in elem:
                        with open(temp_path, "wt", encoding= "utf8") as file:
                            file.write(arr_content[4])
                    else:
                        os.makedirs(temp_path)

                elif cont== 3:
                    temp_path= f"{main_project_path}/app/templates/includes/{elem}"
                    if arr_files[3][0]== elem:
                        with open(temp_path, "wt", encoding= "utf8") as file:
                            file.write("{# your navbar code here #}")
                    else:
                        with open(temp_path, "wt", encoding= "utf8") as file:
                            file.write("{# your footer code here #}\n")
                            file.write(arr_content[5])

                elif cont== 4:
                    temp_path= f"{main_project_path}/app/static/{elem}"
                    os.makedirs(temp_path)
        temp_path= f"{main_project_path}/app/static/css/per_styles.css"
        with open(temp_path, "wt") as file:
            file.write("/*Your css code here*/")

    def core_files(self, project_type, path_to_keep, project_name):
        self.path_to_keep= path_to_keep
        self.project_name= project_name

        if project_type == "tkinter":
            self.tk_files()
        elif project_type == "flask_web":
            self.flask_files()
        elif project_type == "flask_api":
            self.flask_api_files()
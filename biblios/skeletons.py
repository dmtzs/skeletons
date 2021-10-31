try:
    import os
except ImportError as eImp:
    print(f"The following error ocurred: {eImp}")

class Contents():
    def tkContent(self):
        contenido1= '''try:
    from biblios import tkMethods
except Exception as eImp:
    print(f"Ocurrió el siguiente ERROR de importación: {eImp}")
    
if __name__== "__main__":
    try:
        met= tkMethods.tkClass()
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
    print(f"Ocurrió el siguiente error de importación: {eImp}")

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

        contenido3= '__all__= ["tkMethods"]'

        return contenido1, contenido2, contenido3

    def flaskContent(self):
        pass

class Files(Contents):
    pathToKeep= ""
    projectName= ""

    def tkFiles(self):
        arrFiles= ["tkMain.py", "tkMethods.py", "__init__.py"]
        arrContent= ["", "", ""]
        mainProjectPath= f"{self.pathToKeep}/{self.projectName}"
        libFolder= "biblios"

        arrContent[0], arrContent[1], arrContent[2]= self.tkContent()

        os.makedirs(f"{mainProjectPath}/{libFolder}")

        for arch in range(len(arrFiles)):
            if arch== 0:
                file= open(f"{mainProjectPath}/{arrFiles[arch]}", "wt", encoding="utf8")
                file.write(arrContent[0])

            else:
                file= open(f"{mainProjectPath}/{libFolder}/{arrFiles[arch]}", "wt", encoding= "utf8")

                if "__init__" in arrFiles[arch]:
                    file.write(arrContent[2])
                else:
                    file.write(arrContent[1])
            
            file.close()

    def flaskFiles(self):
        pass

    def coreFiles(self, projectType, pathToKeep, projectName):
        self.pathToKeep= pathToKeep
        self.projectName= projectName

        if projectType== "tkinter":
            self.tkFiles()
        else:
            self.flaskFiles()
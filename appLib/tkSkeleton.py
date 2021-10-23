import os

class tkContent():
    def tkEs(self):
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
        titleLabel.place(x= 102, y= 5)

        ven.mainloop()
        '''

        arrFiles= ["tkMain.py", "tkMethods.py"]

        os.mkdir("./biblios")

        for arch in range(len(arrFiles)):
            if arch== 0:
                file= open(arrFiles[arch], "wt", encoding="utf8")
                file.write(contenido1)
            else:
                file= open(f"./biblios/{arrFiles[arch]}", "wt", encoding= "utf8")
                file.write(contenido2)
            
            file.close()
try:
    import os
    import sys
    import platform
    import webbrowser
    import tkinter as tk
    from biblios import skeletons
    from tkinter.constants import CENTER
    from tkinter import filedialog, messagebox, ttk
except ImportError as e_imp:
    print(f"Ocurrió el siguiente error de importación: {e_imp}")

# -----------------Other methods-----------------
class ExtraMethods():
    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def command_so_shell(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema

    def validar_campos(self, bande, bandeComp):
        if self.banderas[bande] == 0 and bandeComp == 0:
            messagebox.showerror("ERROR", "Por favor selecciona una ruta válida")
        
        elif self.banderas[bande] == 0 and bandeComp == 1:
            messagebox.showerror("ERROR", "El nombre del proyecto no puede estar vacío")

    def repo_git(self):
        webbrowser.open("https://github.com/dmtzs/skeletons")

    def validate_flags(self, componentName):
        if componentName == "":
            return 0
        
        elif componentName.isspace():
            return 0

        else:
            return 1

# -----------------Tkinter widgets methods-----------------
class TkClass(ExtraMethods):
    fileIco = "name.ico"
    title_app = "Skeletons" # Title in the upper part of the main frame
    label_title_app = "Skeletons" # Title in the label
    folder_name = ""
    banderas = [0, 0]

    # -----------------Main window and their components-----------------
    def GUI(self):
        def validate_project_name(*args):
            pro_name = nom_project_entry_text.get()

            self.banderas[1] = self.validate_flags(pro_name)
            self.validar_campos(1, 1)

        def abrir_ruta():
            self.folder_name = filedialog.askdirectory()
            if len(self.folder_name) > 1:
                texto = self.folder_name
                color = "green"
                self.banderas[0] = 1
            else:
                texto = "Por favor elije una ruta"
                color = "red"
                self.banderas[0] = 0
            
            self.validar_campos(0, 0) #Descomentar cuando ya se vaya en esta etapa.
            path_project_label.config(text=texto, fg=color)

        def make_project_core():
            if 0 in self.banderas:
                messagebox.showerror("ERROR", "Por favor, valida los campos que se deben de llenar en el formulario")
            
            else:
                project= skeletons.Files()
                op_selected = valComb.get()
                name_seted = nom_project_entry_text.get()

                project.core_files(op_selected, self.folder_name, name_seted)

                messagebox.showinfo("Éxito", "El proyecto fue creado con éxito, verifícalo en el lugar donde decidiste crearlo")

        ven = tk.Tk()
        comando, sis = self.command_so_shell()
        os.system(comando)
        ven.title(self.title_app)
        ven.columnconfigure(0, weight= 1)
        ven.resizable(width=False, height=False)
        # try:
        #     iconImage= self.resource_path(self.fileIco)
        #     ven.iconbitmap(iconImage)
        # except:
        #     ven.iconbitmap(self.fileIco)
        screenWidth = ven.winfo_screenwidth()# Ancho del área de visualización
        screenHeight = ven.winfo_screenheight()# Alto del área de visualización
        
        width = 500
        height = 550
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        ven.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")

        #Label title of the application
        titleLabel= tk.Label(ven, fg="#179A93", text=self.label_title_app, font=("jost", 25))
        titleLabel.place(relx=0.5, y=25, anchor=CENTER)

        # Label for rtequest the path in which the video or mp3 file will be stored
        saveLabel = tk.Label(ven, text="Ruta para crear el proyecto:", font=("jost", 15))
        saveLabel.place(relx=0.5, y=60, anchor=CENTER)

        # Button for keep the file
        saveEntry = tk.Button(ven, width=10, bg="#179A93", fg="white", text="Ruta", command=abrir_ruta)
        saveEntry.focus()
        saveEntry.place(x=10, y=90)

        # Label for show the path selected
        path_project_label = tk.Label(ven, text="Selecciona la ruta para crear el proyecto", fg="red", font=("jost", 8))
        path_project_label.place(x=90, y=93)

        # Label for create the folder and its name.
        nomProject = tk.Label(ven, text="Nombre del proyecto:", font=("jost", 12))
        nomProject.place(x=10, y=140)

        # Entrybox for the name of the project
        nom_project_entry_text = tk.StringVar()
        nomProjectEntry = tk.Entry(ven, width=30, textvariable=nom_project_entry_text)
        nomProjectEntry.place(x=168, y=142)
        nom_project_entry_text.trace_add("write", validate_project_name)
        nom_project_entry_text.set("project")

        # Label for choose the kind of the project.
        projectLabelCombo = tk.Label(ven, text="Qué tipo de proyecto será?:", font=("jost", 12))
        projectLabelCombo.place(x=10, y=180)

        # Combobox with options to create a flask web application, flask API or tkinter project.
        valuesArr = ["tkinter", "flask_web", "flask_api"]
        valComb = tk.StringVar()
        valComb.set(valuesArr[0])
        projectCombo = ttk.Combobox(ven, values=valuesArr, state="readonly", textvariable=valComb, width=22)
        projectCombo.place(x=215, y=180.5)

        # Radio buttons
        lengVar = tk.IntVar()
        lengVar.set(1)
        lenguajeEn = tk.Radiobutton(ven, text="Español", variable=lengVar, value=1, takefocus=False)#, command= languages)
        lenguajeEn.place(x= 395, y= 5)

        lenguajeEs = tk.Radiobutton(ven, text="English", variable=lengVar, value=2, takefocus=False)#, command= languages)
        lenguajeEs.place(x=395, y=30)

        # Apply button
        applyBut = tk.Button(ven, fg="white", width=10, bg="#179A93", text="Apply", command=make_project_core)
        applyBut.place(relx=0.5, y=240, anchor=CENTER)

        # Label to github repository
        labelGit = tk.Label(ven, text="Repositorio del programa:", font=("jost", 10))
        labelGit.place(x=130, y=525)

        # Button to repository
        butGit=tk.Button(ven, width=10, bg="#179A93", fg="white", text="Repositorio", takefocus=False, command=self.repo_git)
        butGit.place(x=290, y=523)

        ven.mainloop()
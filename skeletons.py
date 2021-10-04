try:
    import os
    import platform
except Exception as eImp:
    print(f"Ocurrió el siguiente ERROR de importación: {eImp}")

def commSO():
    sistema= platform.system()

    if sistema== "Windows":
        return "cls", sistema
    else:
        return "clear", sistema

def tkEs():
    contenidoEs= '''try:
    import os
    import platform
except Exception as eImp:
    print(f"Ocurrió el siguiente ERROR de importación: {eImp}")
    
if __name__== ""__main__:
    try:
        pass
    except Exception as ex:
        print(f"Ocurrió el siguiente ERROR: {ex}")
    except KeyboardInterrupt:
        print("Se presionó Ctrl + C")
    finally:
        print("Finalizando programa")
    '''

    file= open("prueba.py", "wt")
    file.write(contenidoEs)
    file.close()

def core():
    pass

if __name__== "__main__":
    try:
        comm, sis= commSO()
        os.system(comm)
        core()
        print("Archivos creados con éxito")
    except Exception as ex:
        print(f"Ocurrió el siguiente ERROR: {ex}")
    except KeyboardInterrupt:
        print("Se presionó Ctrl + C")
    finally:
        print("Finalizando programa")
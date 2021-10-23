try:
    import os
    import sys
    import platform
    from appLib import tkSkeleton, flaskSkeleton
except Exception as eImp:
    print(f"Ocurrió el siguiente ERROR de importación: {eImp}")

def commSO():
    sistema= platform.system()

    if sistema== "Windows":
        return "cls", sistema
    else:
        return "clear", sistema

def core():
    lenargv= len(sys.argv)

    if lenargv== 2:
        if sys.argv[1]== "--tk":
            tkSkel= tkSkeleton.tkContent()
            tkSkel.tkEs()
        
        elif sys.argv[1]== "--flask":
            tkSkel= flaskSkeleton.flaskContent()
            tkSkel.flaskEs()
    else:
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
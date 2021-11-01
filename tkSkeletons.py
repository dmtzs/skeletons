try:
    from biblios import *#Module imported: tkMethods
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
        
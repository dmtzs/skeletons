try:
    from biblios import *#Module imported: tkMethods
except Exception as e_imp:
    print(f"Ocurrió el siguiente ERROR de importación: {e_imp}")
    
if __name__== "__main__":
    try:
        met = tk_methods.TkClass()
        met.GUI()
    except Exception as ex:
        print(f"Ocurrió el ERROR: {ex}")
    except KeyboardInterrupt:
        print("Se presionó Ctrl + C")
    finally:
        print("Finalizando programa")
        
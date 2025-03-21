from tkinter import*
from tkinter import ttk
import ConexionBD as m
#Marco

class Servicio:
    db_name='db_hospitales'
    def __init__(self, Ventana_i=None):
        self.window = Ventana_i
        self.window.title("Aplicación")
        self.window.geometry("800x600")
        self.window.resizable(0,0)
        self.window.config(bd = 10)
        Titulo = Label(Ventana_i,text="Servicios", fg="black", font=("Comic Sans", 17,"bold"),pady=10).pack()
        if Ventana_i is not None:  # Verificar si se proporcionó una ventana
            self.tree=ttk.Treeview(Ventana_i, height=13, columns=("columna1"))
            self.tree.heading("#0",text='Código Servicio', anchor=CENTER)
            self.tree.column("#0", width=100, minwidth=75, stretch=NO)
            
            self.tree.heading("columna1",text='Descripción Servicio',anchor=CENTER)
            self.tree.column("columna1",width=150,minwidth=75,stretch=NO)
            
            self.tree.pack()
            
            self.Obtener_Datos()
    
    def Obtener_Datos(self):
        registros=self.tree.get_children()
        for element in registros:
            self.tree.delete(element)
        query='SELECT * FROM servicios'
        db_rows=self.Ejecutar_Consulta(query)
        for row in db_rows:
            self.tree.insert("",0,text=row[1],values=(row[2]))
                
    def Ejecutar_Consulta(self, query, parameters=()):
        connection = m.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, parameters)
                result = cursor.fetchall()
                connection.commit()
                return result
            except m.Error as e:
                print(f"Error executing query: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
        else:
            print("Error: No se pudo establecer la conexión con la base de datos.")
            return []

if __name__=="__main__":
    Ventana_i = None  # Establecer la ventana como None
    app = Servicio(Ventana_i)

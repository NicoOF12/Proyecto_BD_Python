from tkinter import *
from tkinter import ttk
import ConexionBD as m

class Hospital:
    """
    Clase que representa la interfaz gráfica para gestionar información de hospitales.

    Atributos:
        db_name (str): Nombre de la base de datos utilizada.
        window (Tk | None): Referencia a la ventana principal de la aplicación.
        tree (ttk.Treeview): Tabla donde se muestran los datos de los hospitales.
    """

    db_name = 'db_hospitales'

    def __init__(self, Ventana_i=None):
        """
        Constructor de la clase Hospital. Inicializa la ventana principal y la interfaz gráfica.

        Args:
            Ventana_i (Tk | None): Instancia de la ventana principal de Tkinter.
        """
        self.window = Ventana_i

        # Configuración de la ventana
        if self.window is not None:
            self.window.title("Aplicación")
            self.window.geometry("800x600")
            self.window.resizable(0, 0)
            self.window.config(bd=10)

            # Título de la interfaz
            Label(self.window, text="Hospital", fg="black", font=("Comic Sans", 17, "bold"), pady=10).pack()

            # Configuración del Treeview (tabla de datos)
            self.tree = ttk.Treeview(self.window, height=13, columns=("columna1", "columna2", "columna3", "columna4"))

            # Definir encabezados de la tabla
            self.tree.heading("#0", text='Municipio', anchor=CENTER)
            self.tree.column("#0", width=120, minwidth=75, stretch=NO)

            self.tree.heading("columna1", text='Dirección', anchor=CENTER)
            self.tree.column("columna1", width=170, minwidth=75, stretch=NO)

            self.tree.heading("columna2", text='Nombre', anchor=CENTER)
            self.tree.column("columna2", width=150, minwidth=75, stretch=NO)

            self.tree.heading("columna3", text='Teléfono', anchor=CENTER)
            self.tree.column("columna3", width=150, minwidth=75, stretch=NO)

            self.tree.heading("columna4", text='Cantidad de camas', anchor=CENTER)
            self.tree.column("columna4", width=150, minwidth=75, stretch=NO)

            self.tree.pack()

            # Cargar datos iniciales
            self.Obtener_Datos()

    def Obtener_Datos(self):
        """
        Obtiene los datos de la base de datos y los carga en la tabla (Treeview).
        """
        # Limpiar la tabla antes de cargar nuevos datos
        registros = self.tree.get_children()
        for element in registros:
            self.tree.delete(element)

        # Consulta SQL para obtener los datos de la tabla "hospital"
        query = 'SELECT * FROM hospital'
        db_rows = self.Ejecutar_Consulta(query)

        # Insertar los datos en la tabla
        for row in db_rows:
            self.tree.insert("", 0, text=row[1], values=(row[2], row[3], row[4], row[5]))

    def Ejecutar_Consulta(self, query, parameters=()):
        """
        Ejecuta una consulta SQL en la base de datos.

        Args:
            query (str): La consulta SQL a ejecutar.
            parameters (tuple, opcional): Parámetros para la consulta SQL.

        Returns:
            list: Lista con los resultados obtenidos de la base de datos.
        """
        connection = m.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, parameters)
                result = cursor.fetchall()
                connection.commit()
                return result
            except m.Error as e:
                print(f"Error al ejecutar la consulta: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
        else:
            print("Error: No se pudo establecer la conexión con la base de datos.")
            return []

if __name__ == "__main__":
    Ventana_i = None  # Establecer la ventana como None
    app = Hospital(Ventana_i)

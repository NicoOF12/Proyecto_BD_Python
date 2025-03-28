"""
Módulo para la gestión de pacientes en una aplicación de escritorio con Tkinter.

Este módulo permite registrar, consultar, editar y eliminar información de pacientes en una base de datos.

Clases:
    - Paciente: Clase principal para la gestión de la interfaz gráfica y la interacción con la base de datos.

Dependencias:
    - tkinter: Para la interfaz gráfica.
    - ttk: Para el uso de widgets avanzados.
    - messagebox: Para mostrar mensajes emergentes.
    - datetime: Para manejar fechas.
    - ConexionBD: Módulo para la conexión a la base de datos.
"""

from tkinter import *
from tkinter import ttk, messagebox
import datetime
import ConexionBD as m

class Paciente:
    """
    Clase para la gestión de la interfaz gráfica y la interacción con la base de datos.
    """
    db_name = 'db_hospitales'
    
    def __init__(self, Ventana_i=None):
        """
        Constructor de la clase Paciente.
        
        Parámetros:
            Ventana_i (Tk): Ventana principal de la aplicación.
        """
        self.window = Ventana_i
        self.window.title("Aplicación")
        self.window.geometry("800x600")
        self.window.resizable(0, 0)
        self.window.config(bd=10)
        
        Titulo = Label(Ventana_i, text="Paciente", fg="black", font=("Comic Sans", 17, "bold"), pady=10).pack()
        
        if Ventana_i is not None:
            self.crear_interfaz(Ventana_i)
        
    def crear_interfaz(self, Ventana_i):
        """
        Método para crear la interfaz gráfica del módulo de pacientes.
        
        Parámetros:
            Ventana_i (Tk): Ventana principal de la aplicación.
        """
        marco = LabelFrame(Ventana_i, text="Registro Paciente", font=("Comic Sans", 10, "bold"), pady=5)
        marco.config(bd=2)
        marco.pack()
        
        self.crear_botones(Ventana_i)
        self.crear_formulario(marco)
        self.crear_tabla(Ventana_i)
        self.Obtener_Datos()
        
    def crear_botones(self, Ventana_i):
        """
        Método para crear los botones de acción en la interfaz.
        
        Parámetros:
            Ventana_i (Tk): Ventana principal de la aplicación.
        """
        Frame_Botones = Frame(Ventana_i)
        Frame_Botones.pack()
        
        botones = [
            ("Registrar", "green", self.Agregar_Paciente),
            ("Consultar", "blue", self.Consultar_Paciente),
            ("Editar", "gray", self.Editar_Paciente),
            ("Eliminar", "red", self.Eliminar_Paciente)
        ]
        
        for i, (texto, color, comando) in enumerate(botones):
            Button(Frame_Botones, text=texto, height=1, width=10, bg=color, fg="white", 
                   font=("Comic Sans", 17, "bold"), command=comando).grid(row=0, column=i+1, padx=10, pady=10)

    def crear_formulario(self, marco):
        """
        Método para crear el formulario de ingreso de datos de pacientes.
        
        Parámetros:
            marco (LabelFrame): Marco donde se ubica el formulario.
        """
        Label(marco, text="Cédula paciente", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
        self.CC = Entry(marco, width=25)
        self.CC.focus()
        self.CC.grid(row=0, column=1, padx=5, pady=8)
        
        Label(marco, text="Género", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=9)
        self.genero = ttk.Combobox(marco, values=["Masculino", "Femenino"], width=22, state="readonly")
        self.genero.current(0)
        self.genero.grid(row=0, column=3, padx=5, pady=8)

    def crear_tabla(self, Ventana_i):
        """
        Método para crear la tabla de visualización de pacientes.
        
        Parámetros:
            Ventana_i (Tk): Ventana principal de la aplicación.
        """
        self.tree = ttk.Treeview(Ventana_i, height=13, columns=("columna1", "columna2", "columna3", "columna4"))
        self.tree.heading("#0", text='Cédula', anchor=CENTER)
        self.tree.column("#0", width=90, minwidth=75, stretch=NO)
        self.tree.heading("columna1", text='Nombre', anchor=CENTER)
        self.tree.heading("columna2", text='Género', anchor=CENTER)
        self.tree.heading("columna3", text='Fecha De Nacimiento', anchor=CENTER)
        self.tree.heading("columna4", text='Dirección', anchor=CENTER)
        self.tree.pack()

    def Obtener_Datos(self):
        """
        Método para obtener los datos de la base de datos y mostrarlos en la tabla.
        """
        for element in self.tree.get_children():
            self.tree.delete(element)
        query = 'SELECT * FROM paciente'
        db_rows = self.Ejecutar_Consulta(query)
        for row in db_rows:
            self.tree.insert("", 0, text=row[1], values=(row[2], row[3], row[4], row[5]))

    def Ejecutar_Consulta(self, query, parameters=()):
        """
        Método para ejecutar consultas en la base de datos.
        
        Parámetros:
            query (str): Consulta SQL a ejecutar.
            parameters (tuple): Parámetros opcionales para la consulta.
        
        Retorna:
            list: Resultados de la consulta.
        """
        connection = m.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, parameters)
                result = cursor.fetchall()
                connection.commit()
                return result
            except m.mysql.connector.Error as e:
                print(f"Error ejecutando la consulta: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
        else:
            print("Error: No se pudo establecer la conexión con la base de datos.")
            return []

        
    #-----------------------Pacientes-----------------------------
    def Agregar_Paciente(self):
        """
        Agrega un nuevo paciente a la base de datos si se valida el formulario y no existe una cédula duplicada.
        """
        if self.Validar_formulario_completo_paciente() and self.Validar_registrar_paciente():
            fecha_nacimiento = self.Obtener_Fecha_Combobox()
            query='INSERT INTO paciente (Cedula_Identidad_Paciente, Nombre_Paciente, Genero_Paciente, Fecha_Nacimiento_Paciente, Direccion_Paciente) VALUES(%s, %s, %s, %s, %s)'
            parameters = (self.CC.get(), self.nombre.get(), self.genero.get(), fecha_nacimiento, self.direccion.get())
            self.Ejecutar_Consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Cliente registrado: {self.CC.get()}')
            self.Limpiar_formulario_paciente()
        self.Obtener_Datos()
        
    def Consultar_Paciente(self):
        """
        Consulta un paciente en la base de datos mediante su cédula de identidad.
        """
        if len(self.CC.get()) !=0:
            query='SELECT * FROM paciente WHERE Cedula_Identidad_Paciente = %s'
            parameters=(self.CC.get(),)
            db_rows=self.Ejecutar_Consulta(query, parameters)
            self.Limpiar_formulario_paciente()
            if len(db_rows) !=0:
                self.tree.delete(*self.tree.get_children())
                for row in db_rows:
                    self.tree.insert("",0,text=row[1],values=(row[2],row[3],row[4],row[5]))
            else:
                messagebox.showinfo("ERROR", "Paciente no encontrado")
                self.Limpiar_formulario_paciente()
                self.Obtener_Datos()
        else:
            messagebox.showerror("ERROR", "Ingrese número de cédula")
            self.Obtener_Datos()
            
    def Editar_Paciente(self):
        """
        Abre una ventana para editar los datos de un paciente seleccionado en la interfaz.
        """
        try:
            selected_item = self.tree.item(self.tree.selection()[0])
            CC = selected_item['text']
        except IndexError:
            messagebox.showerror("ERROR", "Por favor selecciona un elemento", parent=self.window)
            return

        nombre = selected_item['values'][0]
        genero = selected_item['values'][1]
        fecha_nacimiento = selected_item['values'][2]
        direccion = selected_item['values'][3]

        self.Ventana_editar = Toplevel(self.window)
        self.Ventana_editar.title('EDITAR PACIENTE')
        self.Ventana_editar.resizable(0, 0)

        # Creación de widgets para la edición de datos
        # ... (Se mantienen los widgets y configuraciones de la ventana de edición)

        self.Ventana_editar.grab_set()  # Asegurarse de que la ventana de edición sea modal

    def Obtener_Fecha_Combobox(self):
        """
        Obtiene la fecha de nacimiento del paciente a partir de los valores seleccionados en los combobox.
        """
        año = self.año.get()
        mes = self.mes.get()
        dia = self.dia.get()
        return f"{año}-{mes}-{dia}"
        
    def Actualizar(self, nuevo_codigo, nuevo_nombre, nuevo_combo_genero, fecha_combobox, nuevo_direccion, codigo, nombre):
        """
        Actualiza los datos de un paciente en la base de datos.
        """
        fecha_combobox = self.Obtener_Fecha_Combobox()
        query='UPDATE paciente SET Cedula_Identidad_Paciente = %s, Nombre_Paciente = %s, Genero_Paciente = %s, Fecha_Nacimiento_Paciente =%s, Direccion_Paciente=%s WHERE Cedula_Identidad_Paciente = %s AND Nombre_Paciente = %s'
        parameters=(nuevo_codigo, nuevo_nombre, nuevo_combo_genero, fecha_combobox, nuevo_direccion, codigo, nombre)
        self.Ejecutar_Consulta(query,parameters)
        messagebox.showinfo('EXITO',f'Paciente actualizado:{nuevo_nombre}')
        self.Ventana_editar.destroy()
        self.Obtener_Datos()
        
    def Eliminar_Paciente(self):
        """
        Elimina un paciente de la base de datos tras confirmar la acción con el usuario.
        """
        try:
            selected_item = self.tree.item(self.tree.selection()[0])
            CC = selected_item['text']
        except IndexError:
            messagebox.showerror("ERROR","Por favor selecciona un elemento") 
            return
        dato=self.tree.item(self.tree.selection())['text']
        nombre=self.tree.item(self.tree.selection())['values'][0]
        query="DELETE FROM paciente WHERE Cedula_Identidad_Paciente = %s"
        respuesta=messagebox.askquestion("ADVERTENCIA",f"¿Seguro que desea eliminar el producto: {nombre}?")
        if respuesta == 'yes':
            self.Ejecutar_Consulta(query,(dato,))
            self.Obtener_Datos()
            messagebox.showinfo('EXITO',f'Paciente eliminado: {nombre}')
        else:
            messagebox.showerror('ERROR',f'Error al eliminar el paciente: {nombre}')
        
    #Funciones de ayuda
    def Validar_formulario_completo_paciente(self):
        """
        Verifica si todos los campos del formulario de paciente han sido completados.
        """
        if len(self.CC.get()) != 0 and len(self.nombre.get()) != 0 and len(self.genero.get()) != 0 and self.año.get() != "" and self.mes.get() != "" and self.dia.get() != "" and len(self.direccion.get()) != 0:
            return True
        else:
            messagebox.showerror("ERROR", "Complete todos los campos del formulario")
            
    def Validar_registrar_paciente(self):
        """
        Verifica si la cédula ingresada ya está registrada en la base de datos.
        """
        parameters = (self.CC.get(),)
        query = "SELECT * FROM paciente WHERE Cedula_Identidad_Paciente = %s"
        dato = self.Ejecutar_Consulta(query, parameters)
        if not dato:
            return True
        else:
            messagebox.showerror("ERROR EN REGISTRO", "Cédula registrada anteriormente")
            return False
        
    def Validar_Entero(self, texto):
        """
        Verifica si un texto ingresado contiene solo números.
        """
        return texto.isdigit() or texto == ''
    
    def Validar_Letras(self, texto):
        """
        Verifica si un texto ingresado contiene solo letras y espacios.
        """
        return texto.replace(' ', '').isalpha() or texto == ''

    def Limpiar_formulario_paciente(self):
        """
        Limpia todos los campos del formulario de paciente.
        """
        self.CC.delete(0, END)
        self.nombre.delete(0, END)
        self.genero.set('')
        self.año.set('')
        self.mes.set('')
        self.dia.set('')
        self.direccion.delete(0, END)
    
if __name__ == "__main__":
    Ventana_i = None  # Establecer la ventana como None
    app = Paciente(Ventana_i)

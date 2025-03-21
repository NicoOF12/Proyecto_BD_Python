from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import datetime
import ConexionBD as m
#Marco

class Paciente:
    db_name='db_hospitales'
    def __init__(self, Ventana_i=None):
        self.window = Ventana_i
        self.window.title("Aplicación")
        self.window.geometry("800x600")
        self.window.resizable(0, 0)
        self.window.config(bd = 10)
        
        Titulo = Label(Ventana_i, text="Paciente", fg="black", font=("Comic Sans", 17, "bold"), pady=10).pack()
        if Ventana_i is not None:    
            marco = LabelFrame(Ventana_i, text="Registro Paciente", font=("Comic Sans", 10, "bold"), pady=5)
            marco.config(bd=2)
            marco.pack()
            
            # Botones y acciones del menú    
            Frame_Botones = Frame(Ventana_i)
            Frame_Botones.pack()
            
            Boton_registrar = Button(Frame_Botones, text="Registrar", height=1, width=10, bg="green", fg="white", font=("Comic Sans", 17, "bold"), command=self.Agregar_Paciente)
            Boton_registrar.grid(row=0, column=1, padx=10, pady=10)        
            
            Boton_consultar = Button(Frame_Botones, text="Consultar", height=1, width=10, bg="blue", fg="white", font=("Comic Sans", 17, "bold"), command=self.Consultar_Paciente)
            Boton_consultar.grid(row=0, column=2, padx=10, pady=10)        
            
            Boton_editar = Button(Frame_Botones, text="Editar", height=1, width=10, bg="gray", fg="white", font=("Comic Sans", 17, "bold"), command=self.Editar_Paciente)
            Boton_editar.grid(row=0, column=3, padx=10, pady=10)        
            
            Boton_eliminar = Button(Frame_Botones, text="Eliminar", height=1, width=10, bg="red", fg="white", font=("Comic Sans", 17, "bold"), command=self.Eliminar_Paciente)
            Boton_eliminar.grid(row=0, column=4, padx=10, pady=10)
            
            # Formulario Paciente
            Label_CC = Label(marco, text="Cédula paciente", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
            self.CC = Entry(marco, width=25, validate='key', validatecommand=(self.window.register(self.Validar_Entero), '%P'))
            self.CC.focus()
            self.CC.grid(row=0, column=1, padx=5, pady=8)
            
            
            Label_genero = Label(marco, text="Género", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=9)
            self.genero = ttk.Combobox(marco, values=["Masculino", "Femenino"], width=22, state="readonly")
            self.genero.current(0)
            self.genero.grid(row=0, column=3, padx=5, pady=8)
            
            Label_nombre = Label(marco, text="Nombre completo", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
            self.nombre = Entry(marco, width=25, validate='key', validatecommand=(self.window.register(self.Validar_Letras), '%P'))
            self.nombre.grid(row=1, column=1, padx=5, pady=8)
            
            Label_fecha_nacimiento = Label(marco, text="Fecha de Nacimiento", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=9)
        
            # Combobox for date selection
            self.año = ttk.Combobox(marco, values=[str(i) for i in range(1900, datetime.datetime.now().year + 1)], width=5, state="readonly")
            self.año.grid(row=1, column=3, padx=5, pady=8, sticky='w')
            
            self.mes = ttk.Combobox(marco, values=[str(i).zfill(2) for i in range(1, 13)], width=5, state="readonly")
            self.mes.grid(row=1, column=3, padx=5, pady=8)
            
            self.dia = ttk.Combobox(marco, values=[str(i).zfill(2) for i in range(1, 32)], width=5, state="readonly")
            self.dia.grid(row=1, column=3, padx=5, pady=8, sticky='e')
            
            Label_direccion = Label(marco, text="Dirección paciente", font=("Comic Sans", 10, "bold")).grid(row=2, column=1, sticky='s', padx=5, pady=8)
            self.direccion = Entry(marco, width=25)
            self.direccion.grid(row=2, column=2, padx=5, pady=8)
            
            # Tabla de registro
            self.tree = ttk.Treeview(Ventana_i, height=13, columns=("columna1", "columna2", "columna3", "columna4"))  # Agregada a Ventana_i
            self.tree.heading("#0", text='Cédula', anchor=CENTER)
            self.tree.column("#0", width=90, minwidth=75, stretch=NO)
            
            self.tree.heading("columna1", text='Nombre', anchor=CENTER)
            self.tree.column("columna1", width=150, minwidth=75, stretch=NO)
            
            self.tree.heading("columna2", text='Género', anchor=CENTER)
            self.tree.column("columna2", width=150, minwidth=75, stretch=NO)
            
            self.tree.heading("columna3", text='Fecha De Nacimiento', anchor=CENTER)
            self.tree.column("columna3", width=150, minwidth=75, stretch=NO)
            
            self.tree.heading("columna4", text='Dirección', anchor=CENTER)
            self.tree.column("columna4", width=150, minwidth=75, stretch=NO)
            
            self.tree.pack()
            
            self.Obtener_Datos()
                    
        #CRUD
        
    def Obtener_Datos(self):
        registros=self.tree.get_children()
        for element in registros:
            self.tree.delete(element)
        query='SELECT * FROM paciente'
        db_rows=self.Ejecutar_Consulta(query)
        for row in db_rows:
            self.tree.insert("",0,text=row[1],values=(row[2],row[3],row[4],row[5]))
                
    def Ejecutar_Consulta(self, query, parameters=()):
        connection = m.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, parameters)
                result = cursor.fetchall()
                connection.commit()
                return result
            except m.mysql.connector.Error as e:
                print(f"Error executing query: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
        else:
            print("Error: No se pudo establecer la conexión con la base de datos.")
            return []
        
    #-----------------------Pacientes-----------------------------
    def Agregar_Paciente(self):
        if self.Validar_formulario_completo_paciente() and self.Validar_registrar_paciente():
            fecha_nacimiento = self.Obtener_Fecha_Combobox()
            query='INSERT INTO paciente (Cedula_Identidad_Paciente, Nombre_Paciente, Genero_Paciente, Fecha_Nacimiento_Paciente, Direccion_Paciente) VALUES(%s, %s, %s, %s, %s)'
            parameters = (self.CC.get(), self.nombre.get(), self.genero.get(), fecha_nacimiento, self.direccion.get())
            self.Ejecutar_Consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Cliente registrado: {self.CC.get()}')
            self.Limpiar_formulario_paciente()
        self.Obtener_Datos()
        
    def Consultar_Paciente(self):
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

        # Valores ventana editar
        label_CC = Label(self.Ventana_editar, text="Cédula paciente: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
        nueva_CC = Entry(self.Ventana_editar, width=25, validate='key', validatecommand=(self.window.register(self.Validar_Entero), '%P'))
        nueva_CC.insert(0, CC)  # Inserta el valor de la cédula en la casilla de entrada
        nueva_CC.grid(row=0, column=1, padx=5, pady=8)

        label_nombre = Label(self.Ventana_editar, text="Nombre del paciente: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
        nuevo_nombre = Entry(self.Ventana_editar, width=25, validate='key', validatecommand=(self.window.register(self.Validar_Letras), '%P'))
        nuevo_nombre.insert(0, nombre)  # Inserta el valor del nombre en la casilla de entrada
        nuevo_nombre.grid(row=1, column=1, padx=5, pady=8)

        label_genero = Label(self.Ventana_editar, text="Género: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=9)
        nuevo_combo_genero = ttk.Combobox(self.Ventana_editar, values=["Masculino", "Femenino"], width=22, state="readonly")
        nuevo_combo_genero.set(genero)
        nuevo_combo_genero.grid(row=2, column=1, padx=5, pady=0)

        Label_fecha_nacimiento = Label(self.Ventana_editar, text="Fecha de Nacimiento", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=9)
        
        # Dividir la fecha de nacimiento en año, mes y día
        año, mes, dia = fecha_nacimiento.split('-')

        # Combobox for date selection
        self.año = ttk.Combobox(self.Ventana_editar, values=[str(i) for i in range(1900, datetime.datetime.now().year + 1)], width=5, state="readonly")
        self.año.grid(row=0, column=3, padx=5, pady=8, sticky='w')
        self.año.set(año)

        self.mes = ttk.Combobox(self.Ventana_editar, values=[str(i).zfill(2) for i in range(1, 13)], width=5, state="readonly")
        self.mes.grid(row=0, column=3, padx=5, pady=8)
        self.mes.set(mes)

        self.dia = ttk.Combobox(self.Ventana_editar, values=[str(i).zfill(2) for i in range(1, 32)], width=5, state="readonly")
        self.dia.grid(row=0, column=3, padx=5, pady=8, sticky='e')
        self.dia.set(dia)

        label_direccion = Label(self.Ventana_editar, text="Dirección: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
        nueva_direccion = Entry(self.Ventana_editar, textvariable=StringVar(self.Ventana_editar, value=direccion), width=25)
        nueva_direccion.grid(row=1, column=3, padx=5, pady=8)

        boton_actualizar = Button(self.Ventana_editar, text="ACTUALIZAR", command=lambda: self.Actualizar(nueva_CC.get(), nuevo_nombre.get(), nuevo_combo_genero.get(), self.Obtener_Fecha_Combobox(), nueva_direccion.get(), CC, nombre), height=2, width=20, bg="black", fg="white", font=("Comic Sans", 10, "bold"))
        boton_actualizar.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

        self.Ventana_editar.grab_set()  # Asegurarse de que la ventana de edición sea modal


    def Obtener_Fecha_Combobox(self):
        año = self.año.get()
        mes = self.mes.get()
        dia = self.dia.get()
        return f"{año}-{mes}-{dia}"
        
    def Actualizar(self,nuevo_codigo,nuevo_nombre,nuevo_combo_genero,fecha_combobox,nuevo_direccion,codigo,nombre):
        fecha_combobox = self.Obtener_Fecha_Combobox()
        query='UPDATE paciente SET Cedula_Identidad_Paciente = %s, Nombre_Paciente = %s, Genero_Paciente = %s, Fecha_Nacimiento_Paciente =%s, Direccion_Paciente=%s WHERE Cedula_Identidad_Paciente = %s AND Nombre_Paciente = %s'
        parameters=(nuevo_codigo,nuevo_nombre,nuevo_combo_genero,fecha_combobox,nuevo_direccion,codigo,nombre)
        self.Ejecutar_Consulta(query,parameters)
        messagebox.showinfo('EXITO',f'Paciente actualizado:{nuevo_nombre}')
        self.Ventana_editar.destroy()
        self.Obtener_Datos()
        
    def Eliminar_Paciente(self):
        try:
            selected_item = self.tree.item(self.tree.selection()[0])
            CC = selected_item['text']
        except IndexError as e:
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
        if len(self.CC.get()) != 0 and len(self.nombre.get()) != 0 and len(self.genero.get()) != 0 and self.año.get() != "" and self.mes.get() != "" and self.dia.get() != "" and len(self.direccion.get()) != 0:
            return True
        else:
            messagebox.showerror("ERROR", "Complete todos los campos del formulario")
            
    def Validar_registrar_paciente(self):
        parameters = (self.CC.get(),)
        query = "SELECT * FROM paciente WHERE Cedula_Identidad_Paciente = %s"
        dato = self.Ejecutar_Consulta(query, parameters)
        if not dato:
            return True
        else:
            messagebox.showerror("ERROR EN REGISTRO", "Cédula registrada anteriormente")
            return False
        
    def Validar_Entero(self, texto):
        return texto.isdigit() or texto == ''
    
    def Validar_Letras(self, texto):
        return texto.replace(' ', '').isalpha() or texto == ''

            
    def Limpiar_formulario_paciente(self):
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
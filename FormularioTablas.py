'''
Módulo: Base.py
Descripción: Interfaz principal de la aplicación de gestión hospitalaria usando Tkinter.
Autor: [Tu Nombre]
Fecha: [Fecha de creación/modificación]
'''

# Importaciones necesarias para la interfaz gráfica y la interacción con otros módulos
from tkinter import *  # Importa todas las funciones de Tkinter
from tkinter import ttk  # Importa los widgets mejorados de Tkinter
from tkinter import messagebox  # Importa la funcionalidad para cuadros de diálogo emergentes

# Importación de módulos que contienen las funcionalidades específicas de la aplicación
import ConsultaHospital as h  # Módulo para gestionar hospitales
import ConsultaMedico as m  # Módulo para gestionar médicos
import ConsultaLaboratorio as l  # Módulo para gestionar laboratorios
import ConsultaServicio as s  # Módulo para gestionar servicios
import CRUDPacientes as p  # Módulo para gestionar pacientes

class Base:
    '''
    Clase Base que representa la ventana principal de la aplicación.
    Contiene botones para acceder a diferentes módulos de consulta.
    '''
    
    def __init__(self, Ventana_Base):
        '''
        Constructor de la clase Base.
        Configura la ventana principal y sus componentes.
        :param Ventana_Base: Instancia de Tk que representa la ventana principal.
        '''
        self.window = Ventana_Base
        self.window.title("Aplicación")  # Título de la ventana
        self.window.geometry("800x300")  # Tamaño de la ventana
        self.window.resizable(0,0)  # Evita redimensionamiento
        self.window.config(bd=10)  # Agrega borde a la ventana
        
        # Título de la interfaz
        Label(Ventana_Base, text="Base de Datos hospital", fg="black", font=("Comic Sans", 17, "bold"), pady=10).pack()
        
        # Frame para organizar los botones
        Frame_Botones = Frame(Ventana_Base)
        Frame_Botones.pack()
        
        # Botón para abrir el módulo de Hospitales
        Boton_hospital = Button(Frame_Botones, text="Hospital", height=2, width=10, bg="green", fg="white",
                                font=("Comic Sans", 17, "bold"), command=self.llamar_consulta_hospital)
        Boton_hospital.grid(row=0, column=1, padx=10, pady=10)
        
        # Botón para abrir el módulo de Médicos
        Boton_Medico = Button(Frame_Botones, text="Médico", height=2, width=10, bg="green", fg="white",
                              font=("Comic Sans", 17, "bold"), command=self.llamar_consulta_medico)
        Boton_Medico.grid(row=0, column=2, padx=10, pady=10)
        
        # Botón para abrir el módulo de Pacientes
        Boton_Paciente = Button(Frame_Botones, text="Paciente", height=2, width=10, bg="green", fg="white",
                                font=("Comic Sans", 17, "bold"), command=self.llamar_consulta_paciente)
        Boton_Paciente.grid(row=0, column=3, padx=10, pady=10)
        
        # Botón para abrir el módulo de Laboratorios
        Boton_Laboratorio = Button(Frame_Botones, text="Laboratorio", height=2, width=10, bg="green", fg="white",
                                   font=("Comic Sans", 17, "bold"), command=self.llamar_consulta_laboratorio)
        Boton_Laboratorio.grid(row=1, column=2, padx=10, pady=10)
        
        # Botón para abrir el módulo de Servicios
        Boton_Servicio = Button(Frame_Botones, text="Servicio", height=2, width=10, bg="green", fg="white",
                                font=("Comic Sans", 17, "bold"), command=self.llamar_consulta_servicio)
        Boton_Servicio.grid(row=1, column=3, padx=10, pady=10)
    
    def llamar_consulta_hospital(self):
        ''' Abre la ventana de consulta de Hospitales '''
        Ventana_Hospital = Toplevel(self.window)
        h.Hospital(Ventana_Hospital)
        Ventana_Hospital.transient(self.window)
        Ventana_Hospital.grab_set()
    
    def llamar_consulta_medico(self):
        ''' Abre la ventana de consulta de Médicos '''
        Ventana_Medico = Toplevel(self.window)
        m.Medico(Ventana_Medico)
        Ventana_Medico.transient(self.window)
        Ventana_Medico.grab_set()
    
    def llamar_consulta_paciente(self):
        ''' Abre la ventana de consulta de Pacientes '''
        Ventana_Paciente = Toplevel(self.window)
        p.Paciente(Ventana_Paciente)
        Ventana_Paciente.transient(self.window)
        Ventana_Paciente.grab_set()
    
    def llamar_consulta_laboratorio(self):
        ''' Abre la ventana de consulta de Laboratorios '''
        Ventana_Laboratorio = Toplevel(self.window)
        l.Laboratorio(Ventana_Laboratorio)
        Ventana_Laboratorio.transient(self.window)
        Ventana_Laboratorio.grab_set()

    def llamar_consulta_servicio(self):
        ''' Abre la ventana de consulta de Servicios '''
        Ventana_Servicio = Toplevel(self.window)
        s.Servicio(Ventana_Servicio)
        Ventana_Servicio.transient(self.window)
        Ventana_Servicio.grab_set()

# Punto de entrada de la aplicación
if __name__ == "__main__":
    Ventana_Base = Tk()
    app = Base(Ventana_Base)
    Ventana_Base.mainloop()

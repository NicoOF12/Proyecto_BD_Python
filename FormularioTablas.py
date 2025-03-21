#importaciones
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ConsultaHospital as h
import ConsultaMedico as m
import ConsultaLaboratorio as l
import ConsultaServicio as s
import CRUDPacientes as p

import ConsultaHospital as h  # Importar el módulo

class Base:
    
    def __init__(self, Ventana_Base):
        self.window = Ventana_Base
        self.window.title("Aplicación")
        self.window.geometry("800x300")
        self.window.resizable(0,0)
        self.window.config(bd = 10)
        
        Titulo = Label(Ventana_Base,text="Base de Datos hospital", fg="black", font=("Comic Sans", 17,"bold"),pady=10).pack()
        
        Frame_Botones = Frame(Ventana_Base)
        Frame_Botones.pack()
        
        # Botón para llamar al módulo ConsultaHospital.py
        Boton_hospital = Button(Frame_Botones,text="Hospital",height=2,width=10,bg="green",fg="white",font=("Comic Sans", 17,"bold"), command=self.llamar_consulta_hospital)
        Boton_hospital.grid(row=0, column=1, padx=10, pady=10)
        
        # Botón para llamar al módulo ConsultaMedico.py
        Boton_Medico = Button(Frame_Botones,text="Médico",height=2,width=10,bg="green",fg="white",font=("Comic Sans", 17,"bold"), command=self.llamar_consulta_medico)
        Boton_Medico.grid(row=0, column=2, padx=10, pady=10)
        
        # Botón para llamar al módulo CRUDPacientes.py
        Boton_Paciente = Button(Frame_Botones,text="Paciente",height=2,width=10,bg="green",fg="white",font=("Comic Sans", 17,"bold"), command=self.llamar_consulta_paciente)
        Boton_Paciente.grid(row=0, column=3, padx=10, pady=10)
        
        # Botón para llamar al módulo ConsultaLaboratorio.py
        Boton_Laboratorio = Button(Frame_Botones,text="Laboratorio",height=2,width=10,bg="green",fg="white",font=("Comic Sans", 17,"bold"), command=self.llamar_consulta_laboratorio)
        Boton_Laboratorio.grid(row=1, column=2, padx=10, pady=10)
        
        # Botón para llamar al módulo ConsultaServicio.py
        Boton_Servicio = Button(Frame_Botones,text="Servicio",height=2,width=10,bg="green",fg="white",font=("Comic Sans", 17,"bold"), command=self.llamar_consulta_servicio)
        Boton_Servicio.grid(row=1, column=3, padx=10, pady=10)
    
    def llamar_consulta_hospital(self):
        Ventana_Hospital = Toplevel(self.window)  # Crear una nueva ventana para la consulta del hospital
        app_Hospital = h.Hospital(Ventana_Hospital)  # Crear una instancia de la clase insertar
        Ventana_Hospital.transient(self.window)  # Hacer que la ventana hija esté encima de la ventana principal
        Ventana_Hospital.grab_set()  # Bloquear la ventana principal hasta que se cierre la ventana hija
        
    def llamar_consulta_medico(self):
        Ventana_Medico = Toplevel(self.window)  # Crear una nueva ventana para la consulta del medico
        app_Medico = m.Medico(Ventana_Medico)  # Crear una instancia de la clase insertar
        Ventana_Medico.transient(self.window)  # Hacer que la ventana hija esté encima de la ventana principal
        Ventana_Medico.grab_set()  # Bloquear la ventana principal hasta que se cierre la ventana hija
        
    def llamar_consulta_paciente(self):
        Ventana_Paciente = Toplevel(self.window)  # Crear una nueva ventana para la consulta del paciente
        app_Paciente = p.Paciente(Ventana_Paciente)  # Crear una instancia de la clase insertar
        Ventana_Paciente.transient(self.window)  # Hacer que la ventana hija esté encima de la ventana principal
        Ventana_Paciente.grab_set()  # Bloquear la ventana principal hasta que se cierre la ventana hija
        
    def llamar_consulta_laboratorio(self):
        Ventana_Paciente = Toplevel(self.window)  # Crear una nueva ventana para la consulta del paciente
        app_Paciente = l.Laboratorio(Ventana_Paciente)  # Crear una instancia de la clase insertar
        Ventana_Paciente.transient(self.window)  # Hacer que la ventana hija esté encima de la ventana principal
        Ventana_Paciente.grab_set()  # Bloquear la ventana principal hasta que se cierre la ventana hija

    def llamar_consulta_servicio(self):
        Ventana_Paciente = Toplevel(self.window)  # Crear una nueva ventana para la consulta del paciente
        app_Paciente = s.Servicio(Ventana_Paciente)  # Crear una instancia de la clase insertar
        Ventana_Paciente.transient(self.window)  # Hacer que la ventana hija esté encima de la ventana principal
        Ventana_Paciente.grab_set()  # Bloquear la ventana principal hasta que se cierre la ventana hija

        
if __name__ == "__main__":
    Ventana_Base = Tk()
    app = Base(Ventana_Base)
    Ventana_Base.mainloop()
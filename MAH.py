import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import Database 
from Database import *
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class FormularioArticulos():
    def __init__(self):
        self.articulo1=Database.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.iconbitmap(resource_path('artpoll.ico'))
        self.ventana1.title("Archivo Historico")
        self.ventana1.resizable(False, False)
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_datos()
        self.consulta_por_dato()
        self.listado_datos()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_datos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de registros")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Registro")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label3=ttk.Label(self.labelframe1, text="Id : ")        
        self.label3.grid(column=0, row=0, padx=4, pady=4, sticky="E")
        self.idcarga=tk.StringVar()
        self.entryid=ttk.Entry(self.labelframe1, textvariable=self.idcarga)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Nombre : ")        
        self.label2.grid(column=0, row=1, padx=4, pady=4, sticky="E")
        self.namecarga=tk.StringVar()
        self.entryname=ttk.Entry(self.labelframe1, textvariable=self.namecarga)
        self.entryname.grid(column=1, row=1, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Apellidos : ")        
        self.label2.grid(column=0, row=2, padx=4, pady=4, sticky="E")
        self.lastnamecarga=tk.StringVar()
        self.entrylastname=ttk.Entry(self.labelframe1, textvariable=self.lastnamecarga)
        self.entrylastname.grid(column=1, row=2, padx=4, pady=4)
        self.label1=ttk.Label(self.labelframe1, text="Fecha : ")
        self.label1.grid(column=0, row=3, padx=4, pady=4, sticky="E")
        self.birthdatecarga=tk.StringVar()
        self.entrydate=ttk.Entry(self.labelframe1, textvariable=self.birthdatecarga)
        self.entrydate.grid(column=1, row=3, padx=4, pady=4)
        self.label1=ttk.Label(self.labelframe1, text="Archivo : ")
        self.label1.grid(column=0, row=4, padx=4, pady=4, sticky="E")
        self.filecarga=tk.StringVar()
        self.entryfile=ttk.Entry(self.labelframe1, textvariable=self.filecarga)
        self.entryfile.grid(column=1, row=4, padx=4, pady=4)
        self.boton1=tk.Button(self.labelframe1, text="Volver", width=8, bd=5, background = "green", 
                                  fg = "white", cursor='hand2', command=self.volver)
        self.boton1.grid(column=0, row=5, padx=4, pady=4)
        self.boton1=tk.Button(self.labelframe1, text="Agregar", width=8, bd=5, background = "green", 
                                  fg = "white", cursor='hand2', command=self.agregar)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)

    def volver(self):
        self.ventana1.withdraw()
        path = ("C:/Modulos/AMUHT.exe")
        print(path)
        os.system(path)
        self.ventana1.destroy()

    def agregar(self):
        datos=(self.idcarga.get(), self.namecarga.get(), self.lastnamecarga.get(), self.birthdatecarga.get(), self.filecarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.idcarga.set('')
        self.namecarga.set('')
        self.lastnamecarga.set('')
        self.birthdatecarga.set('')
        self.filecarga.set('')

    def consulta_por_dato(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por dato")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="id :")
        self.label1.grid(column=0, row=0, padx=4, pady=4, sticky="E")
        self.idconsult=tk.StringVar()
        self.entryid=ttk.Entry(self.labelframe2, textvariable=self.idconsult)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Nombre :")        
        self.label2.grid(column=0, row=1, padx=4, pady=4, sticky="E")
        self.nameconsult=tk.StringVar()
        self.nameout=ttk.Entry(self.labelframe2, textvariable=self.nameconsult, state="readonly")
        self.nameout.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Apellidos :")        
        self.label3.grid(column=0, row=2, padx=4, pady=4, sticky="E")
        self.lastnameconsult=tk.StringVar()
        self.phoneout=ttk.Entry(self.labelframe2, textvariable=self.lastnameconsult, state="readonly")
        self.phoneout.grid(column=1, row=2, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Fecha :")        
        self.label3.grid(column=0, row=3, padx=4, pady=4, sticky="E")
        self.birthdateconsult=tk.StringVar()
        self.phoneout=ttk.Entry(self.labelframe2, textvariable=self.birthdateconsult, state="readonly")
        self.phoneout.grid(column=1, row=3, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Archivo :")        
        self.label3.grid(column=0, row=4, padx=4, pady=4, sticky="E")
        self.fileconsult=tk.StringVar()
        self.phoneout=ttk.Entry(self.labelframe2, textvariable=self.fileconsult, state="readonly")
        self.phoneout.grid(column=1, row=4, padx=4, pady=4)
        self.boton1=tk.Button(self.labelframe2, text="Abrir", width=8, bd=5, background = "green", 
                                  fg = "white", command= self.abrirArchivo)
        self.boton1.grid(column=0, row=5, padx=4, pady=4)
        self.boton1=tk.Button(self.labelframe2, text="Consultar", width=8, bd=5, background = "green", 
                                  fg = "white", command= self.consultar)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)

    def abrirArchivo(self):
        path = (self.fileconsult.get())
        print(path)
        os.system(path)

    def consultar(self):
        datos=(self.idconsult.get(), )
        respuesta= self.articulo1.consulta(datos) 
        if respuesta:
            self.nameconsult.set(respuesta[0])
            self.lastnameconsult.set(respuesta[1])
            self.birthdateconsult.set(respuesta[2])
            self.fileconsult.set(respuesta[3])
            mb.showinfo("Información", "Información encontrada")
        else:
            self.nameconsult.set('')
            self.lastnameconsult.set('')
            self.birthdateconsult.set('')
            self.fileconsult.set('')
            mb.showinfo("Información", "No existe información con dicho Id")

    def listado_datos(self):
        self.pagina3 = tk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Filtrar consulta")
        self.labelframe3=tk.LabelFrame(self.pagina3, text="Consulta")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe3, text="Nombre completo:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.filtername=tk.StringVar()
        self.entryid=ttk.Entry(self.labelframe3, textvariable=self.filtername)
        self.entryid.grid(column=0, row=2, padx=4, pady=4)
        self.boton1=tk.Button(self.labelframe3, text="Filtrar dato", width=14, bd=5, background="green", 
                                  fg="white", command=self.filtrar)
        self.boton1.grid(column=0, row=3, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=4, padx=10, pady=10)

    def filtrar(self):
        datos=(self.filtername.get(), )
        respuesta=self.articulo1.recuperar_todos(datos)
        self.scrolledtext1.delete("1.0", tk.END)
        if len(respuesta)>0:        
            for fila in respuesta:
                self.scrolledtext1.insert(tk.END,"Id: "+str(fila[0])+"\nLast Name: "+fila[1]+
                                        "\nBirthdate: "+str(fila[2])+"\nPath: "+str(fila[3])+
                                        "\n\n")
                mb.showinfo("Información", "Información encontrada")
        else:
            mb.showinfo("Información", "No información con dicho nombre")
aplicacion1=FormularioArticulos()
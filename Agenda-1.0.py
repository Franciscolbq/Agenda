from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import datetime
"import mysql.connector"
import re

users = {"Fran":123,
        "Heber":333,
        "Flor":684,
        "Julian":632,
        "Fer":444
}
logins = 3
ingreso = False

while logins > 0 and ingreso == False:

    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario in users:

        try:

            if int(contraseña) == users[usuario]:
         
                agenda = Tk()
                agenda.title = ("Agenda")
                vari = StringVar()
                varip = StringVar()
                hoy = date.today()
                control = "[a-zA-Z]"
                control2 = "[0-9]"
                recordverif1 = StringVar()
                recordverif2 = StringVar()
                recordverif3 = StringVar()
                recordverif4 = StringVar()
                fverificado = "Valor verificado"
                fnoverificado = "Valor no verificado"
                comentario = StringVar()
         
                #Pannel de pestañas
                pestaña = ttk.Notebook(agenda)
                pestaña.grid(column=0, row=1)
                pestaña2 = ttk.Notebook(agenda)
                pestaña2.grid(column=0, row=9)
                p1 = ttk.Frame(pestaña)   
                p2 = ttk.Frame(pestaña)   
                p3 = ttk.Frame(pestaña)
                p4 = ttk.Frame(pestaña)
                p5 = ttk.Frame(pestaña)
                p6 = ttk.Frame(pestaña)
                pestaña.add(p1, text='Ingreso')
                pestaña.add(p2, text='Agregar')
                pestaña.add(p3, text='Modificar')
                pestaña.add(p4, text='Eliminar')
                pestaña.add(p5, text='Evento hoy')
                pestaña.add(p6, text='Aux')

                #Pestaña Ingreso (p1)

                Label(p1, text= hoy.strftime('%d/%m/%Y')).grid(row=1, column=1, sticky=N)
                Label(p1, text="Hoy es:").grid(row=1, column=0, sticky=N)
                Label(p1, text="Bienvenido: ").grid(row=0, column=0, sticky=N)

                e1 = Label(p1, textvariable = vari, padx =50, pady= 5)
                e1.grid(row=0, column=1)

                vari.set("")
                vari.set(usuario)
                
                #Pestaña Agregar (p2)

                Label(p2, text= hoy.strftime('%d/%m/%Y')).grid(row=0, column=1, sticky=N)
                Label(p2, text="Hoy es:").grid(row=0, column=0, sticky=N)
                Label(p2, text="Año:").grid(row=1, column=0, sticky=N)
                Label(p2, text="Mes:").grid(row=2, column=0, sticky=N)
                Label(p2, text="Día:").grid(row=3, column=0, sticky=N)
                Label(p2, text="Ingrese el recordatorio:").grid(row=4, column=0, sticky=N)
                
                #Caracteristica de campos.

                e2 = Entry(p2)
                e3 = Entry(p2)
                e4 = Entry(p2)
                e5 = Entry(p2)

                #Posicion de campos

                e2.grid(row=1, column=1)
                e3.grid(row=2, column=1)
                e4.grid(row=3, column=1)
                e5.grid(row=4, column=1)
                g1 = Label(p2, textvariable = recordverif1, padx =50, pady= 5)
                g1.grid(row=1, column=2)
                g2 = Label(p2, textvariable = recordverif2, padx =50, pady= 5)
                g2.grid(row=2, column=2)            
                g3 = Label(p2, textvariable = recordverif3, padx =50, pady= 5)
                g3.grid(row=3, column=2)
                g4 = Label(p2, textvariable = recordverif4, padx =50, pady= 5)
                g4.grid(row=4, column=2)

                #Agrega recordatorios.

                def alta():
                    if (re.match(control2,e2.get())):
                        recordverif1.set("Año verificado.")
                    else:
                        recordverif1.set("Ingresa un valor de año.")
                    if (re.match(control2,e3.get())):
                        recordverif2.set("Mes verificado.")
                    else:
                        recordverif2.set("Ingresa un valor de mes.")
                    if (re.match(control2,e4.get())):
                        recordverif3.set("Día verificado.")
                    else:
                        recordverif3.set("Ingresa un valor de día.")
                    if (re.match(control,e5.get())):
                        recordverif4.set("Recordatorio verificado.")
                    else:
                        recordverif4.set("Ingresa un recordatorio.")
                    try:
                        mibase = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        passwd = "",
                        database = "Agenda"
                        )        
                        micursor = mibase.cursor()
                        sql = "INSERT INTO Agenda (Fecha,Recordatorio) VALUES (%s,%s)"
                        dato1 = (date(int(e2.get()),int(e3.get()),int(e4.get())),str(e5.get()))
                        micursor.execute(sql, dato1)
                        mibase.commit()
                        print(f"Se agrego el recordatorio el dia {e4.get()}/{e3.get()}/{e2.get()}.")
                    except:
                        print("La fecha ingresada es invalida.")
                
                b = Button(p2, text="Ingresar", command=alta, padx=5, pady=5)
                b.grid(row=6, column=1)

                #Pestaña modificar (p3)

                Label(p3, text= hoy.strftime('%d/%m/%Y')).grid(row=0, column=1, sticky=N)
                Label(p3, text="Hoy es:").grid(row=0, column=0, sticky=N)
                Label(p3, text="Año:").grid(row=1, column=0, sticky=N)
                Label(p3, text="Mes:").grid(row=2, column=0, sticky=N)
                Label(p3, text="Día:").grid(row=3, column=0, sticky=N)
                Label(p3, text="Ingrese modificación:").grid(row=4, column=0, sticky=N)

                #Caracteristica de campos.

                e6 = Entry(p3)
                e7 = Entry(p3)
                e8 = Entry(p3)
                e9 = Entry(p3)

                #Posicion de campos

                e6.grid(row=1, column=1)
                e7.grid(row=2, column=1)
                e8.grid(row=3, column=1)
                e9.grid(row=4, column=1)
                g1 = Label(p3, textvariable = recordverif1, padx =50, pady= 5)
                g1.grid(row=1, column=2)
                g2 = Label(p3, textvariable = recordverif2, padx =50, pady= 5)
                g2.grid(row=2, column=2)            
                g3 = Label(p3, textvariable = recordverif3, padx =50, pady= 5)
                g3.grid(row=3, column=2)
                g4 = Label(p3, textvariable = recordverif4, padx =50, pady= 5)
                g4.grid(row=4, column=2)

                def modificar():
                    if (re.match(control2,e6.get())):
                        recordverif1.set("Año verificado.")
                    else:
                        recordverif1.set("Ingresa un valor de año.")
                    if (re.match(control2,e7.get())):
                        recordverif2.set("Mes verificado.")
                    else:
                        recordverif2.set("Ingresa un valor de mes.")
                    if (re.match(control2,e8.get())):
                        recordverif3.set("Día verificado.")
                    else:
                        recordverif3.set("Ingresa un valor de día.")
                    if (re.match(control,e9.get())):
                        recordverif4.set("Recordatorio verificado.")
                    else:
                        recordverif4.set("Ingresa un recordatorio.")
                    try:
                        mibase = mysql.connector.connect(
                            host="localhost",  
                            user="root",  
                            passwd="",  
                            database="Agenda"
                        )
                        micursor = mibase.cursor()
                        datosec1 = (e9.get(),date(int(e6.get()),int(e7.get()),int(e8.get())))
                        sql = "UPDATE Agenda SET Recordatorio = %s WHERE Fecha = %s"
                        micursor.execute(sql,datosec1)
                        mibase.commit()
                        print(f"Se modifico el recordatorio de la fecha: {e8.get()}/{e7.get()}/{e6.get()}")
                    except:
                        print("La fecha ingresada es invalida.")
                g = Button(p3, text="Modificar", command=modificar, padx=5, pady=5)
                g.grid(row=6, column=1)

                #Pestaña borrar (p4)

                Label(p4, text= hoy.strftime('%d/%m/%Y')).grid(row=0, column=1, sticky=N)
                Label(p4, text="Hoy es:").grid(row=0, column=0, sticky=N)
                Label(p4, text="Año:").grid(row=1, column=0, sticky=N)
                Label(p4, text="Mes:").grid(row=2, column=0, sticky=N)
                Label(p4, text="Día:").grid(row=3, column=0, sticky=N)

                #Caracteristica de campos.

                e10 = Entry(p4)
                e11 = Entry(p4)
                e12 = Entry(p4)

                #Posicion de campos

                e10.grid(row=1, column=1)
                e11.grid(row=2, column=1)
                e12.grid(row=3, column=1)
                g1 = Label(p4, textvariable = recordverif1, padx =50, pady= 5)
                g1.grid(row=1, column=2)
                g2 = Label(p4, textvariable = recordverif2, padx =50, pady= 5)
                g2.grid(row=2, column=2)            
                g3 = Label(p4, textvariable = recordverif3, padx =50, pady= 5)
                g3.grid(row=3, column=2)
                
                #Borra recordatorio en la fecha ingresada.

                def borrar():
                    if (re.match(control2,e10.get())):
                        recordverif1.set("Año verificado.")
                    else:
                        recordverif1.set("Ingresa un valor de año.")
                    if (re.match(control2,e11.get())):
                        recordverif2.set("Mes verificado.")
                    else:
                        recordverif2.set("Ingresa un valor de mes.")
                    if (re.match(control2,e12.get())):
                        recordverif3.set("Día verificado.")
                    else:
                        recordverif3.set("Ingresa un valor de día.")
                    try:
                        mibase = mysql.connector.connect(
                            host="localhost",  
                            user="root",  
                            passwd="",  
                            database="Agenda"
                        )
                        micursor = mibase.cursor()
                        sql = "DELETE FROM Agenda WHERE Fecha = %s"
                        dato2 = (date(int(e10.get()),int(e11.get()),int(e12.get())),)
                        micursor.execute(sql, dato2)
                        mibase.commit()
                        print(f"Se borro de la lista la fecha: {e12.get()}/{e11.get()}/{e10.get()}")
                    except:
                        print("La fecha ingresada es invalida.")

                def borrartodo():
                    ordenborrartodo = input("¿Seguro que quiere borrar todo? S/N :")

                    if ordenborrartodo == "S" or ordenborrartodo == "s":

                        mibase = mysql.connector.connect(
                            host="localhost",  
                            user="root",  
                            passwd="",  
                            database="Agenda"
                        )
                        micursor = mibase.cursor()
                        sql = "DROP TABLE Agenda.Agenda"
                        micursor.execute(sql)
                        mibase.commit()
                        print("Agenda eliminada.")
                    
                    elif ordenborrartodo == "N" or ordenborrartodo == "n":
                        print("No se borro la agenda.")

                    else:
                        print("Ingreso invalido.")
                    

                e = Button(p4, text="Borrar", command=borrar, padx=5, pady=5)
                e.grid(row=6, column=1)

                h = Button(p4, text="Borrar todo", command=borrartodo, padx=5, pady=5)
                h.grid(row=9, column=1)

                #Pestaña Evento Hoy (p5)

                Label(p5, text= hoy.strftime('%d/%m/%Y')).grid(row=0, column=1, sticky=N)
                Label(p5, text="Hoy es:").grid(row=0, column=0, sticky=N)

                Label(p5, text="Evento hoy:").grid(row=3, column=0, sticky=N)
                e13 = Label(p5, textvariable = varip, padx =50, pady= 5)
                e13.grid(row=3, column=1)

                def proximorecordatorio():
                    try:
                        mibase = mysql.connector.connect(
                            host="localhost",  
                            user="root",  
                            passwd="",  
                            database="Agenda"
                        )
                        micursor = mibase.cursor()
                        sql = "SELECT Recordatorio FROM Agenda WHERE Fecha = %s"
                        dato3 = (date.today(),)
                        micursor.execute(sql,dato3)
                        resultado = micursor.fetchall()
                        varip.set("")
                        varip.set(resultado)
                        print(f"Se buscaron recordatorios el dia {hoy.strftime('%d/%m/%Y')}")
                    except:
                        print("La fecha ingresada es invalida.")

                c = Button(p5, text="Recordatorio hoy", command=proximorecordatorio, padx=5, pady=5)
                c.grid(row=6, column=1)

                #Aux (p6)

                Label(p6, text= hoy.strftime('%d/%m/%Y')).grid(row=0, column=1, sticky=N)

                def crearbd():
                    try:
                        mibase = mysql.connector.connect(   
                            host="localhost",  
                            user="root",  
                            passwd="")
                        micursor = mibase.cursor()
                        micursor.execute("CREATE DATABASE Agenda")
                        print("Base de datos creada.")
                    except:
                        print("La base de datos ya existe.")
                #Crea la tabla

                def crearagenda():
                    try:
                        mibase = mysql.connector.connect(   
                            host="localhost",  
                            user="root",  
                            passwd="",
                            database="Agenda")
                        micursor = mibase.cursor()
                        micursor.execute("CREATE TABLE Agenda(Fecha date NOT NULL,Recordatorio TEXT NOT NULL)")
                        print("Tabla creada.")
                    except:
                        print("La tabla ya existe.")

                d = Button(p6, text="Crear BD", command=crearbd, padx=5, pady=5)
                d.grid(row=2, column=0)

                f = Button(p6, text="Crear Tabla", command=crearagenda, padx=5, pady=5)
                f.grid(row=2, column=2)

                agenda.mainloop()

                ingreso = True
            
            else:
                print("Contraseña incorrecta.")
                logins -= 1
        except:
            print("Contraseña incorrecta.\nIngrese una contraseña numerica")
            logins -= 1
    else:
        print("Usuario inexistente.")
        logins -= 1

if logins == 0:
    print("Acceso denegado.")
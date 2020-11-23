from __future__ import print_function
from PIL import ImageTk, Image
from CaptureImage import captureImage
import tkinter as tk


class winInterface():
    win = None
    cadena = ""
    labelImage1 = None
    labelImage2 = None
    wOriginal = None
    hOriginal = None
    wFormatted = None
    hFormatted = None

    #####################################################################################################
    "Método constructor"

    def __init__(self):
        self.win = tk.Tk()
        self.Toplevel2 = tk.Toplevel(self.win)
        self.canvas2 = tk.Canvas(self.Toplevel2, borderwidth=5, background="blue")
        self.frame2 = tk.Frame(self.canvas2, width=500, height=900)
        self.scroll2 = tk.Scrollbar(self.Toplevel2, orient="vertical", command=self.canvas2.yview)
        self.scroll2H = tk.Scrollbar(self.Toplevel2, orient="horizontal", command=self.canvas2.xview)

        self.Toplevel1 = tk.Toplevel(self.win)
        self.canvas1 = tk.Canvas(self.Toplevel1, borderwidth=5, background="orange")
        self.frame1 = tk.Frame(self.canvas1, width=500, height=900)
        self.scroll1 = tk.Scrollbar(self.Toplevel1, orient="vertical", command=self.canvas1.yview)
        self.scroll1H = tk.Scrollbar(self.Toplevel1, orient="horizontal", command=self.canvas1.xview)

        self.winInter()
        self.win.mainloop()

    #####################################################################################################
    "Aquí se construye los diferentes elementos de la aplicación"

    def winInter(self):
        self.win.title("insert Image")
        self.win.geometry("600x400")
        self.win.resizable(1, 1)
        self.win.iconbitmap("ico\print_icon_159070.ico")
        self.win.config(bg="beige")
        ############################################################################################
        "Nivel superior 1: Abre imagen Formateada"
        self.Toplevel1.title("Imagen Formateada")
        self.canvas1.pack(side="left", fill="both", expand=1)
        self.frame1.pack(fill="both", expand=1)
        self.frame1.config(bg="white")
        self.canvas1.configure(yscrollcommand=self.scroll1.set, xscrollcommand=self.scroll1H.set)
        self.scroll1.pack(side="right", fill="y")
        self.scroll1H.pack(side="bottom", fill="x")
        self.canvas1.pack(side="left", fill="both", expand=True)
        self.canvas1.create_window((5, 5), window=self.frame1, anchor="nw")
        self.frame1.bind("<Configure>",
                         lambda event, canvas=self.canvas1: canvas.configure(scrollregion=canvas.bbox("all")))
        self.labelImage1 = tk.Label(self.frame1)
        self.labelImage1.pack(fill="both")
        self.labelImage1.pack(side=tk.LEFT, fill=tk.Y)

        ############################################################################################
        "Nivel superior 2: Abre imagen original"
        self.Toplevel2.title("Imagen Original")
        self.canvas2.pack(side="left", fill="both", expand=1)
        self.frame2.pack(fill="both", expand=1)
        self.frame2.config(bg="white")
        self.canvas2.configure(yscrollcommand=self.scroll2.set, xscrollcommand=self.scroll2H.set)
        self.scroll2.pack(side="right", fill="y")
        self.scroll2H.pack(side="bottom", fill="x")
        self.canvas2.pack(side="left", fill="both", expand=True)
        self.canvas2.create_window((5, 5), window=self.frame2, anchor="nw")
        self.frame2.bind("<Configure>",
                         lambda event, canvas=self.canvas2: canvas.configure(scrollregion=canvas.bbox("all")))
        self.labelImage2 = tk.Label(self.frame2)
        self.labelImage2.pack(fill="both")
        self.labelImage2.pack(side=tk.LEFT, fill=tk.Y)
        ############################################################################################
        "Botones"
        btn1 = tk.Button(self.win, text='Format Image', command=self.FormatImage).place(x=10, y=10)
        btn2 = tk.Button(self.win, text='Open Original Image', command=self.openOriginalImage).place(x=210, y=10)
        btn3 = tk.Button(self.win, text='Open Formatted Image', command=self.openFormattedImage).place(x=410, y=10)

        ############################################################################################
        "Etiquetas"
        tk.Label(text="IMAGEN ORIGINAL", background="beige", font=("Times New Roman", 14)).place(x=30, y=120)
        tk.Label(text="IMAGEN PROCESADA", background="beige", font=("Times New Roman", 14)).place(x=290, y=120)
        tk.Label(text="Ancho", background="beige", font=("Times New Roman", 14)).place(x=50, y=180)
        tk.Label(text="Alto", background="beige", font=("Times New Roman", 14)).place(x=130, y=180)
        tk.Label(text="Ancho", background="beige", font=("Times New Roman", 14)).place(x=310, y=180)
        tk.Label(text="Alto", background="beige", font=("Times New Roman", 14)).place(x=390, y=180)
        self.win.mainloop()

    #####################################################################################################
    "Metodo que invoca a CaptureImage para formatear imagen"

    @staticmethod
    def FormatImage():
        x = captureImage()
        x.sizeCalculation()
        x.orientation()
        x.checkImageLimits()

    #####################################################################################################
    "Método para abrir la imagen original"

    def openOriginalImage(self):
        img = Image.open("Original.jpg")
        imag = ImageTk.PhotoImage(img)
        self.labelImage2.configure(image=imag)
        self.labelImage2.image = imag
        self.widthOriginal = img.size[0]
        self.heightOriginal = img.size[1]
        self.wOriginal = tk.Label(self.win, text=self.widthOriginal, background="beige",
                                  font=("Times New Roman", 14)).place(x=50, y=200)
        self.hOriginal = tk.Label(self.win, text=self.heightOriginal, background="beige",
                                  font=("Times New Roman", 14)).place(x=130, y=200)
        self.win.mainloop()
        return imag

    #####################################################################################################
    "Método para abrir la imagen formateada"

    def openFormattedImage(self):
        img = Image.open("result.jpg")
        imag = ImageTk.PhotoImage(img)
        self.labelImage1.configure(image=imag)
        self.labelImage1.image = imag
        self.widthFormatted = img.size[0]
        self.heightFormatted = img.size[1]
        self.wFormatted = tk.Label(self.win, text=self.widthFormatted, background="beige",
                                   font=("Times New Roman", 14)).place(x=310, y=200)
        self.hFormatted = tk.Label(self.win, text=self.heightFormatted, background="beige",
                                   font=("Times New Roman", 14)).place(x=390, y=200)
        self.win.mainloop()
        return imag


if __name__ == "__main__":
    winInterface()

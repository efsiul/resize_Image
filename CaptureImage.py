from tkinter import filedialog
from cv2 import *
import numpy as np


class captureImage():
    # caden=""
    orien = str
    height = int
    width = int
    hFormatted = int
    wFormatted = int
    newSheet = None

    #####################################################################################################
    "Método constructor de la clase"

    def __init__(self):
        # self.image = 'image/20131202amv-prensa-joan-barreda-marruecos-17.jpg'
        self.image = self.capture()
        self.orien = ""
        self.newSheet = np.full((796, 1123, 3), 255)

    #####################################################################################################
    "Método para abrir una ventana y seleccionar la imagen"

    def openImage(self):
        file = filedialog.askopenfilename(title="Abrir un fichero.")
        cadena = file.split("/")
        cadena = cadena[-2] + "/" + cadena[-1]
        return cadena

    #####################################################################################################
    "Método para capturar la imagen que se abrio, este lo vuelve arreglo"

    def capture(self):
        cadena = self.openImage()
        img = cv2.imread(cadena)
        self.img = img
        return img

    #####################################################################################################
    "Método para calcular las medidas de la imágen que se abrio previamente"

    def sizeCalculation(self):
        image = self.image
        sizeImag = []

        self.height = image.shape[0]
        self.width = image.shape[1]

        sizeImag.append(self.width)
        sizeImag.append(self.height)
        return (sizeImag)

    #####################################################################################################
    "Método para establecer la orientación de la imágen"

    def orientation(self):
        sizeImag = self.sizeCalculation()
        if sizeImag[0] > sizeImag[1]:
            self.orien = "horizontal"
        elif sizeImag[0] < sizeImag[1]:
            self.orien = "vertical"
        return self.orien

    #####################################################################################################
    "Método para formtear la imágen en caso de que se salga de las proporciones de la hoja A4"

    def checkImageLimits(self):
        image = self.image
        reduct = image
        res = np.array([image.shape])

        '''Aquí se calcula el porcentaje o la escala a la cual se reduce la imágen en caso de que sobre pase el 
        tamaño de la hoja A4, este factor se multiplicará posteriormente por las dimensiones de la imágen original 
        para obtener las nuevas dimensiones de tal forma que se conserve el ratio. 
        Para calcularlo, al 98% de las dimensiones de la imágen se le resta un cociente que corresponde a: 
        una resta en el númerador entre el la dimensión mas grande de la imágen original y el número 1123 que es 
        la dimensión más grande de la hoja, esta substracción dividida por la dimensión más grande de la imágen'''
        scalingWidth = (0.98 - ((self.width - 1123) / self.width))
        scalingHeight = (0.98 - ((self.height - 1123) / self.height))
        typeOrientation = self.orientation()

        if typeOrientation == "horizontal":
            # En caso de que la imagen sea horizontal se verifica si el ancho supera los 1123 pixeles, en ese caso se reduce proporcioalmente, de lo contrario se imprime la imagen normal
            if (self.width / 1123) > 1:
                # ancho y alto multiplicados por el  porcentaje al cual se va a reducir en el caso horizontal
                wid = int(self.width * scalingWidth)
                heig = int(self.height * scalingWidth)
                self.wFormatted = wid
                self.hFormatted = heig
                res = cv2.resize(reduct, (wid, heig), interpolation=cv2.INTER_AREA)
            else:
                res = image
                self.wFormatted = self.width
                self.hFormatted = self.height

        elif typeOrientation == "vertical":
            # En caso de que la imagen sea vertical se verifica si el alto supera los 1123 pixeles, en ese caso se reduce proporcioalmente, de lo contrario se imprime la imagen normal        elif typeOrientation == "vertical":
            if (self.height / 1123) > 1:
                wid = int(self.width * scalingHeight)
                heig = int(self.height * scalingHeight)
                self.wFormatted = wid
                self.hFormatted = heig
                res = cv2.resize(reduct, (wid, heig), interpolation=cv2.INTER_AREA)
            else:
                res = image
                self.wFormatted = self.width
                self.hFormatted = self.height
        cv2.imwrite("resultados/result.jpg", res)
        cv2.imwrite("resultados/Original.jpg", self.image)
        return res


if __name__ == '__main__':
    x = captureImage()
    x.orientation()
    x.sizeCalculation()
    x.checkImageLimits()

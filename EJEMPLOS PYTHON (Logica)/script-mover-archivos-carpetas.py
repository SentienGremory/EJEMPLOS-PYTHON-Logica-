from PIL import Image #libreria pillow (instalar)
import os #leer los archivos en la carpeta de descargas

downloadsFolder = "/Users/rocha/Downloads/" #definimos la carpeta donde se buscaran los archivos
picturesFolder = "/Users/rocha/Pictures/" #definimos a que carpeta iran las imagenes

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder): 
        name, extension = os.path.splitext(downloadsFolder + filename) 

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + filename)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp4"]:
            musicFolder = "/Users/rocha/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
            print(name + ": " + extension)



        if extension in [".docx", ".pptx", ".pdf"]:
            docuFolder = "/Users/rocha/Documents/" 
            os.rename(downloadsFolder + filename, docuFolder + filename)
            print(name + ": " + extension)





#if __name__ == "__main__": (aqui pregunta si el archivo que se esta ejecutando lo estamos ejecutando en la terminal)
    #for filename in os.listdir(downloadsFolder): iterar (checar) todos los archviso que se encuentran en esta carpeta, "filename" es una variable temporal y sirve para indicar todos los archivos en el directorio sin importar su tipo
        #name, extension = os.path.splitext(downloadsFolder + filename) aqui tomamos el nombre del arcihivo y su extension y luego se separa entre el nombre del arichivo y extension

        #if extension in [".jpg", ".jpeg", ".png"]: aqui se pregunta si es jpg png o jpeg
            #picture = Image.open(downloadsFolder + filename) permite mejorar la manipulacion del codigo
            #picture.save(picturesFolder + filename) aqui hara que se guarde la imagen en la carpeta q especificamos arriba, pcitures folder
            #os.remove(downloadsFolder + filename) aqui borrar las copias que se quedaron en downloads 
            #print(name + ": " + extension)

        #if extension in [".mp4"]:
            #musicFolder = "/Users/rocha/Music/"
            #os.rename(downloadsFolder + filename, musicFolder + filename)
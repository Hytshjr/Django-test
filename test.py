from PIL import Image
import csv
import numpy as np
from faker import Faker
import random
from tkinter import filedialog
import os

fake = Faker()

def generate_random_product():
    name = fake.word()
    description = fake.sentence()
    price = round(random.uniform(10, 50),2)
    stock = round(random.randint(0, 100),1)
    return [name, description, price, stock]

def create_csv(file_path, num_rows):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir el encabezado
        writer.writerow(['id', 'name', 'description', 'price', 'stock'])
        i = 1
        # Escribir filas de datos aleatorios
        for _ in range(num_rows):
            product = generate_random_product()
            product.insert(0, i)
            i = 1 + i
            writer.writerow(product)


def modify_image():
    directori = filedialog.askdirectory()
    file_names = os.listdir(directori)

    for file_name in file_names:
        file_path = directori+'/'+file_name
        print(file_path)
        image = cut_image(file_path)
        image.save(file_path)

        

    
def cut_image(path):
    imagen = Image.open(path)  # Reemplaza 'ruta_de_tu_imagen.jpg' con la ruta de tu imagen

    # Convertir la imagen a una matriz de numpy
    matriz_image = np.array(imagen)

    new_image = np.array(Image.fromarray(matriz_image).resize((matriz_image.shape[1], matriz_image.shape[1])))

    new_image = Image.fromarray(new_image.astype('uint8'))

    return new_image


if __name__ == "__main__":
    # file_path = 'productos.csv'
    # num_rows = 70  # Puedes cambiar esto al número de filas que desees
    # create_csv(file_path, num_rows)
    # print(f"Archivo CSV creado en: {file_path}")
    
    modify_image()

    
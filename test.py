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

def create_path_product(file_path, num_rows):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir el encabezado
        writer.writerow(['id', 'imagenpath', 'product_id'])
        i = 1

        directori = 'D://Backend//django//app_monolitic//static//images'
        file_names = os.listdir(directori)
        # Escribir filas de datos aleatorios
        for file in file_names:
            product = ['/static/images/'+file,i ]
            product.insert(0, i)
            i = 1 + i
            writer.writerow(product)

    
def create_product(file_path, num_rows):
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

# Modelos
# from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     address = models.CharField(max_length=255, blank=True, null=True)


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image_path = models.CharField(max_length=255)


# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50)


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

# Modelos fin


if __name__ == "__main__":
    file_path = 'productos.csv'
    num_rows = 70  # Puedes cambiar esto al número de filas que desees
    create_product(file_path, num_rows)
    print(f"Archivo CSV creado en: {file_path}")
    
    # modify_image()

    
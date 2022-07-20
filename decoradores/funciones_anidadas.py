"""
    Debemos considerar que las funciones anidadas dentro de 
    funcion_mayor no se ejecutan hasta que se llama a esta primera, 
    siendo muestra del scope o alcance de las funciones. 
    Si las llamamos obtendremos un error
"""


def funcion_mayor():
    print("Esta es una función mayor y su mensaje de salida.")

    def librerias():
        print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

    def frameworks():
        print("Algunos frameworks de Python son: Django, Dash y Flask.")

    frameworks()
    librerias()


if __name__ == '__main__':
    funcion_mayor()

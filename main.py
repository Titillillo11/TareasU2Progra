from coche import Coche

def main():
    coche1 = Coche("Toyota", "Corolla", 2015)
    coche2 = Coche("Ford", "Mustang", 2018)
    coche3 = Coche("Chevrolet", "Spark", 2020)

    coche1.mostrar_informacion()
    coche2.mostrar_informacion()
    coche3.mostrar_informacion()

    año_actual = 2024
    print(f"El {coche1.marca} {coche1.modelo} tiene {coche1.calcular_edad_del_coche(año_actual)} años.")
    print(f"El {coche2.marca} {coche2.modelo} tiene {coche2.calcular_edad_del_coche(año_actual)} años.")
    print(f"El {coche3.marca} {coche3.modelo} tiene {coche3.calcular_edad_del_coche(año_actual)} años.")

if __name__ == "__main__":
    main()

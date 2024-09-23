from circulo import Circulo

def main():
    circulo1 = Circulo(5)
    circulo2 = Circulo(10)
    circulo3 = Circulo(15)

    print(f"Círculo 1 (Radio: {circulo1.radio}) - Área: {circulo1.calcular_area():.2f}, Perímetro: {circulo1.calcular_perimetro():.2f}")
    print(f"Círculo 2 (Radio: {circulo2.radio}) - Área: {circulo2.calcular_area():.2f}, Perímetro: {circulo2.calcular_perimetro():.2f}")
    print(f"Círculo 3 (Radio: {circulo3.radio}) - Área: {circulo3.calcular_area():.2f}, Perímetro: {circulo3.calcular_perimetro():.2f}")

if __name__ == "__main__":
    main()

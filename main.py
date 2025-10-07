
from src.bmi.core import calcular_imc, classificar_imc, faixa_peso_ideal
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculadora de IMC (Python).")
    parser.add_argument("--peso", type=float, required=True, help="Peso em kg. Ex: 70.5")
    parser.add_argument("--altura", type=float, required=True, help="Altura em metros. Ex: 1.75")
    args = parser.parse_args()

    imc = calcular_imc(args.peso, args.altura)
    categoria = classificar_imc(imc)
    ideal = faixa_peso_ideal(args.altura)

    print(f"IMC: {imc}")
    print(f"Classificação: {categoria.name} (faixa {categoria.range})")
    print(f"Peso ideal para a altura {args.altura}m: {ideal[0]}kg a {ideal[1]}kg")

if __name__ == "__main__":
    main()

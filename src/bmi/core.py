
from dataclasses import dataclass

# Business rules / constants
MIN_HEIGHT_M = 0.5
MAX_HEIGHT_M = 2.5
MIN_WEIGHT_KG = 2.0
MAX_WEIGHT_KG = 500.0

@dataclass(frozen=True)
class BMICategory:
    name: str
    range: str

CATEGORIES = [
    (float("-inf"), 18.5, BMICategory("Abaixo do peso", "< 18.5")),            # Underweight
    (18.5, 25.0, BMICategory("Peso normal", "18.5–24.9")),                     # Normal
    (25.0, 30.0, BMICategory("Sobrepeso", "25.0–29.9")),                       # Overweight
    (30.0, 35.0, BMICategory("Obesidade I", "30.0–34.9")),                     # Obesity I
    (35.0, 40.0, BMICategory("Obesidade II", "35.0–39.9")),                    # Obesity II
    (40.0, float("inf"), BMICategory("Obesidade III", ">= 40.0")),             # Obesity III
]

def validate_inputs(peso_kg: float, altura_m: float) -> None:
    """
    Regras de validação:
    - peso e altura devem ser números reais (float) > 0
    - altura entre 0.5m e 2.5m (inclusivo nas bordas)
    - peso entre 2kg e 500kg (inclusivo nas bordas)
    """
    if not isinstance(peso_kg, (int, float)) or not isinstance(altura_m, (int, float)):
        raise ValueError("Peso e altura devem ser números (int/float).")
    if peso_kg <= 0 or altura_m <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")
    if not (MIN_HEIGHT_M <= altura_m <= MAX_HEIGHT_M):
        raise ValueError(f"Altura deve estar entre {MIN_HEIGHT_M}m e {MAX_HEIGHT_M}m.")
    if not (MIN_WEIGHT_KG <= peso_kg <= MAX_WEIGHT_KG):
        raise ValueError(f"Peso deve estar entre {MIN_WEIGHT_KG}kg e {MAX_WEIGHT_KG}kg.")

def calcular_imc(peso_kg: float, altura_m: float, *, casas_decimais: int = 2) -> float:
    """
    IMC = peso_kg / (altura_m ** 2)
    - Retorna arredondado para 'casas_decimais' (padrão = 2).
    """
    validate_inputs(peso_kg, altura_m)
    imc = peso_kg / (altura_m ** 2)
    return round(imc, casas_decimais)

def classificar_imc(imc: float) -> BMICategory:
    """
    Classifica o IMC segundo faixas (OMS). Fronteiras seguem convenção:
    - Faixas [a, b) até a última, que é [40, +inf)
    """
    if not isinstance(imc, (int, float)):
        raise ValueError("IMC deve ser numérico.")
    if imc < 0:
        raise ValueError("IMC não pode ser negativo.")
    for lower, upper, cat in CATEGORIES:
        if lower <= imc < upper:
            return cat
    # teórico: não alcançado devido aos limites estabelecidos
    return CATEGORIES[-1][2]

def faixa_peso_ideal(altura_m: float, *, casas_decimais: int = 2) -> tuple[float, float]:
    """
    Para IMC 'saudável' (18.5 a 24.9), calcula a faixa de peso ideal com base na altura.
    Retorna tupla (min_kg, max_kg) arredondada.
    """
    validate_inputs(MIN_WEIGHT_KG, altura_m)  # valida apenas altura dentro dos limites
    min_kg = 18.5 * (altura_m ** 2)
    max_kg = 24.9 * (altura_m ** 2)
    return (round(min_kg, casas_decimais), round(max_kg, casas_decimais))

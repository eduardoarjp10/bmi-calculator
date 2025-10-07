
import math
import pytest
from src.bmi.core import (
    calcular_imc, classificar_imc, faixa_peso_ideal,
    validate_inputs, MIN_HEIGHT_M, MAX_HEIGHT_M, MIN_WEIGHT_KG, MAX_WEIGHT_KG
)

def test_calcular_imc_happy_path():
    assert calcular_imc(70, 1.75) == 22.86  # 70 / 1.75^2 = 22.857...

@pytest.mark.parametrize("peso,altura,esperado", [
    (50, 1.70, "Abaixo do peso"),    # ~17.30
    (65, 1.70, "Peso normal"),       # ~22.49
    (80, 1.70, "Sobrepeso"),         # ~27.68
    (92, 1.70, "Obesidade I"),       # ~31.84
    (105, 1.70, "Obesidade II"),     # ~36.33
    (120, 1.70, "Obesidade III"),    # ~41.52
])
def test_classificar_imc_por_faixa(peso, altura, esperado):
    imc = calcular_imc(peso, altura)
    categoria = classificar_imc(imc)
    assert categoria.name == esperado

def test_classificar_imc_bordas():
    # fronteiras (18.5, 25, 30, 35, 40)
    for imc, esperado in [
        (18.49, "Abaixo do peso"),
        (18.50, "Peso normal"),
        (24.99, "Peso normal"),
        (25.00, "Sobrepeso"),
        (29.99, "Sobrepeso"),
        (30.00, "Obesidade I"),
        (34.99, "Obesidade I"),
        (35.00, "Obesidade II"),
        (39.99, "Obesidade II"),
        (40.00, "Obesidade III"),
        (55.00, "Obesidade III"),
    ]:
        assert classificar_imc(imc).name == esperado

@pytest.mark.parametrize("peso,altura,msg", [
    (0, 1.7, "maiores que zero"),
    (70, 0, "maiores que zero"),
    (-5, 1.7, "maiores que zero"),
    (70, -1, "maiores que zero"),
    ("70", 1.7, "números"),
    (70, "1.7", "números"),
    (70, 0.3, "Altura deve estar entre"),
    (70, 3.0, "Altura deve estar entre"),
    (1.0, 1.7, "Peso deve estar entre"),
    (800.0, 1.7, "Peso deve estar entre"),
])
def test_validate_inputs_erros(peso, altura, msg):
    with pytest.raises(ValueError) as e:
        validate_inputs(peso, altura)
    assert msg in str(e.value)

def test_faixa_peso_ideal():
    # Para 1.75m: min=18.5*h^2, max=24.9*h^2
    min_kg, max_kg = faixa_peso_ideal(1.75)
    assert min_kg == round(18.5 * (1.75**2), 2)
    assert max_kg == round(24.9 * (1.75**2), 2)

def test_calcular_imc_casas_decimais_configuravel():
    assert calcular_imc(70, 1.75, casas_decimais=3) == 22.857

def test_classificar_imc_valida_imc_negativo_e_tipo():
    with pytest.raises(ValueError):
        classificar_imc(-1)
    with pytest.raises(ValueError):
        classificar_imc("22.0")  # type: ignore

def test_limites_validos_de_altura_e_peso():
    # Testa nas bordas válidas
    assert calcular_imc(MIN_WEIGHT_KG, MIN_HEIGHT_M) > 0
    assert calcular_imc(MAX_WEIGHT_KG, MAX_HEIGHT_M) > 0

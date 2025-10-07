
# Calculadora de IMC (Python + Pytest)

Pequena aplicação que calcula o **IMC** (Índice de Massa Corporal), classifica o resultado segundo faixas da **OMS** e fornece a **faixa de peso ideal** para uma altura informada. O projeto inclui **testes unitários** com Pytest e instruções para gerar **relatório de cobertura** com `pytest-cov`.

## Como executar

### 1) Pré-requisitos
- Python 3.10+
- `pip` instalado

### 2) Instalar dependências
```bash
pip install -r requirements.txt
```

### 3) Rodar a aplicação (CLI)
```bash
python main.py --peso 70 --altura 1.75
```
Saída esperada (exemplo):
```
IMC: 22.86
Classificação: Peso normal (faixa 18.5–24.9)
Peso ideal para a altura 1.75m: 56.66kg a 76.41kg
```

### 4) Rodar os testes
```bash
pytest
```

### 5) Rodar testes **com cobertura**
```bash
pytest --cov=src --cov-report=term-missing
```
> Tire um print do relatório no terminal e anexe ao repositório (por exemplo em `docs/coverage.png`).  
> Dica: Para gerar HTML detalhado, rode:  
> ```bash
> pytest --cov=src --cov-report=html
> open htmlcov/index.html  # (ou seu navegador preferido)
> ```

---

## Estrutura do projeto
```
bmi-calculator/
├─ src/
│  └─ bmi/
│     ├─ __init__.py
│     └─ core.py
├─ tests/
│  └─ test_core.py
├─ main.py
├─ pytest.ini
├─ requirements.txt
└─ README.md
```

---

## Regras de Negócio Testadas

1. **Cálculo do IMC:** `IMC = peso_kg / (altura_m^2)` com arredondamento padrão para 2 casas decimais.  
2. **Classificação segundo faixas (OMS):**
   - Abaixo do peso: **IMC < 18.5**
   - Peso normal: **18.5 ≤ IMC < 25**
   - Sobrepeso: **25 ≤ IMC < 30**
   - Obesidade I: **30 ≤ IMC < 35**
   - Obesidade II: **35 ≤ IMC < 40**
   - Obesidade III: **IMC ≥ 40**
3. **Validação de entrada:**
   - `peso` e `altura` devem ser numéricos e **> 0**.
   - `altura` deve estar em **[0.5m, 2.5m]**.
   - `peso` deve estar em **[2kg, 500kg]**.
   - Mensagens de erro claras para entradas inválidas.
4. **Faixa de peso ideal** para a altura informada: retorna `(mín, máx)` correspondente a IMC de **18.5** a **24.9**.
5. **Configuração de arredondamento** opcional para o IMC (padrão 2 casas), permitindo precisão customizada.

---

## Cobertura esperada
Os testes incluem:
- **Caminhos felizes** (cálculo e classificação em diferentes faixas);
- **Testes de borda** nas fronteiras das faixas de IMC;
- **Validações de entrada** com diferentes mensagens de erro;
- **Cálculo do peso ideal** e **parâmetro de arredondamento**.

Com isso, é comum obter **cobertura alta (>95%)** no módulo `core.py`. Execute o comando de cobertura e anexe o print ao repositório.

---

## Publicação
1. Crie um repositório (GitHub/GitLab).
2. Faça o push deste diretório.
3. Inclua no repositório o **print** do relatório de cobertura gerado localmente (ex.: `docs/coverage.png`).

---

## Licença
MIT

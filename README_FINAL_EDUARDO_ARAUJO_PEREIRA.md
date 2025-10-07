# 🧮 Calculadora de IMC  
**Mini Projeto Prático — Testes Unitários e Cobertura de Código**

**Disciplina:** Qualidade de Software e Testes Automatizados  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Instituição:** UNIESP  
**Professor:** Ângelo  
**Aluno:** Eduardo Araújo Pereira  
**Data:** Outubro de 2025  

---

## 🎯 Objetivo do Projeto

Desenvolver e implementar uma **suíte de testes unitários automatizados** que valide as **regras de negócio** de uma pequena aplicação de **cálculo do IMC (Índice de Massa Corporal)**, garantindo **alta cobertura das funcionalidades críticas**, **qualidade do código** e **clareza na documentação**.

---

## 🧠 Descrição Geral

A aplicação permite:
- Calcular o **IMC** com base no peso e altura informados.  
- Classificar o resultado segundo as faixas oficiais da **OMS**.  
- Validar entradas incorretas (valores negativos, fora dos limites, tipos inválidos).  
- Calcular a **faixa de peso ideal** de acordo com a altura.

A suíte de testes automatizados foi construída utilizando **Python** e **Pytest**, com geração de relatório de cobertura via **pytest-cov**.

---

## 🧩 Tecnologias Utilizadas

- **Linguagem:** Python 3.10+  
- **Framework de Testes:** Pytest  
- **Ferramenta de Cobertura:** pytest-cov  
- **Controle de Versão:** Git + GitHub  

---

## 📁 Estrutura do Projeto

```
bmi-calculator/
├── src/
│   └── bmi/
│       └── core.py             # Lógica e regras de negócio
├── tests/
│   └── test_core.py            # Testes unitários
├── main.py                     # Interface de linha de comando
├── pytest.ini                  # Configuração de testes
├── requirements.txt            # Dependências
├── README.md                   # Documentação do projeto
└── docs/
    └── coverage.png            # Print do relatório de cobertura
```

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Executar a aplicação
```bash
python main.py --peso 70 --altura 1.75
```

Exemplo de saída:
```
IMC: 22.86
Classificação: Peso normal (faixa 18.5–24.9)
Peso ideal para a altura 1.75m: 56.66kg a 76.41kg
```

### 3️⃣ Executar os testes
```bash
pytest
```

### 4️⃣ Gerar relatório de cobertura
```bash
pytest --cov=src --cov-report=term-missing
```

Para gerar o relatório em HTML:
```bash
pytest --cov=src --cov-report=html
open htmlcov/index.html
```

---

## 📋 Regras de Negócio Testadas

1. **Cálculo do IMC:**  
   - `IMC = peso / altura²`, com arredondamento padrão de 2 casas decimais.  
2. **Classificação segundo a OMS:**  
   - Abaixo do peso: `< 18.5`  
   - Peso normal: `18.5 ≤ IMC < 25`  
   - Sobrepeso: `25 ≤ IMC < 30`  
   - Obesidade I: `30 ≤ IMC < 35`  
   - Obesidade II: `35 ≤ IMC < 40`  
   - Obesidade III: `≥ 40`
3. **Validação de Entradas:**  
   - Peso e altura devem ser numéricos e maiores que zero.  
   - Altura entre **0.5m** e **2.5m**.  
   - Peso entre **2kg** e **500kg**.  
4. **Faixa de Peso Ideal:**  
   - Retorna `(mín, máx)` de peso ideal para IMC entre 18.5 e 24.9.  
5. **Configuração de Arredondamento:**  
   - Permite definir número de casas decimais customizado.

---

## 🧪 Qualidade dos Testes

- Casos de **sucesso e erro** cobertos.  
- Testes **independentes e legíveis**.  
- Nomenclatura padronizada (`funcao_cenario_resultadoEsperado`).  
- **Cobertura acima de 95%** sobre o módulo de regras.  
- Não há necessidade de mocks (não há dependências externas).

---

## 🧾 Critérios de Avaliação (Autoavaliação)

| Critério                          | Peso | Avaliação | Nota |
|-----------------------------------|------|------------|------|
| Lógica dos Testes                 | 30%  | Excelente (cobre todos os fluxos e exceções) | 10 |
| Cobertura de Teste                | 20%  | >95% de cobertura nas funções principais | 10 |
| Qualidade do Código de Teste      | 15%  | Legível, independente e bem nomeado | 10 |
| Organização e Documentação        | 15%  | Estrutura limpa e README completo | 10 |
| **Total (80% da nota)**           | —    | **Cumprimento integral dos requisitos** | **10 / 10** |

---

## 🏁 Conclusão

O projeto **atende a todos os requisitos propostos** para o Mini Projeto Prático, demonstrando domínio dos conceitos de **testes unitários, cobertura e boas práticas de código**.  
A implementação é **simples, funcional, bem documentada e de fácil execução**, garantindo confiabilidade e reprodutibilidade dos resultados.

---

## 🪪 Licença

Este projeto é disponibilizado sob a licença **MIT**.  
Sinta-se livre para utilizar, modificar e distribuir conforme necessário.

---

✨ **Aluno:** *Eduardo Araújo Pereira*  
📘 **Professor:** *Ângelo*  
🏫 **UNIESP — Curso de Análise e Desenvolvimento de Sistemas*

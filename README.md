# <img src="https://i.pinimg.com/originals/03/6b/29/036b2969dcd09ae9d16515681632121a.gif" alt="Interface da Calculadora" width="70"> Calculadora de Proporcional 
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python) ![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-orange) ![Versão](https://img.shields.io/badge/Versão-v2.0-brightgreen) ![Licença](https://img.shields.io/badge/Licen%C3%A7a-Uso%20Pessoal-orange)

---

## 👋 Sobre o Programa

A **Calculadora de Proporcional** é um software desenvolvido em Python com **CustomTkinter** para calcular automaticamente o valor proporcional de mensalidades baseado nos dias de consumo. O objetivo do programa é automatizar e simplificar o cálculo proporcional de mensalidades, evitando erros manuais e agilizando o processo para pequenas empresas ou serviços que precisam calcular o consumo de clientes de forma rápida, precisa e prática. 

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x** – linguagem principal  
- **CustomTkinter** – interface gráfica moderna  
- **Pillow (PIL)** – manipulação de imagens  
- **datetime, math, webbrowser** – módulos nativos do Python

---

## ✨ Funcionalidades

- Calcular valor proporcional da mensalidade  
- Mostrar dias consumidos  
- Arredondamento simples e desconto de 10 centavos  
- Copiar texto pronto para área de transferência  
- Interface limpa com link para o GitHub do desenvolvedor

---

## 🚀 Modo de Instalação

1. Baixe o arquivo do instalador na aba **[Releases](https://github.com/miguelsfrds/Calc_Proporcional/releases/tag/V2.1)**.  
2. Execute o instalador (`CalculadoraProporcional_Setup.exe`).  
3. Siga as instruções na tela.  
4. Após a instalação, abra o programa pelo menu iniciar ou pelo atalho criado na área de trabalho.

### ⚙️ Para estudar ou modificar o código
1. Instale Python 3.x  
2. Instale dependências:

```bash
pip install customtkinter pillow
```
## 📄 Como funciona

1. **Informe os dados do cliente:**
   - Data de vencimento (`dd/mm`)  
   - Último dia de consumo (`dd/mm`)  
   - Valor da mensalidade (inteiro)

2. **O programa realiza os cálculos automaticamente:**
   - Calcula os dias consumidos a partir do dia seguinte ao vencimento  
   - Calcula o valor proporcional baseado em 30 dias  
   - Arredonda o valor:
     - Para cima se a parte decimal > 0,5  
     - Para baixo caso contrário  
   - Aplica desconto fixo de 10 centavos  

3. **Resultado exibido na tela:**
   - Valor proporcional da mensalidade  
   - Dias consumidos  
   - Valor do desconto  
   - Botão para copiar texto pronto, por exemplo:
   ```bash
   REFERENTE AOS 18 UTILIZADOS DO MES 10
   ```
---

## 📌 Contato

- GitHub: [miguelsfrds](https://github.com/miguelsfrds)  
- Versão do programa: v2.0  
- Para sugestões, melhorias ou reportar bugs, abra uma issue no GitHub.

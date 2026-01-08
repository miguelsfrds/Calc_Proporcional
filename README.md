# <img src="https://i.pinimg.com/originals/03/6b/29/036b2969dcd09ae9d16515681632121a.gif" alt="Interface da Calculadora" width="70"> Calculadora de Proporcional  

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter%20%7C%20Tkinter-orange)
![Versão](https://img.shields.io/badge/Versão-v2.2-brightgreen)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-Uso%20Pessoal-orange)

---

## 👋 Sobre o Programa

A **Calculadora de Proporcional** é um software desenvolvido em **Python**, criado para **calcular automaticamente o valor proporcional de mensalidades** com base nos dias efetivamente utilizados pelo cliente.

O objetivo do projeto é **automatizar e simplificar** um cálculo que normalmente é feito de forma manual, reduzindo erros e agilizando o processo para pequenas empresas, provedores de serviço ou uso pessoal.

Atualmente, o projeto conta com **duas versões**, permitindo melhor compatibilidade com diferentes tipos de computadores:

- 🖥️ **Versão moderna** — interface desenvolvida em **CustomTkinter**
- 💡 **Versão simples e leve** — feita com **Tkinter puro**, indicada para PCs antigos ou com baixo desempenho

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.11+**  
- **CustomTkinter** (versão moderna)  
- **Tkinter** (versão simples)  
- **Pillow (PIL)**  
- **datetime / math / webbrowser**

---

## ✨ Funcionalidades

- Cálculo proporcional automático  
- Suporte a cálculos entre meses diferentes  
- Exibição dos dias consumidos  
- Arredondamento simples  
- Aplicação de desconto fixo de 10 centavos  
- Botão para copiar texto pronto  
- Interface simples, direta e prática  

---

## 📦 Como Usar o Programa

> ⚠️ **Não é necessário instalar Python ou dependências.**  
> Basta baixar o executável da versão desejada.

🔽 **Baixe o programa pela página oficial de Releases:**  
👉 **[Releases](https://github.com/miguelsfrds/Calc_Proporcional/releases/tag/2.2)**

Na página de *Releases* você encontrará:
- 🖥️ **Versão moderna (CustomTkinter)**  
- 💡 **Versão simples e leve (Tkinter puro)**  

Basta baixar o arquivo desejado, extrair o `.zip` e executar o `.exe`.

> 💡 *Se o seu computador for antigo ou lento, prefira a versão simples.*

---

## 📄 Como Funciona o Cálculo

1. Informe:
   - Data de vencimento (`dd/mm`)
   - Último dia de consumo (`dd/mm`)
   - Valor da mensalidade (inteiro)

2. O programa:
   - Conta os dias consumidos a partir do dia seguinte ao vencimento  
   - Calcula o valor proporcional com base em 30 dias  
   - Arredonda o valor:
     - Para cima se a parte decimal > 0,5  
     - Para baixo caso contrário  
   - Aplica desconto fixo de **R$ 0,10**  

3. Resultado exibido na tela com opção de copiar o texto, exemplo:
   ```text
   REFERENTE AOS 18 UTILIZADOS DO MES 10

---

## 🧾 Licença

Este projeto é de **uso livre apenas para fins educacionais e pessoais**.  
A **redistribuição comercial, venda ou uso com fins lucrativos é proibida**, salvo com autorização prévia do autor.

---

## 📫 Contato

Em caso de dúvidas, sugestões ou feedbacks, entre em contato:

- 💌 **miguelferreirads458@gmail.com**  
- 🌐 [GitHub](https://github.com/miguelsfrds)

---

Feito com 💙 por **miguelsfrds**

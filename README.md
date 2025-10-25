# 🖨️ Automação de Impressão de Etiquetas

Este projeto automatiza a digitação e execução de códigos em um sistema desktop para **impressão de etiquetas**, a partir de uma planilha CSV.

## 🚀 Objetivo
Automatizar uma tarefa repetitiva e propensa a erros humanos: inserir manualmente dezenas (ou centenas) de códigos em um sistema fechado para gerar etiquetas.

Com este script, todo o processo é feito automaticamente, poupando tempo e garantindo consistência.

---

## 🧠 Tecnologias utilizadas
- **Python 3**
- **PyAutoGUI** — automação de mouse e teclado  
- **Tkinter** — exibição de janelas e mensagens  
- **Pandas** — leitura e manipulação de dados CSV  
- **CTypes** — checagem do estado do Caps Lock (Windows)

---

## ⚙️ Como funciona
1. Lê o arquivo `etiqueta.csv`, contendo a coluna `codigo`.
2. Exibe mensagens interativas (Tkinter) para iniciar ou cancelar o processo.
3. Verifica se o Caps Lock está ativado (e aguarda até ser desligado).
4. Simula o login no sistema com usuário e senha pré-definidos.
5. Digita cada código do CSV, confirma e adiciona a quantidade.
6. Finaliza com a confirmação do processo.

---

## 📂 Estrutura esperada do arquivo CSV

| codigo |
|:------:|
| ABC123 |
| XYZ789 |
| ...    |

> Certifique-se de que o arquivo `etiqueta.csv` está na mesma pasta do script.

---

## 🧰 Requisitos
Instale as dependências:
```bash
pip install pyautogui pandas

import pyautogui
import time
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import ctypes
import sys


VERSION = "1.1"

# Funções para exibir mensagens com versão
def msg_info(title, message):
    messagebox.showinfo(title, f"{message}\n\n{' ' * 30}Versão: {VERSION}")

def msg_error(title, message):
    messagebox.showerror(title, f"{message}\n\n{' ' * 30}Versão: {VERSION}")

def msg_warning(title, message):
    messagebox.showwarning(title, f"{message}\n\n{' ' * 30}Versão: {VERSION}")

def msg_question(title, message):
    return messagebox.askyesno(title, f"{message}\n\n{' ' * 30}Versão: {VERSION}")

# Verificar estado do Caps Lock
def is_caps_lock_on():
    return bool(ctypes.windll.user32.GetKeyState(0x14) & 0x0001)

# Configurar tempo de pausa do PyAutoGUI
pyautogui.PAUSE = 2

# Importar base de dados
try:
    tabela = pd.read_csv('etiqueta.csv')
    tabela.columns = tabela.columns.str.strip().str.lower()
    if 'codigo' not in tabela.columns:
        raise ValueError("A coluna 'codigo' não foi encontrada no arquivo CSV!")
except FileNotFoundError:
    msg_error("Erro", "Arquivo 'etiqueta.csv' não encontrado!")
    sys.exit()
except ValueError as e:
    msg_error("Erro", str(e))
    sys.exit()

# Mostrar aviso de versão antiga antes de começar
root = tk.Tk()
root.withdraw()
msg_info("Aviso Importante", "Olá, você está utilizando uma versão mais antiga porque o aplicativo inicial ocorreu um bug inesperado.")

# Perguntar se deseja iniciar
if not msg_question("Bem-vindo!", f"Deseja iniciar o processo de impressão de {len(tabela)} etiquetas?\n\n"):
    msg_info("Execução Cancelada", "A execução foi cancelada.\n")
    sys.exit()

# Avisar se o Caps Lock estiver ativado
if is_caps_lock_on():
    msg_warning("Aviso", "O Caps Lock está ativado! Desative-o antes de continuar.")
    while is_caps_lock_on():
        time.sleep(5)

# Simulação de login
pyautogui.click(x=372, y=743)
pyautogui.write('vend')
pyautogui.press('tab')
pyautogui.write('3431')
pyautogui.press('enter')
pyautogui.press('enter')

time.sleep(3)
pyautogui.click(x=352, y=128)

# Preenchimento automático de códigos
for codigo in tabela['codigo'].astype(str).str.upper():
    pyautogui.write(codigo)
    pyautogui.press('enter')
    pyautogui.write('1')
    pyautogui.press('f2')

time.sleep(2)
pyautogui.click(x=869, y=602)
pyautogui.press('enter')

msg_info("Processo Concluído", f"Todos os {len(tabela)} códigos foram executados com sucesso!\n")

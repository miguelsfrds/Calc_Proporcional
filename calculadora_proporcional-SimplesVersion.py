import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import math
import webbrowser
import sys, os


# --- Função para localizar o ícone ---
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# --- Lógica ---
def calcula_consumo():
    try:
        data_venc = entry_vencimento.get()
        data_cons = entry_consumo.get()
        valor_mensal = int(entry_mensalidade.get())

        ano = datetime.now().year

        dia_v, mes_v = map(int, data_venc.split("/"))
        dia_c, mes_c = map(int, data_cons.split("/"))

        vencimento = datetime(ano, mes_v, dia_v)

        if mes_c < mes_v:
            consumo = datetime(ano + 1, mes_c, dia_c)
        else:
            consumo = datetime(ano, mes_c, dia_c)

        inicio = vencimento + timedelta(days=1)
        dias = (consumo - inicio).days + 1

        if dias <= 0:
            resultado_var.set("⚠️ Datas inválidas.")
            return

        proporcional = (valor_mensal / 30) * dias

        resultado = math.ceil(proporcional) if proporcional % 1 > 0.5 else math.floor(proporcional)
        desconto = round((valor_mensal - resultado) - 0.10, 2)

        proximo_mes = vencimento.month + 1 if vencimento.month < 12 else 1

        texto = (
            f"O cliente utilizou {dias} dias.\n"
            f"Mensalidade {proximo_mes}: R${resultado}\n"
            f"Desconto: {desconto}"
        )

        texto_copia.set(f"REFERENTE AOS {dias} UTILIZADOS DO MES {proximo_mes}")
        resultado_var.set(texto)
        botao_copiar.config(state="normal")

    except Exception:
        resultado_var.set("⚠️ Formato inválido. Use dd/mm e valor inteiro.")


def copiar_texto():
    root.clipboard_clear()
    root.clipboard_append(texto_copia.get())
    root.update()
    messagebox.showinfo("Copiado", "Texto copiado para a área de transferência.")


def abrir_github(event=None):
    webbrowser.open("https://github.com/miguelsfrds")


# --- Interface ---
root = tk.Tk()
root.title("Calculadora de Proporcional")
root.geometry("500x420")
root.resizable(False, False)

# Ícone
icon = resource_path("calc_icon.ico")
if os.path.exists(icon):
    root.iconbitmap(icon)

# Fonte padrão
FONTE = ("Consolas", 12)
FONTE_TITULO = ("Consolas", 16, "bold")

# Container principal
frame = tk.Frame(root, padx=20, pady=15)
frame.pack(fill="both", expand=True)

# Título
tk.Label(frame, text="CALCULADORA DE PROPORCIONAL", font=FONTE_TITULO).grid(row=0, column=0, columnspan=2, pady=10)

# Entradas
tk.Label(frame, text="Data de vencimento (dd/mm):", font=FONTE).grid(row=1, column=0, sticky="w")
entry_vencimento = tk.Entry(frame, font=FONTE)
entry_vencimento.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Último dia de consumo:", font=FONTE).grid(row=2, column=0, sticky="w")
entry_consumo = tk.Entry(frame, font=FONTE)
entry_consumo.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Valor da mensalidade:", font=FONTE).grid(row=3, column=0, sticky="w")
entry_mensalidade = tk.Entry(frame, font=FONTE)
entry_mensalidade.grid(row=3, column=1, pady=5)

# Botões
tk.Button(frame, text="Calcular", font=FONTE, command=calcula_consumo).grid(row=4, column=0, columnspan=2, pady=10)

botao_copiar = tk.Button(frame, text="Copiar texto", font=FONTE, command=copiar_texto, state="disabled")
botao_copiar.grid(row=5, column=0, columnspan=2)

# Resultado
resultado_var = tk.StringVar()
tk.Label(frame, textvariable=resultado_var, font=FONTE, justify="left", fg="green").grid(row=6, column=0, columnspan=2, pady=15)

texto_copia = tk.StringVar()

# Rodapé
rodape = tk.Frame(root)
rodape.pack(fill="x", pady=5)

tk.Label(rodape, text="v2.2", font=FONTE, fg="gray").pack(side="left", padx=10)

github = tk.Label(rodape, text="miguelsfrds", font=FONTE, fg="blue", cursor="hand2")
github.pack(side="right", padx=10)
github.bind("<Button-1>", abrir_github)

root.mainloop()

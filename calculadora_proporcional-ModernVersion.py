import customtkinter as ctk
from datetime import datetime, timedelta
import math
import webbrowser
import sys, os

# Função para localizar o ícone (funciona no .exe e no .py)
def resource_path(relative_path):
    """Obtém o caminho correto do arquivo mesmo dentro do executável"""
    try:
        base_path = sys._MEIPASS  # usado pelo PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# variável global para armazenar o botão de copiar
botao_copiar = None

def calcula_consumo():
    global botao_copiar
    try:
        # Captura os dados inseridos pelo usuário
        data_vencimento_cliente = entry_vencimento.get()
        data_consumo_cliente = entry_consumo.get()
        valor_mensalidade = int(entry_mensalidade.get())

        # Usa o ano atual para completar as datas
        ano_atual = datetime.now().year

        dia_venc, mes_venc = map(int, data_vencimento_cliente.split("/"))
        dia_cons, mes_cons = map(int, data_consumo_cliente.split("/"))

        data_vencimento = datetime(ano_atual, mes_venc, dia_venc)

        # Se o mês de consumo for menor, é no próximo ano
        if mes_cons < mes_venc:
            data_consumo = datetime(ano_atual + 1, mes_cons, dia_cons)
        else:
            data_consumo = datetime(ano_atual, mes_cons, dia_cons)


        # Começa a contagem a partir do dia seguinte ao vencimento
        inicio_consumo = data_vencimento + timedelta(days=1)
        dias_consumidos = (data_consumo - inicio_consumo).days + 1


        # Cálculo proporcional baseado em 30 dias fixos
        calc_proporcional = (valor_mensalidade / 30) * dias_consumidos
        parte_inteira = int(calc_proporcional)
        parte_decimal = calc_proporcional - parte_inteira

        # Ajusta o mês para o próximo (volta pra 1 se for dezembro)
        proximo_mes = data_vencimento.month + 1
        if proximo_mes > 12:
            proximo_mes = 1

        # Arredonda o valor de forma simples
        if parte_decimal > 0.5:
            resultado = math.ceil(calc_proporcional)
        else:
            resultado = math.floor(calc_proporcional)

        # Calcula o desconto com 10 centavos a menos
        desconto = (valor_mensalidade - resultado) - 0.10
        desconto = round(desconto, 2)

        # Texto de resultado
        resultado_text = (
            f"O cliente utilizou {dias_consumidos} dias.\n"
            f"O valor da mensalidade {proximo_mes} alterada ficará R${resultado}\n"
            f"Desconto de {desconto}"
        )

        # Texto para copiar
        copiar_text = f"REFERENTE AOS {dias_consumidos} UTILIZADOS DO MES {proximo_mes}"

        # Atualiza o texto na tela
        resultado_label.configure(text=resultado_text, text_color="green")

        # Função de copiar texto
        def copia_texto_pronto(texto):
            interface.clipboard_clear()
            interface.clipboard_append(texto)
            interface.update()
            resultado_label.configure(text="✅ Texto copiado!", text_color="green")

        # Cria o botão de copiar, se ainda não existir
        if botao_copiar is None:
            botao_copiar = ctk.CTkButton(interface, text="Copiar texto pronto", command=lambda: copia_texto_pronto(copiar_text), font=fonte_padrao)
            botao_copiar.pack()
        else:
            # Se já existir, apenas atualiza o comando para copiar o novo texto
            botao_copiar.configure(command=lambda: copia_texto_pronto(copiar_text))

    except ValueError:
        # Mostra erro em vermelho se o formato estiver errado
        error = ("⚠️ Formato inválido! Use o formato dd/mm, ex: 20/09\n"
                 "ou coloque o valor da mensalidade inteiro (ex: 70)")
        resultado_label.configure(text=error, text_color="red")


# --- INTERFACE ---

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

interface = ctk.CTk()
interface.title("Calculadora de Proporcional")
interface.geometry("400x450")

# Ícone (deve estar na mesma pasta que o arquivo .py)
icon_path = resource_path("calc_icon.ico")
if os.path.exists(icon_path):
    interface.iconbitmap(icon_path)
else:
    print("⚠️ Ícone não encontrado:", icon_path)

fonte_padrao = ("Consolas", 14)
fonte_mensagem = ("Consolas", 12)

# Título da calculadora
texto_calculadora_proporcional = ctk.CTkLabel(interface, text="CALCULADORA DE PROPORCIONAL", font=("Consolas", 18, "bold"))
texto_calculadora_proporcional.pack(pady=20)

# Campos de entrada
entry_vencimento = ctk.CTkEntry(interface, placeholder_text="Data de vencimento (ex: 20/09)", font=fonte_padrao)
entry_vencimento.pack(pady=10, padx=20, fill="x")

entry_consumo = ctk.CTkEntry(interface, placeholder_text="Último dia de consumo (ex: 07/10)", font=fonte_padrao)
entry_consumo.pack(pady=10, padx=20, fill="x")

entry_mensalidade = ctk.CTkEntry(interface, placeholder_text="Valor da mensalidade", font=fonte_padrao)
entry_mensalidade.pack(pady=10, padx=20, fill="x")

# Botão principal
botao_calcula = ctk.CTkButton(interface, text="Calcular", command=calcula_consumo, font=fonte_padrao)
botao_calcula.pack()

# Exibição do resultado
resultado_label = ctk.CTkLabel(interface, text="", text_color="green", font=fonte_mensagem)
resultado_label.pack(pady=20)

# --- LINK DO GITHUB ---
def abrir_github(event=None):
    webbrowser.open("https://github.com/miguelsfrds")

link_github = ctk.CTkLabel(
    interface,
    text="miguelsfrds",
    font=("Consolas", 15),
    text_color="white",
    compound="left"
)
link_github.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
link_github.bind("<Button-1>", abrir_github)

# --- VERSÃO ---
versao_label = ctk.CTkLabel(
    interface,
    text="v2.2",
    font=("Consolas", 15),
    text_color="gray"
)
versao_label.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

interface.mainloop()

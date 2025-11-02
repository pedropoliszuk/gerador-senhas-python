import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            raise ValueError
        if tamanho < 8:
            messagebox.showerror("Erro", "O tamanho mínimo permitido é 8 caracteres.")
            return
        if tamanho > 20:
            messagebox.showerror("Erro", "O tamanho máximo permitido é 20 caracteres.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Digite um número inteiro positivo")
        return
    
    chars = string.ascii_letters + string.digits + "!@#$%&*()-_"
    senha = ''.join(secrets.choice(chars) for _ in range(tamanho))
    label_resultado.config(text=senha)
    pyperclip.copy(senha)
    messagebox.showinfo("Copiado!", "A senha foi copiada para a área de transferência!")
    


janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("300x150")

tk.Label(janela, text="Digite a quantidade de caracteres da senha (máx. 20):").pack(pady=5)

def somente_numeros(P):
    return P.isdigit() or P == ""

vcmd = janela.register(somente_numeros)

entry_tamanho = tk.Entry(janela, validate="key", validatecommand=(vcmd, "%P"))
entry_tamanho.pack(pady=5)

tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=5)
label_resultado = tk.Label(janela, text="", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

janela.mainloop()

import tkinter as tk
from tkinter import messagebox, scrolledtext
import uuid
import binascii
from Crypto.Cipher import AES

# Função para gerar KI
def gen_ki():
    return str(uuid.uuid4()).replace('-', '').upper()

# Função para calcular OPc
def calc_opc_hex(k_hex, op_hex):
    iv = binascii.unhexlify(16 * '00')
    ki = binascii.unhexlify(k_hex)
    op = binascii.unhexlify(op_hex)
    aes_crypt = AES.new(ki, mode=AES.MODE_CBC, IV=iv)
    data = op
    o_pc = xor_str(data, aes_crypt.encrypt(data))
    return binascii.hexlify(o_pc).decode('utf-8')

# Função auxiliar para realizar XOR entre strings
def xor_str(s, t):
    return bytes([_a ^ _b for _a, _b in zip(s, t)])

# Função para gerar OPc com base no OP e KI
def gen_opc(op, ki):
    return calc_opc_hex(ki, op)

# Função para gerar eKI
def aes_128_cbc_encrypt(key, text):
    IV = binascii.unhexlify('00000000000000000000000000000000')
    keyb = binascii.unhexlify(key)
    textb = binascii.unhexlify(text)
    encryptor = AES.new(keyb, AES.MODE_CBC, IV=IV)
    ciphertext = encryptor.encrypt(textb)
    return ciphertext.hex().upper()

def gen_eki(transport, ki):
    return aes_128_cbc_encrypt(transport, ki)

# Função para gerar as chaves
def generate_multiple_keys():
    op = op_entry.get()
    tk_key = tk_entry.get()
    num = num_entry.get()

    if not op or not tk_key or not num.isdigit():
        messagebox.showerror("Input Error", "Please provide OP, TK, and a valid number.")
        return
    
    num = int(num)
    results.delete(1.0, tk.END)  # Limpa a área de texto
    for i in range(num):
        ki = gen_ki()
        opc = gen_opc(op, ki)
        eki = gen_eki(tk_key, ki)
        results.insert(tk.END, f"KI: {ki}\nOPc: {opc}\neKI: {eki}\n{'-'*40}\n")

# Configurando a janela tkinter
root = tk.Tk()
root.title("CryptoKey Generator")

# Configuração de cores
background_color = "#1c559a"  # RGB(28, 85, 154) em hexadecimal
text_color = "white"

# Aplicar cor de fundo à janela principal
root.configure(bg=background_color)

# Criando os campos de entrada para OP, TK e número de chaves
tk.Label(root, text="Operator Key (OP):", bg=background_color, fg=text_color).grid(row=1, column=0, padx=10, pady=10)
op_entry = tk.Entry(root, width=70)
op_entry.grid(row=1, column=1, padx=0, pady=10)

tk.Label(root, text="Transport Key (TK):", bg=background_color, fg=text_color).grid(row=2, column=0, padx=10, pady=10)
tk_entry = tk.Entry(root, width=70)
tk_entry.grid(row=2, column=1, padx=0, pady=10)

tk.Label(root, text="Number of Keys:", bg=background_color, fg=text_color).grid(row=4, column=0, padx=10, pady=10)
num_entry = tk.Entry(root, width=70)
num_entry.grid(row=4, column=1, padx=0, pady=10)

# Botão para gerar as chaves
generate_button = tk.Button(root, text="Generate Multiple eKI", command=generate_multiple_keys, bg="#0d3c73", fg=text_color)
generate_button.grid(row=5, column=1, padx=10, pady=10)

# Área de texto para exibir os resultados
results = scrolledtext.ScrolledText(root, width=80, height=20, bg="#0d3c73", fg=text_color, insertbackground=text_color)
results.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Executa a aplicação tkinter
root.mainloop()
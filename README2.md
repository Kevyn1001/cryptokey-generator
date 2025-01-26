# CryptoKey Generator  

**CryptoKey Generator** é uma aplicação desenvolvida para gerar chaves criptográficas essenciais, como **KI (Key Identifier)**, **OPc (Operator Code derivado)** e **eKI (Encrypted Key Identifier)**. Essas chaves são amplamente utilizadas em operações de autenticação e comunicação segura em redes de telecomunicações.  

Este projeto foi baseado no repositório [kiopcgenerator](https://github.com/PodgroupConnectivity/kiopcgenerator) e expandido com uma interface gráfica amigável usando **Tkinter**, tornando o processo acessível e interativo.  

## **Table of Contents**  
- [Descrição](#descrição)  
- [Funcionalidades](#funcionalidades)  
- [Uso](#uso)    
- [Créditos](#créditos)  

---

## **Descrição**  

### **Chaves Suportadas:**  
1. **KI (Key Identifier):** Uma chave secreta única para cada assinante, usada na autenticação em redes de telecomunicações.  
2. **OPc (Operator Code derivado):** Derivado de **OP (Operator Key)** e **KI**, protege a chave OP contra exposições.  
3. **eKI (Encrypted Key Identifier):** Uma versão criptografada do KI para transporte seguro e armazenamento.  

### **Importância em Redes de Telecom:**  
- **Segurança:** Previne acessos não autorizados e protege dados confidenciais.  
- **Autenticação:** Garante que dispositivos legítimos sejam conectados à rede.  
- **Conformidade:** Atende a padrões e regulamentações internacionais de segurança.  

### **Destaques Técnicos:**  
- **Algoritmo AES (CBC):** Utilizado para encriptação com alta segurança.  
- **Interface gráfica com Tkinter:** Permite gerar chaves de forma simples e interativa.  
- **Geração de múltiplas chaves:** Configure parâmetros e crie várias chaves com um clique.  

---

## **Funcionalidades**  

- Geração de **KI** aleatório ou baseado em entrada do usuário.  
- Cálculo do **OPc** a partir do OP e KI.  
- Geração de **eKI** com base na Transport Key (TK).  
- Interface gráfica para configurar OP, TK e número de chaves.  
- Exibição organizada dos resultados na interface.  

---

## **Uso**  

1. Clone o repositório:  
   ```bash
   git clone https://github.com/Kevyn1001/cryptokey-generator.git
   cd CryptoKey-Generator
   ```

2. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:  
   ```bash
   python CryptoKey_Gen.py
   ```

4. Insira os parâmetros:  
   - **OP:** Operator Key (32 caracteres).  
   - **TK:** Transport Key (32 caracteres).  
   - **Número de chaves:** Quantidade de chaves que deseja gerar.  

---

## **Exemplo de Saída**  

```text
----------------------------------------
KI: C23BC0441B8F49FFAC7EBB31FA07DA9B
OPc: 231a2ab7860a3e7468e8cec6adc66911
eKI: AB966E53CA60A523C6B6D86C566D053E 
----------------------------------------  
```

---

## **Créditos**  

Este projeto foi desenvolvido com base no repositório [kiopcgenerator](https://github.com/PodgroupConnectivity/kiopcgenerator), criado pela equipe da **PodgroupConnectivity**.  


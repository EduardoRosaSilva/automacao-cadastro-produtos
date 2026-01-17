# 🤖 Automação de Cadastro de Produtos com Python

Este projeto foi desenvolvido para automatizar a tarefa repetitiva de cadastrar centenas de produtos em um sistema corporativo. Utilizando Python, o script lê uma base de dados e interage com a interface gráfica do sistema, reduzindo o tempo de operação e eliminando erros humanos.

## 🚀 Tecnologias Utilizadas
* **Python 3.10+**
* **Pandas:** Para manipulação e leitura da base de dados (CSV).
* **PyAutoGUI:** Para controle do mouse e teclado (RPA - Robotic Process Automation).
* **OpenPyXL:** Engine auxiliar para leitura de arquivos.

## ⚙️ Funcionalidades
1.  **Leitura de Dados:** Importa automaticamente a base `produtos.csv`.
2.  **Login Automático:** Acessa o sistema web da empresa.
3.  **Preenchimento Inteligente:** Itera sobre cada linha da planilha, preenche os campos (Código, Marca, Tipo, Custo, etc.) e submete o formulário.
4.  **Tratamento de Exceções:** Verifica campos vazios (como observações) antes de preencher.

## 📦 Como executar
1.  Clone o repositório.
2.  Instale as dependências:
    ```bash
    pip install pandas pyautogui openpyxl
    ```
3.  Execute o script:
    ```bash
    python app.py
    ```
    *(Nota: Durante a execução, não utilize o mouse/teclado, pois o PyAutoGUI assume o controle).*

## ⚠️ Nota sobre Resolução
Este script utiliza coordenadas de tela mapeadas para resolução **1920x1200**. Se executado em monitores diferentes, pode ser necessário recalibrar as coordenadas `x` e `y` nas funções de clique.

---
*Projeto desenvolvido durante o curso Python Impressionador.*

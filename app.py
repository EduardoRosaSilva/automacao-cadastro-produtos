import pyautogui
import time
import pandas as pd
import webbrowser  # Biblioteca nativa para abrir URLs de forma mais limpa
import sys

# Configurações globais
pyautogui.PAUSE = 0.5
URL_SISTEMA = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

def carregar_dados(arquivo):
    """Carrega o arquivo CSV e trata possíveis erros de leitura."""
    try:
        tabela = pd.read_csv(arquivo)
        print(f"Base de dados carregada com sucesso! {len(tabela)} produtos encontrados.")
        return tabela
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        sys.exit()

def login_sistema():
    """Abre o navegador e realiza o login."""
    print("Iniciando automação...")
    
    # Abrir navegador direto no link (mais robusto que digitar chrome)
    webbrowser.open(URL_SISTEMA)
    
    # Tempo de segurança para carregar o site (pode variar conforme internet)
    time.sleep(5) 
    
    # Como estamos usando PyAutoGUI, usamos coordenadas ou navegação por TAB.
    
    # Passo para garantir o foco no campo de email (ajuste a coordenada se mudar a tela)
    # Dica: Use pyautogui.position() para descobrir a posição no seu monitor
    pyautogui.click(x=1192, y=500) 
    
    pyautogui.write('meuemail@email.com')
    pyautogui.press('tab')
    pyautogui.write('minhasenha')
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    time.sleep(3) # Espera o login processar

def cadastrar_produtos(tabela):
    """Itera sobre a tabela e preenche os campos do formulário."""
    print("Iniciando cadastro de produtos...")
    
    for linha in tabela.index:
        # Clica no primeiro campo
        pyautogui.click(x=971, y=367)
        
        # Extrai dados
        codigo = tabela.loc[linha, 'codigo']
        marca = tabela.loc[linha, 'marca']
        tipo = tabela.loc[linha, 'tipo']
        categoria = tabela.loc[linha, 'categoria']
        preco = tabela.loc[linha, 'preco_unitario']
        custo = tabela.loc[linha, 'custo']
        obs = tabela.loc[linha, 'obs']

        # Preenchimento
        pyautogui.write(str(codigo))
        pyautogui.press('tab')
        pyautogui.write(str(marca))
        pyautogui.press('tab')
        pyautogui.write(str(tipo))
        pyautogui.press('tab')
        pyautogui.write(str(categoria))
        pyautogui.press('tab')
        pyautogui.write(str(preco))
        pyautogui.press('tab')
        pyautogui.write(str(custo))
        pyautogui.press('tab')
        
        if not pd.isna(obs):
            pyautogui.write(str(obs))
            
        pyautogui.press('tab')
        pyautogui.press('enter') # Enviar
        
        # Scroll para garantir que o formulário esteja visível para o próximo loop
        pyautogui.scroll(5000)

    print("Cadastro finalizado com sucesso!")

# --- Execução Principal ---
if __name__ == "__main__":
    base_de_dados = carregar_dados('produtos.csv')
    login_sistema()
    cadastrar_produtos(base_de_dados)
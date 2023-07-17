import requests
import time

def testar_conectividade(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Conexão com {url} bem-sucedida.")
        else:
            print(f"Não foi possível conectar-se a {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao conectar-se a {url}: {e}")

# Lista de 10 sites de notícias mais usados no Brasil
sites_noticias = [
    "https://www.globo.com",
    "https://www.uol.com.br",
    "https://www.folha.uol.com.br",
    "https://www.estadao.com.br",
    "https://www.gazetadopovo.com.br",
    "https://www.terra.com.br",
    "https://www.r7.com",
    "https://www.bbc.com/portuguese",
    "https://www.metropoles.com",
    "https://www.correiobraziliense.com.br"
]

contador = 0
while True:
    # Executar o teste para cada site de notícias
    for site in sites_noticias:
        testar_conectividade(site)

    contador += 1
    print(f"Execução {contador} concluída.")

    # Verificar se é uma execução de espera longa
    if contador % 12 == 0:
        tempo_espera = 1800  # 1800 segundos = 30 minutos
        print("Aguardando 30 minutos para reiniciar...")
    else:
        tempo_espera = 300  # 300 segundos = 5 minutos
        print("Aguardando 5 minutos para a próxima execução...")

    # Iniciar cronômetro regressivo
    for segundos_restantes in range(tempo_espera, 0, -1):
        minutos_restantes, segundos_restantes = divmod(segundos_restantes, 60)
        print(f"Tempo restante: {minutos_restantes:02d}:{segundos_restantes:02d}", end="\r")
        time.sleep(1)

    print()  # Pular linha após o cronômetro regressivo

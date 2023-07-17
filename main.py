import requests
from bs4 import BeautifulSoup
import time
import subprocess

def testar_conectividade(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Conexão com {url} bem-sucedida.")
            return response.text
        else:
            print(f"Não foi possível conectar-se a {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao conectar-se a {url}: {e}")
    return None

def exibir_notificacao(titulo):
    subprocess.run(["notify-send", "Notícia em destaque", titulo])

def extrair_noticia_destaque(html, url):
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')

        if "globo.com" in url:
            noticias_destaque = soup.find_all('div', class_='headline__container')
            if noticias_destaque:
                print("Notícias em destaque:")
                for noticia in noticias_destaque:
                    titulo = noticia.find('h2', class_='post__title').text.strip()
                    link = noticia.find('a', class_='post__link')['href']
                    print(f"┌{'─' * (len(titulo) + 2)}┐")
                    print(f"│ {titulo} │")
                    print(f"└{'─' * (len(titulo) + 2)}┘")
                    print(f"Link: {link}")
                    print()
                    exibir_notificacao(titulo)
            else:
                print("Não foi possível encontrar notícias em destaque.")

        elif "uol.com.br" in url:
            noticias_destaque = soup.find_all('article', class_='headlineMain section__grid__main__highlight__item')
            if noticias_destaque:
                print("Notícias em destaque:")
                for noticia in noticias_destaque:
                    titulo = noticia.find('h3', class_='title__element headlineMain__title').text.strip()
                    link = noticia.find('a', class_='hyperlink headlineMain__link')['href']
                    print(f"┌{'─' * (len(titulo) + 2)}┐")
                    print(f"│ {titulo} │")
                    print(f"└{'─' * (len(titulo) + 2)}┘")
                    print(f"Link: {link}")
                    print()
                    exibir_notificacao(titulo)
            else:
                print("Não foi possível encontrar notícias em destaque.")

        elif "folha.uol.com.br" in url:
            noticias_destaque = soup.find_all('a', class_='c-main-headline__url')
            if noticias_destaque:
                print("Notícias em destaque:")
                for noticia in noticias_destaque:
                    titulo = noticia.find('h2', class_='c-main-headline__title').text.strip()
                    link = noticia['href']
                    print(f"┌{'─' * (len(titulo) + 2)}┐")
                    print(f"│ {titulo} │")
                    print(f"└{'─' * (len(titulo) + 2)}┘")
                    print(f"Link: {link}")
                    print()
                    exibir_notificacao(titulo)
            else:
                print("Não foi possível encontrar notícias em destaque.")

        elif "estadao.com.br" in url:
            noticias_destaque = soup.find_all('div', class_='headline')
            if noticias_destaque:
                print("Notícias em destaque:")
                for noticia in noticias_destaque:
                    titulo = noticia.find('h2').text.strip()
                    link = noticia.find('a')['href']
                    print(f"┌{'─' * (len(titulo) + 2)}┐")
                    print(f"│ {titulo} │")
                    print(f"└{'─' * (len(titulo) + 2)}┘")
                    print(f"Link: {link}")
                    print()
                    exibir_notificacao(titulo)
            else:
                print("Não foi possível encontrar notícias em destaque.")

        elif "gazetadopovo.com.br" in url:
            noticias_destaque = soup.find_all('article', class_='c-item item-1 template-default no-image no-related h-wide pwl-standart has-caption')
            if noticias_destaque:
                print("Notícias em destaque:")
                for noticia in noticias_destaque:
                    titulo = noticia.find('h2', class_='title').text.strip()
                    link = noticia.find('a', class_='standart trigger-gtm')['href']
                    print(f"┌{'─' * (len(titulo) + 2)}┐")
                    print(f"│ {titulo} │")
                    print(f"└{'─' * (len(titulo) + 2)}┘")
                    print(f"Link: {link}")
                    print()
                    exibir_notificacao(titulo)
            else:
                print("Não foi possível encontrar notícias em destaque.")

        elif "terra.com.br" in url:
            noticias_destaque = soup.find_all('a', class_='card-news__text--title')
            if noticias_destaque:
                print("Notícias em destaque:")
                for noticia in noticias_destaque:
                    titulo = noticia.find('h3').text.strip()
                    link = noticia['href']
                    print(f"┌{'─' * (len(titulo) + 2)}┐")
                    print(f"│ {titulo} │")
                    print(f"└{'─' * (len(titulo) + 2)}┘")
                    print(f"Link: {link}")
                    print()
                    exibir_notificacao(titulo)
            else:
                print("Não foi possível encontrar notícias em destaque.")

        elif "bbc.com/portuguese" in url:
            noticias_destaque = soup.find_all('div', class_='bbc-14gzkm2 e718b9o0')
            if noticias_destaque:
                print("Notícias em destaque:")
                for noticia in noticias_destaque:
                    titulo = noticia.find('h3', class_='bbc-1whbtaf ea6by782').text.strip()
                    link = noticia.find('a')['href']
                    print(f"┌{'─' * (len(titulo) + 2)}┐")
                    print(f"│ {titulo} │")
                    print(f"└{'─' * (len(titulo) + 2)}┘")
                    print(f"Link: {link}")
                    print()
                    exibir_notificacao(titulo)
            else:
                print("Não foi possível encontrar notícias em destaque.")

        else:
            print(f"Não há lógica para extrair notícias em destaque do site: {url}.")
    else:
        print("Não há conteúdo HTML para analisar.")

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
    contador += 1
    print(f"Execução {contador} iniciada.")

    # Executar o teste e extrair notícias em destaque para cada site de notícias
    for site in sites_noticias:
        html = testar_conectividade(site)
        extrair_noticia_destaque(html, site)

    print(f"Execução {contador} concluída.")

    # Verificar se é uma execução de espera longa
    if contador % 12 == 0:
        tempo_espera = 1800  # 1800 segundos = 30 minutos
        print("Aguardando 30 minutos para reiniciar...")
    else:
        tempo_espera = 600  # 600 segundos = 10 minutos
        print("Aguardando 10 minutos para a próxima execução...")

    # Iniciar cronômetro regressivo
    for segundos_restantes in range(tempo_espera, 0, -1):
        minutos_restantes, segundos_restantes = divmod(segundos_restantes, 60)
        print(f"Tempo restante: {minutos_restantes:02d}:{segundos_restantes:02d}", end="\r")
        time.sleep(1)

    print()

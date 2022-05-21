from pip._vendor import requests
import json


def get_git(language):
    url = 'https://api.github.com/search/repositories?q=language:'+language # atribuindo a URL
    print(url) # printando a URL
    r = requests.get(url) # Gerando o get.
    json_crew = r.json()['items'] # Tratando os dados para JSON
    lista_repos = []
    for elem in json_crew:  # id, nome, url, dono, stats, watchers, forks, description, lenguage
        repos = {
            'id': elem["id"],
            'Nome': elem["name"],
            'url': elem["owner"]["url"],
            'fork': elem["forks"],
            'language': elem["language"],
            'Visualizações': elem["watchers_count"],
            'Estrela': elem["stargazers_count"],
        }


        lista_repos.append(repos)
        lista_repos.sort(key=lambda x: x["Estrela"], reverse=True) # Não precisaria do lambda mas é sempre legal
    return lista_repos

print(get_git('python'))
 


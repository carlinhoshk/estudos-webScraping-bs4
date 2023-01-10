import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=desenvolvedor+java&biw=958&bih=919&ei=_eq8Y5rkFemH1sQPu5GI4AM&uact=5&oq=linkedin+vagas&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzILCAAQgAQQsQMQgwEyBQgAEIAEMggIABCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgAEEc6EQguEIAEELEDEIMBEMcBENEDSgQIQRgASgQIRhgAUNUCWLwJYLQLaABwAngAgAFkiAGjBJIBAzUuMZgBAKABAcgBCMABAQ&sclient=gws-wiz-serp&ibp=htl;jobs&sa=X&ved=2ahUKEwip3KjGlrz8AhVmrJUCHadzCZUQutcGKAB6BAgUEAM#fpstate=tldetail&htivrt=jobs&htidocid=PNXoYaJ0TZgAAAAAAAAAAA%3D%3D'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

trabalhos = soup.find_all('div', class_='gws-plugins-horizon-jobs__tl-lif')
trabalho = trabalhos[2]
nome = trabalho.find('div', class_='BjJfJf PUpOsf')

print(nome)
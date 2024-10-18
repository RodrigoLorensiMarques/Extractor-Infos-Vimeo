
from dic import dicionario_vimeo
import pprint #Biblioteca Pprint apenas para melhor visualização dos dados.


Videos=[]

Data= dicionario_vimeo['data']
PrimeiroItem=Data[0]


for item in Data:
    Downloads= item['download']

    Quali_540= ''
    Quali_720=''
    Quali_1080=''

    for DicionarioDownload in Downloads:
        if DicionarioDownload['rendition'] =='540p':
            Quali_540= DicionarioDownload['link']
        
        if DicionarioDownload['rendition'] =='720p':
            Quali_720= DicionarioDownload['link']

        if DicionarioDownload['rendition'] =='1080p':
            Quali_1080= DicionarioDownload['link']   

        URI=item['uri']
        Nome=item['name']
        Duracao=item['duration']
   

    dict_Videos= {'uri': URI, 'nome': Nome, 'duracao': Duracao, 'link540p': Quali_540, 'link720p': Quali_720, 'link1080p': Quali_1080}

    Videos.append(dict_Videos)


pprint.pprint (Videos)

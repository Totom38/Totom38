import requests
import json

url = 'https://sherpas.com/t/etudiant-en-ecole-dingenieur-donne-cours-de-mathematiques-et-dinformatique-en-ligne-et-sur-evry#teacher-ratings'

réponse = str(requests.get(url).content.decode('utf-8'))
réponse = réponse[réponse.find('"reviews"')+10:réponse.find('"subjects"')-1:]
réponse = sorted(json.loads(réponse), key=lambda x: len(x['comment']), reverse=True)

with open('reviews.json', 'w', encoding='utf-8') as f:
    json.dump(réponse, f, indent=4, ensure_ascii=False)
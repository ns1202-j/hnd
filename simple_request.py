import requests


query = {'lat':'45','lon':'180'}
#response = requests.get('https://192.168.11.41/nova/consulta1.php', params = query)
#response = requests.get('https://xkcd.com/353/')
response = requests.get('http://192.168.11.41/nova/consulta1.php')

print (response.text)

response = requests.post('http://192.168.11.41/nova/postprueba.php',data = {'foo2':'bar2'})



print (response.text)

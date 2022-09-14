import requests
#
if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
    
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])
        
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
#Script de python que consulta el api de pokemon 
# para listar los nombres de pokemon pero se le agrego
# interacción para que listaras más pokemons segun se vaya requiriendo.
# Contribuyo: <Angel Gael Villegas Rocha>
# Fecha: < 13/09/2022>

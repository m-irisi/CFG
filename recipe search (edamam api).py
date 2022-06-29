import requests
from pprint import pprint

def recipe_search(ingredient):
    app_id = 'dd0a9504'
    app_key = '03de3442e25326b7910a0458023088ca'
    result = requests.get(
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    ) 
    
    data = result.json()
    pprint(data)
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print(recipe['mealType'])
        print()

run()
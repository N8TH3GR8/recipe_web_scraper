from bs4 import BeautifulSoup
import requests


def recipe_scraper(recipe_url):
    res = None
    try:
        res = requests.get(recipe_url)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        print('\nPlease refresh the page and try again.')
        exit()
    soup = BeautifulSoup(res.text, 'html.parser')
    ingredients = soup.find_all(itemprop='recipeIngredient')
    ingredients = [i.text for i in ingredients]
    directions = []
    counter = 1
    for d in soup.find(itemprop='recipeInstructions').text.split('\n'):
        if not (d.isspace() or d == ''):
            directions.append(str(counter) + '. ' + d + '\n')
            counter += 1
    try:
        prep_time = soup.find(itemprop='prepTime').text
    except AttributeError:
        prep_time = 'unlisted'
    try:
        cook_time = soup.find(itemprop='cookTime').text
    except AttributeError:
        cook_time = 'unlisted'
    print('INGREDIENTS:')
    for i in ingredients:
        print(i)
    print('\nDIRECTIONS:\n')
    for i in directions:
        print(i)
    print('PREP TIME: ' + prep_time)
    print('COOK TIME: ' + cook_time)


recipe_scraper('https://www.allrecipes.com/recipe/19368/chucks-favorite-mac-and-cheese/')

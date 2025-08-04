import jmespath
import json

def search_in_json(word_for_search, name_file):
    with open(f'../{name_file}', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        result = jmespath.search(f'people[*].{word_for_search}', json_data)
    return result
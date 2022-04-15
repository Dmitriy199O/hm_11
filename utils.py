import json

DATA = []


def load_candidates_from_json(path='candidates.json'):
    global DATA
    with open(path, 'r', encoding='UTF-8') as file:
        DATA = json.load(file)

    return DATA


def get_candidate_by_id(user_id):
    for candidate in DATA:
        if candidate['id'] == user_id:
            return {
                'name': candidate["name"],
                'position': candidate["position"],
                'picture': candidate["picture"],
                'skills': candidate["skills"],
            }
    return {'not found'}


def get_candidates_by_name(candidate_name):
    return [candidate for candidate in DATA if candidate_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in DATA:
        skills_list = candidate['skills'].lower().split(", ")
        if skill_name.lower() in skills_list:
            candidates.append(candidate)
    return candidates
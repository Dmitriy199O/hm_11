from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate_by_id, \
    get_candidates_by_name, get_candidates_by_skill

data = load_candidates_from_json('candidates.json')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('list.html', candidates=data)


@app.route('/candidate/<int:id>')
def get_by_id(id):
    candidate = get_candidate_by_id(id)
    return render_template('profile.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, candidates_len=len(candidates))


@app.route('/skills/<skill_name>')
def skills(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidate=candidates, candidates_len=len(candidates), skill_name=skill_name)


app.run(debug=True)

from flask import Blueprint, render_template, jsonify, request, current_app, session
from app.models import URLGenerator
from functools import wraps

bp = Blueprint('main', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
def index():
    return render_template('main/index.html')

@bp.route('/generate', methods=['POST'])
@login_required
def generate():
    count = min(int(request.json.get('count', 5)), current_app.config['MAX_URLS'])
    urls = URLGenerator.generate_urls(count, current_app.config['BASE_URL'])
    return jsonify({'urls': urls})
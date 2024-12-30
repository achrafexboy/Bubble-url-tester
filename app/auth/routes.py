from flask import Blueprint, jsonify, request, session
import os

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    password = request.json.get('password')
    if password == os.environ.get('ADMIN_PASSWORD', 'admin123'):
        session['logged_in'] = True
        return jsonify({'success': True})
    return jsonify({'error': 'Invalid password'}), 401

@bp.route('/logout')
def logout():
    session.clear()
    return jsonify({'success': True})
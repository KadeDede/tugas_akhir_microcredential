from app import app
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from flask import send_file
from app.control import get_data_tiktok
from app.control import train
from app.control import predicting
from flask import Flask, render_template
import asyncio

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        req = request.get_json()
        hastag = req.get('hastag')
        # data_tiktok = get_data_tiktok.getdata(hastag)
        return jsonify({
            'nama_file': hastag,
        })

        # author_follow = req.get('author_follow')
        # author_love = req.get('author_love')
        #
        # data_tiktok = get_data_tiktok.getdata(hastag)
        # return jsonify({
        #     'nama_file': req,
        # })


@app.route('/analysis', methods=['POST'])
def analysis():
    if request.method == 'POST':
        req = request.get_json()
        hastag = req.get('hastag')
        author_follow = req.get('author_follow')
        author_love = req.get('author_love')
        music = req.get('music')
        # data_tiktok = get_data_tiktok.getdata(hastag)

        run_analisis = predicting.predicting(music, hastag, author_follow, author_love)
        return jsonify({
            'estimate': str(run_analisis),
        })

@app.route('/train', methods=['POST'])
def trains():
    if request.method == 'POST':
        req = request.get_json()
        # hastag = req.get('hastag')
        # author_follow = req.get('author_follow')
        # author_love = req.get('author_love')
        # music = req.get('music')
        # data_tiktok = get_data_tiktok.getdata(hastag)

        run_analisis = train.training()
        return jsonify({
            'estimate': str(run_analisis),
        })
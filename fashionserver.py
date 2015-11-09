from flask import Flask, request, jsonify, send_from_directory
import getcolor as gc
from treetolayout import tree_to_layout, gen_tree
from rowlayout import layout_to_html, gen_row_layout
import random

app = Flask(__name__)


@app.route('/')
def serve_ui():
    """ Serve the ui's html.
    """
    return app.send_static_file('index.html')


@app.route('/get-colors/', methods=['GET'])
def get_colors():
    colors = gc.get_colors();
    return jsonify({'colors': colors}), 200 

@app.route('/get-layout-colors/', methods=['GET'])
def get_layout_colors():
    colors = gc.get_layout_details();
    return jsonify({'colors': colors}), 200

@app.route('/page-gen/')
def page_gen():
    return app.send_static_file('page-generator.html')

@app.route('/page-row-gen/')
def page_row_gen():
    return app.send_static_file('page-row-generator.html')


@app.route('/gen-layout/', methods=['GET'])
def gen_layout():
    '''element_list = [{'weight': 2, 'data': '<p>Hello world!</p>'},
                    {'weight': 4, 'data': '<p>I am the master commander!</p>'},
                    {'weight': 1, 'data': '<p>Bruh</p>'},
                    {'weight': 2, 'data': '<p>Jenkins, you\'re a jerk</p>'},
                    {'weight': 1, 'data': '<p>Beep boop</p>'},
                    {'weight': 1, 'data': '<p>Making up words</p>'},
                    {'weight': 1, 'data': '<p>Fa la la la la</p>'},
                    {'weight': 1, 'data': '<p>gcd is probably 1 I mean lets be real</p>'},
                    {'weight': 1, 'data': '<p>3.1415926535897932384626433...</p>'},
                    {'weight': 1, 'data': '<p>I am a blob</p>'},
                    {'weight': 1, 'data': '<p>What is space?</p>'},
                    {'weight': 1, 'data': '<p>Who you?</p>'},
                    {'weight': 1, 'data': '<p>new phone who dis</p>'},
                    {'weight': 1, 'type': 'image', 'data': '<img src=""\>'},
                    ]'''

    element_list = [{'weight': 2, 'data': '<p>Hello world!</p>'},
                    {'weight': 4, 'data': '<p>I am the master commander!</p>'},
                    {'weight': 1, 'data': '<p>Bruh</p>'},
                    {'weight': 2, 'data': '<p>Jenkins, you\'re a jerk</p>'},
                    {'weight': 1, 'data': '<p>Beep boop</p>'},
                    {'weight': 1, 'data': '<p>Making up words</p>'},
                    {'weight': 1, 'type': 'image', 'data': '<img src="/static/images/SalazarGames.png"\>'},
                    {'weight': 1, 'type': 'image', 'data': '<img src="/static/images/swingsprofpic.jpg"\>'},
                    ]
    random.shuffle(element_list)
    return tree_to_layout(gen_tree(element_list, 0) )

@app.route('/gen-rows-layout/', methods=['GET'])
def gen_rows_layout():
    '''element_list = [{'weight': 2, 'data': '<p>Hello world!</p>'},
                    {'weight': 4, 'data': '<p>I am the master commander!</p>'},
                    {'weight': 1, 'data': '<p>Bruh</p>'},
                    {'weight': 2, 'data': '<p>Jenkins, you\'re a jerk</p>'},
                    {'weight': 1, 'data': '<p>Beep boop</p>'},
                    {'weight': 1, 'data': '<p>Making up words</p>'},
                    {'weight': 1, 'data': '<p>Fa la la la la</p>'},
                    {'weight': 1, 'data': '<p>gcd is probably 1 I mean lets be real</p>'},
                    {'weight': 1, 'data': '<p>3.1415926535897932384626433...</p>'},
                    {'weight': 1, 'data': '<p>I am a blob</p>'},
                    {'weight': 1, 'data': '<p>What is space?</p>'},
                    {'weight': 1, 'data': '<p>Who you?</p>'},
                    {'weight': 1, 'data': '<p>new phone who dis</p>'},
                    {'weight': 1, 'type': 'image', 'data': '<img src=""\>'},
                    ]'''

    panes = [
            {'title': 'pane1', 
            'content':[
                {'type':'text',  'data':'<p>Hello world!</p>'},
                {'type':'text',  'data':'<p>I am the master commander!</p>'},
                {'type':'text',  'data':'<p>Bruh</p>'},
                {'type':'text',  'data':'<p>Jenkins, you\'re a jerk</p>'},
                {'type':'text',  'data':'<p>Beep boop</p>'},
            ]},

            {'title': 'pane2', 
            'content':[
                {'type':'text',  'data':'<p>Making up words</p>'},
                {'type':'text',  'data':'<p>Fa la la la la</p>'},
                {'type':'text',  'data':'<p>gcd is probably 1 I mean lets be real</p>'},
                {'type':'text',  'data':'<p>3.1415926535897932384626433...</p>'},
                {'type':'text',  'data':'<p>I am a blob</p>'},
                {'type':'text',  'data':'<p>What is space?</p>'},
                {'type':'text',  'data':'<p>Who you?</p>'},
                {'type': 'image', 'data': '<img src="/static/images/SalazarGames.png"\>'},
                {'type': 'image', 'data': '<img src="/static/images/swingsprofpic.jpg"\>'},
            ]}
            ]
    return layout_to_html(gen_row_layout(panes))

if __name__ == '__main__':
    app.run(debug=True)

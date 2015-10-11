from flask import Flask, request, jsonify, send_from_directory
import getcolor as gc
from treetolayout import tree_to_layout, gen_tree

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

@app.route('/page-gen/')
def page_gen():
    return app.send_static_file('page-generator.html')


@app.route('/gen-layout/', methods=['GET'])
def gen_layout():
    element_list = [{'weight': 2, 'data': 'Hello world!'},
                    {'weight': 4, 'data': 'I am the master commander!'},
                    {'weight': 1, 'data': 'Bruh'},
                    {'weight': 2, 'data': 'Jenkins, you\'re a jerk'},
                    {'weight': 1, 'data': 'Beep boop'},
                    {'weight': 1, 'data': 'Making up words'},
                    {'weight': 1, 'data': 'Fa la la la la'},
                    {'weight': 1, 'data': 'gcd is probably 1 I mean lets be real'},
                    {'weight': 1, 'data': '3.1415926535897932384626433...'},
                    {'weight': 1, 'data': 'I am a blob'},
                    {'weight': 1, 'data': 'What is space?'},
                    {'weight': 1, 'data': 'Who you?'},
                    {'weight': 1, 'data': 'new phone who dis'},
                    ]
    return tree_to_layout(gen_tree(element_list, 0) )

if __name__ == '__main__':
    app.run(debug=True)

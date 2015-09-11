from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


@app.route('/')
def serve_ui():
    """ Serve the ui's html.
    """
    return app.send_static_file('index.html')


@app.route('/get-colors/', methods=['GET'])
def get_colors():
    # do stuff
    return jsonify({'colors': ["#CCCCAA", "#AACCCC", "#CCAACC", "#CCACAC"]}), 200

if __name__ == '__main__':
    app.run(debug=True)
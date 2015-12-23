from math import *
from random import *


def gen_piece_count():
    return 3 + randrange(-1,2) + randrange(-1,2)


def get_piece_weight(piece):
    return 100 + randrange(1,100);


def gen_row_layout(panes):
    for i in range(len(panes)):

        content = panes[i]['content']

        curr_bin = []
        bins = [curr_bin]
        bin_size = 500
        curr_size = 0
        piece_count = gen_piece_count()


        shuffle(content) 
        for piece in content:
            piece['weight'] = get_piece_weight(piece)
            
            if piece_count <= 0 or curr_size + piece['weight'] > bin_size:
                curr_bin = []
                bins.append(curr_bin)
                curr_size = 0
                piece_count = gen_piece_count()
                
            curr_bin.append(piece)
            curr_size += piece['weight']
            piece_count -= 1

        panes[i]['content'] = bins
    
    return panes

def layout_to_html(panes):
        html ='<div class="content-screen">\n'

        for pane in panes:
            html += pane_to_html(pane)
        
        html += '</div>\n'
        return html

def pane_to_html(pane):
        html ='<div id="' + pane['title'] + '" class="content-pane">\n'
        
        for row in pane['content']:
            html += row_to_html(row)
            
        html += '</div>\n'
        return html

def row_to_html(row):
        html ='<div class="content-row">\n'
        
        for piece in row:
            html += piece_to_html(piece)
            
        html += '</div>\n'
        return html

def piece_to_html(piece):
        classes = 'content-piece '
        if piece['type'] == 'image':
            classes += 'cont-image'
        elif piece['type'] == 'text':    
            classes += 'cont-text'
            
        html ='<div class="' + classes + '">\n'

        
        html += piece['data'] + "\n"
            
        html += '</div>\n'
        return html



def main():
    panes = [
            {'title': 'pane1', 
            'content':[
                {'type':'text',  'data':'<p>Hello world!</p>'},
                {'type':'text',  'data':'<p>I am the master commander!</p>'},
                {'type':'text',  'data':'<p>Bruh</p>'},
                {'type':'text',  'data':'<p>Jenkins, you\'re a jerk</p>'},
                {'type':'text',  'data':'<p>Beep boop</p>'}
            ]},

            {'title': 'pane2', 
            'content':[
                {'type':'text',  'data':'<p>Making up words</p>'},
                {'type':'text',  'data':'<p>Fa la la la la</p>'},
                {'type':'text',  'data':'<p>gcd is probably 1 I mean lets be real</p>'},
                {'type':'text',  'data':'<p>3.1415926535897932384626433...</p>'},
                {'type':'text',  'data':'<p>I am a blob</p>'},
                {'type':'text',  'data':'<p>What is space?</p>'},
                {'type':'text',  'data':'<p>Who you?</p>'}
            ]}
            ]
    layout = gen_row_layout(panes)
    print layout_to_html(layout)


if __name__ == '__main__':
    main()

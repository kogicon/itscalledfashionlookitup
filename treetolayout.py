from math import *
from random import *

def randremove(l, n):
    """
    Remove n random elements from list `l`
    """
    new = []
    for i in range(n):
            if len(l) == 0:
                    print 'ERROR: n was bigger than len l'
                    break
            r = randrange(len(l))
            new.append(l[r])
            l = l[:r] + l[r+1:]
    return new, l


def divide(lst, min_size, split_size):
    """
    Divides a list into several buckets, ensuring that each bucket has at least min_size elements.
    This is a generator, that yields each bucket as a list, one by one.
    :param lst: The list to split up
    :param min_size: The minimum number of objects in each sub-list
    :param split_size: The number of sub-lists
    :return: Yields a sub-list, one at a time.
    """
    it = iter(lst)
    from itertools import islice
    size = len(lst)
    for i in range(split_size - 1, 0, -1):
        s = randint(min_size, size - min_size * i)
        yield list(islice(it, 0, s))
        size -= s
    yield list(it)


def gen_tree(el, depth):
    tree = {}

    if len(el) <= 1:
            element = el[0]
            tree['type'] = 'content'
            tree['weight'] = element['weight']
            tree['data'] = element['data']
            return tree

    box_count = randrange(2, ceil(sqrt(len(el)))+1)

    boxes = list(divide(el, 1, box_count))

    print len(boxes)

    tree['type'] = 'container'
    if depth % 2 == 0:
            tree['orientation'] = 'V'
    else:
            tree['orientation'] = 'H'
    tree['weight'] = 1
    tree['children'] = []

    for box in boxes:
            tree['children'].append(gen_tree(box, depth+1))

    return tree


def tree_to_layout(tree):
        layout ='<div class="content-screen">\n'
        layout = tree_to_layout_help(layout, tree)
        layout += '</div>\n'
        return layout


def tree_to_layout_help(layout, tree):
    if tree['type'] == 'container':
        orientation = ''
        if tree['orientation'] == 'H':
                orientation = 'horizontal'
        elif tree['orientation'] == 'V':
                orientation = 'vertical'
        # assert that tree has children
        layout += '<div class="content-container ' + orientation + '">\n'
        for child in tree['children']:
                layout = tree_to_layout_help(layout, child)
        layout += '</div>\n'

    elif tree['type'] == 'content':
        # assert that tree has data
        layout += '<div class="content">\n'
        layout += tree['data'] + '\n'
        layout += '</div>\n'

    return layout


def main():
    element_list = [{'weight':2, 'data':'Hello world!'},
                    {'weight':4, 'data':'I am the master commander!'},
                    {'weight':1, 'data':'Bruh'},
                    {'weight':2, 'data':'Jenkins, you\'re a jerk'},
                    {'weight':1, 'data':'Beep boop'},
                    {'weight':1, 'data':'Making up words'},
                    {'weight':1, 'data':'Fa la la la la'},
                    {'weight':1, 'data':'gcd is probably 1 I mean lets be real'},
                    {'weight':1, 'data':'3.1415926535897932384626433...'},
                    {'weight':1, 'data':'I am a blob'},
                    {'weight':1, 'data':'What is space?'},
                    {'weight':1, 'data':'Who you?'}]
    print tree_to_layout(gen_tree(element_list, 0) )


if __name__ == '__main__':
    main()
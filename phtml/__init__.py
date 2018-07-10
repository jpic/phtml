import copy


class Node:
    def __new__(cls, *args):
        self = object.__new__(cls)
        self.tag = copy.copy(getattr(cls, 'tag'))
        self.attrs = copy.copy(getattr(cls, 'attrs', {}))
        return self

    def __init__(self, *args, selfclose=None):
        self.children = []
        for arg in args:
            if isinstance(arg, dict):
                self.attrs.update(arg)
            else:
                self.children.append(arg)

        self.selfclose = selfclose

    def __str__(self):
        html = ['<', self.tag]
        for key, value in self.attrs.items():
            html += [
                ' ',
                key.replace('_', '-'),
                '="',
                value,
                '"',
            ]

        if self.selfclose:
            html.append(' />')
            if self.children:
                raise Exception('No children with selfclose')
        else:
            html += ['>'] + [str(c) for c in self.children]
            html += ['</', self.tag, '>']

        return ''.join(html)

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.attrs[key]
        elif isinstance(key, int):
            return self.children[key]
        else:
            raise Exception('Node __getitem__ only accepts int or str')

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self.attrs[key] = value
        elif isinstance(key, int):
            self.children[key] = value
        else:
            raise Exception('Node __setitem__ only accepts int or str key')

    def append(self, value):
        self.children.append(value)

    def jinja(self, **context):
        from jinja2 import Template
        return Template(str(self)).render(**context)


class Div(Node):
    tag = 'div'


class Form(Node):
    tag = 'form'
    attrs = {'method': 'POST'}


class Input(Node):
    tag = 'input'


class Submit(Input):
    attrs = {'type': 'submit'}

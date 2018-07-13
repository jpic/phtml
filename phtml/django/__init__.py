import phtml


class Form(phtml.Form):
    pass


class Field(phtml.Div):
    def __init__(self, name, *args):
        self.name = name
        super().__init__(*args)

    def __str__(self):
        return '''<input
            type="{{ form[self.name].widget.type }}"
            name="{{ form[self.name].widget.name }}"
            {% if widget.value != None %}value="{{ widget.value|stringformat:'s' }}"{% endif %}
            {% for name, value in widget.attrs.items %}{% if value is not False %} {{ name }}{% if value is not True %}="{{ value|stringformat:'s' }}"{% endif %}{% endif %}{% endfor %}
        >'''

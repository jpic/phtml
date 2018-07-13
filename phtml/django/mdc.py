from phtml import django, mdc


class Form(django.Form, mdc.Form):
    pass


class Field(django.Field, mdc.Field):
    pass

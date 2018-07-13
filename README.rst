Welcome to phtml !
~~~~~~~~~~~~~~~~~~

phtml is a silly python library to generate HTML in Python like you would with a template, but refactor-oriented with a Pythonic React-like pattern based on nested components.

Component base
==============

You have an Element class you can import as E:

.. code-block:: python

    from phtml import E

    form_layout = E(
        'form',                     # e.tag
        {                           # e.attrs
            'class': 'foo',         # e.attrs['class']
            'method': 'POST',       # e.attrs['method']
        },
        '{{ form.as_p() }}',        # e.children[0]
        E('input', {'type': 'submit'}),
    )

Casting form_layout to string will return the following:

.. code-block:: django

    <form class="foo" method="POST">
        {{ form.as_p() }}
        <input type="submit" />
    </form>

Rendering with jinja:

.. code-block:: python

    form_layout.jinja(form=YourForm)

You can import the Component class as C:

.. code-block:: python

    class CheckboxField(Comoponent):
        phtml = '''
        <div class="mdc-form-field">
            <div class="mdc-checkbox">
                <input
                    type="checkbox"
                    id="{{ field.id }}"
                    class="mdc-checkbox__native-control"
                    name="{{ field.name }}"
                />
              <div class="mdc-checkbox__background"></div>
            </div>
            <label for="{{ id }}">{{ label }}</label>
        </div>
        '''

React style
===========

Another possibility

.. code-block:: python

    class Checkbox(Node):
        html = '''
<div class="mdc-form-field">
  <div class="mdc-checkbox">
    <input type="checkbox" id="my-checkbox" class="mdc-checkbox__native-control"/>
    <div class="mdc-checkbox__background">
    </div>
  </div>
  <label for="my-checkbox">{self.help_text}</label>
</div>
        '''.strip()

Rendering
=========

While calling ``phtml.jinja.render(form_layout, form=YourForm())`` will
return the phtml output processed with form in the context and produce the
final result.

The whole purpose is refactoring HTML generating logic into Python components:

.. code-block:: python

    from phtml import Form, Submit

    form_layout = Form(
        {'class': 'foo'},
        ['{{ form.as_p() }}', Submit())],
    )

Importing on the fly
====================

.. code-block:: python

    from phtml import Node

    form_layout = Node.factory(
        'phtml.Form', {'class': 'foo'},
        '{{ form.as_p() }}',
        Node('phtml.Submit'),
    )

Jinja and Materialize for the poor
==================================

Suppose you want to make a nice layout for the login form, please don't repeat
boring and verbose code like this because somewhere in the world a cat would
probably die because of a side effect in an alternate reality or something:

.. code-block:: python

    from phtml import Form, Div

    your_layout = Form(
        Div({'class': 'row'},
            Div({'class': 'col m6 s12'}, '{{ form["username"] }}'),
            Div({'class': 'col m6 s12'}, '{{ form["password"] }}'),
        ),
    )

Refactored components for the rich
==================================

Instead make a beautiful layout with reusable components:

.. code-block:: python

    from phtml.django.mdc import Form, Row, Col, Input

    class YourLoginForm(forms.LoginForm):
        _phtml = Form(
            Row(
                Col(m=6, s=12, Input('username')),
                Col(m=6, s=12, Input('password')),
            )
        )

.. note:: For the documentation of the constructor of each component, please
          fill in their docstrings under their signature in Python code, UTSL !

Silly and Stupid context based rendering
========================================

You could render as such in jinja (or in Python without the curly braces):
``{{ form._phtml.jinja(form) }}``, since all rendering logic should already be
in phtml.

Thank you
=========

Thanks a lot for reading. Hope this will serve as a useful example for anybody
on a mission to "refactor HTML in Python".

Welcome to phtml !
~~~~~~~~~~~~~~~~~~

phtml is a silly python library to generate HTML in Python like you would with a template, but refactor-oriented with a Pythonic React-like pattern based on nested components.

Component base
==============

The base component class is Node:

.. code-block:: python

    from phtml import Node

    form_layout = Node(
        'form',                     # node.tag
        {                           # node.attrs
            'class': 'foo',         # node.attrs['class']
            'method': 'POST',       # node.attrs['method']
        },
        [                           # node.children
            '{{ form.as_p() }}',    # node.children[0]
            Node('input', {'type': 'submit'}, selfclose=True),
        ],
    )

Casting form_layout to string will return the following:

.. code-block:: django

    <form class="foo" method="POST">
        {{ form.as_p() }}
        <input type="submit" />
    </form>

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
        ['{{ form.as_p() }}', Node('phtml.Submit')],
    )

Jinja and Materialize for the poor
==================================

Suppose you want to make a nice layout for the login form, please don't repeat
boring and verbose code like this because somewhere in the world a cat would
probably die because of a side effect in an alternate reality or something:

.. code-block:: python

    from phtml import Form, Div

    your_layout = Form(
        Div({'class': 'row'}, [
            Div({'class': 'col m6 s12'}, ['{{ form["username"] }}']),
            Div({'class': 'col m6 s12'}, ['{{ form["password"] }}']),
        ]),
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
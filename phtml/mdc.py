from phtml import Div


class Grid(Div):
    attrs = {'class': 'mdc-layout-grid'}


class Row(Div):
    attrs = {'class': 'mdc-layout-grid__inner'}


class Cell(Div):
    attrs = {'class': 'mdc-layout-grid__cell'}


class Form(Div):
    phtml = '''
    <form>
        {% for error in form.non_field_errors %}
            {{ error }}
        {% endfor %}
    </form>
    '''


class Field(Div):
    attrs = {'class': 'mdc-form-field'}


class CheckboxField:
    phtml = '''
    <div class="mdc-form-field">
        {{
        <div class="mdc-checkbox">
            <input
                type="checkbox"
                id="{{ id }}"
                class="mdc-checkbox__native-control"
                name="{{ name }}"
            />
          <div class="mdc-checkbox__background"></div>
        </div>
        <label for="{{ id }}">{{ label }}</label>
    </div>
    '''

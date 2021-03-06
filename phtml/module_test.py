import pytest

from phtml import Div


def test_init_div_tag():
    assert Div().tag == 'div'


def test_init_div_attrs():
    assert Div().attrs == {}


def test_init_div_children():
    assert Div().children == []


def test_init_attr():
    assert Div({'data-url': 'foo'}).attrs == {'data-url': 'foo'}


def test_init_children():
    assert Div('foo').children == ['foo']


def test_str_default():
    assert str(Div()) == '<div></div>'


def test_str_child():
    assert str(Div('foo')) == '<div>foo</div>'


def test_str_children():
    assert str(Div('foo', Div())) == '<div>foo<div></div></div>'


def test_str_attr():
    assert str(Div({'class': 'a'})) == '<div class="a"></div>'


def test_str_attr_child():
    assert str(Div({'class': 'a'}, 'b')) == '<div class="a">b</div>'


def test_getitem_attr():
    assert Div({'class': 'a'})['class'] == 'a'


def test_getitem_child():
    assert Div('a')[0] == 'a'


def test_getitem_exception():
    with pytest.raises(Exception):
        Div()['data-lol']


def test_setitem_attr():
    n = Div()
    n['data-lol'] = 'a'
    assert n.attrs['data-lol'] == 'a'


def test_append_child():
    n = Div()
    n.append('bar')
    assert n.children[0] == 'bar'


def test_setitem_exception():
    with pytest.raises(Exception):
        Div()[Div] = 'test'


def test_jinja():
    assert Div('{{ a }}').jinja(a=1) == '<div>1</div>'


def test_new_attrs():
    class Foo(Div):
        attrs = {'class': 'foo'}
    assert Foo()['class'] == 'foo'


def test_new_attrs_update():
    class Foo(Div):
        attrs = {'class': 'foo'}
    assert Foo({'bar': 'test'})['bar'] == 'test'


def test_new_attrs_override():
    class Foo(Div):
        attrs = {'class': 'foo'}
    assert Foo({'class': 'bar'})['class'] == 'bar'


def test_new_phtml_tag_parse():
    class Foo(Div):
        phtml = '<form></form>'
    assert Foo().tag == 'form'


def test_new_phtml_attr_merge():
    class Foo(Div):
        phtml = '<form class="foo"></form>'
        attrs = {'method': 'POST'}

    assert Foo().attrs == {'class': 'foo', 'method': 'POST'}
    assert str(Foo()) == '<form method="POST" class="foo"></form>'


def test_new_phtml_attr_override():
    class Foo(Div):
        phtml = '<form></form>'
        attrs = {'method': 'POST'}
    assert Foo({'method': 'GET'}).attrs == {'method': 'GET'}


def test_new_phtml_children():
    class Foo(Div):
        phtml = '<form></form>'
    assert str(Foo('bar')) == '<form>bar</form>'

import pytest

from api import create_app


app = create_app(__name__)


def test_get_cats_facts():
    response = app.test_client().get('/cat_facts/2')
    assert response.status_code == 400

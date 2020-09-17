import pytest
from unittest.mock import Mock

from libpythonpro import github_api

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/18421824?v=4'
    resp_mock.json.return_value = {'login': 'wosubtil',
                                   'id': 18421824,
                                   'avatar_url': url}
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    github_api.requests.get = Mock(return_value=resp_mock)
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('wosubtil')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('rezon')
    assert 'https://avatars2.githubusercontent.com/u/527028?v=4' == url

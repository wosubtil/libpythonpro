from unittest.mock import Mock

from libpythonpro import github_api

def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {'login': 'wosubtil',
                                   'id': 18421824,
                                   'avatar_url': 'https://avatars0.githubusercontent.com/u/18421824?v=4'}
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('wosubtil')
    assert 'https://avatars0.githubusercontent.com/u/18421824?v=4' == url
from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Welinton', email='welinton.ti@gmail.com'),
            Usuario(nome='Gabriel', email='gabriel@gmail.com')
        ],
        [
            Usuario(nome='Welinton', email='welinton.ti@gmail.com')
        ]
    ]

)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'welinton.ti@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Welinton', email='welinton.ti@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'welinton@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'welinton@gmail.com',
        'welinton.ti@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )

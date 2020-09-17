import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'welinton.ti@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados



def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Welinton', email='welinton.ti@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'welinton@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
    assert enviador.parametros_de_envio == (
        'welinton@gmail.com',
        'welinton.ti@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
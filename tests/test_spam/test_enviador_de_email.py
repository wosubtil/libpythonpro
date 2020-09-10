import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['welinton.ti@gmail.com', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'lordwos@gmail.com',
        'Curso Python Pro',
        'Primeira turma Guido Von Rossun'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()

    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'lordwos@gmail.com',
            'Curso Python Pro',
            'Primeira turma Guido Von Rossun'
        )

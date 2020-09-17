import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')  # o escopo padrão é por function
def conexao():
    # Setup
    conexao_obj = Conexao()
    # Retorna o valor injetado nos testes
    yield conexao_obj
    # Teardown
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
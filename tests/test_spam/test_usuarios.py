from libpythonpro.spam.modelos import Usuario


# scope padrão: function
# scope module - Escopo por módulo
# scope session


def test_savar_usuario(sessao):
    usuario = Usuario(nome='Welinton', email='welinton.ti@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Welinton', email='welinton.ti@gmail.com'),
                Usuario(nome='Gabriel', email='gabriel@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

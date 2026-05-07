from unittest.mock import Mock
from main import calcular_desconto, processar_pedido
import pytest

def test_calcular_desconto_com_cupom():
    valor = calcular_desconto(100, "GEEK20")
    assert valor == 80

def test_calcular_desconto_sem_cupom():
    valor = calcular_desconto(100, "")
    assert valor == 100

def test_processar_pedido_sucesso():
    gateway_mock = Mock()
    gateway_mock.cobrar.return_value = True

    resultado = processar_pedido(100, "1234", gateway_mock)

    gateway_mock.cobrar.assert_called_once_with("1234", 100)

    assert resultado == "Compra aprovada!"

def test_processar_pedido_gateway_recusado():
    gateway_mock = Mock()
    gateway_mock.cobrar.return_value = False

    with pytest.raises(ValueError):
        processar_pedido(100, "1234", gateway_mock)

def test_processar_pedido_valor_invalido():
    gateway_mock = Mock()

    with pytest.raises(ValueError):
        processar_pedido(0, "1234", gateway_mock)
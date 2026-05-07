from pytest_bdd import scenarios, given, when, then
from fastapi.testclient import TestClient
from main import app

scenarios("./features/compra_sucesso.feature")

client = TestClient(app)

@given('que existe um produto "teclado"')
def produto_existe():
    pass

@when('eu realizar uma compra do produto "teclado"')
def realizar_compra():
    global response

    response = client.post(
        "/api/comprar",
        json={
            "produto": "teclado",
            "cartao": "1234",
            "cupom": ""
        }
    )

@then("a compra deve ser aprovada")
def validar_compra():
    assert response.status_code == 200
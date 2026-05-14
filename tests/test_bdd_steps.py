from pytest_bdd import scenarios, given, when, then

scenarios("./features/compra_sucesso.feature")

response = None

@given('que existe um produto "teclado"')
def produto_existe(client):
    response = client.get("/api/produtos")

    assert response.status_code == 200
    produtos = response.json()

    assert any(p["nome"] == "teclado" for p in produtos)

@when('eu realizar uma compra do produto "teclado"')
def realizar_compra(client):
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
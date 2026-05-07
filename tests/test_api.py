def test_listar_produtos(client):
    response = client.get("/api/produtos")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert "nome" in data[0]
    assert "preco" in data[0]
    assert "estoque" in data[0]

def test_comprar_produto(client):
    response = client.post(
        "/api/comprar",
        json={
            "produto": "teclado",
            "cartao": "1111",
            "cupom": "GEEK20"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "sucesso"
    assert data["valor_pago"] == 160.0

def test_produto_inexistente(client):
    response = client.post(
        "/api/comprar",
        json={
            "produto": "cadeira",
            "cartao": "1111"
        }
    )

    assert response.status_code == 404
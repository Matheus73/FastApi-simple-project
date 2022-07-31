def test_post_book(client):
    response = client.post("/book/",json={"titulo": "test", "autor": "test", "ano": 2021})
    assert response.status_code == 201
    assert response.json() == {
            "message": "Dados cadastrados com sucesso",
            "error": None,
            "data": {
                "id": 11,
                "titulo": "test",   
                "autor": "test",
                "ano": 2021,
                }
            }
    

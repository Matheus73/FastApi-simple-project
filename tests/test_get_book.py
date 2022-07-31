def test_get_book(client):
    response = client.get("/book/")
    assert response.status_code == 201
    assert response.json() == {
            "message": "dados buscados com sucesso",
            "error": None,
            "data": [ 
                { "id": 1, "titulo": "Livro 1", "autor": "Autor 1", "ano": 2020 },
                { "id": 2, "titulo": "Livro 2", "autor": "Autor 2", "ano": 2020 },
                { "id": 3, "titulo": "Livro 3", "autor": "Autor 3", "ano": 2020 },
                { "id": 4, "titulo": "Livro 4", "autor": "Autor 4", "ano": 2020 },
                { "id": 5, "titulo": "Livro 5", "autor": "Autor 5", "ano": 2020 },
                { "id": 6, "titulo": "Livro 6", "autor": "Autor 6", "ano": 2020 },
                { "id": 7, "titulo": "Livro 7", "autor": "Autor 7", "ano": 2020 },
                { "id": 8, "titulo": "Livro 8", "autor": "Autor 8", "ano": 2020 },
                { "id": 9, "titulo": "Livro 9", "autor": "Autor 9", "ano": 2020 },
                { "id": 10, "titulo": "Livro 10", "autor": "Autor 10", "ano": 2020 },
            ]
        }

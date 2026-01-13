import pytest_asyncio
from fastapi import status
from httpx import AsyncClient


async def test_create_post_success(client: AsyncClient, access_token: str):
    # Given
    # cria o header de autorização com o token de acesso
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "title": "post 1",
        "content": "some content",
        "published_at": "2024-04-12T04:33:14.403Z",
        "published": True
    }

    # When
    # faz a requisição POST para o endpoint de criação de post
    response = await client.post("/posts/", json=data, headers=headers)

    # Then
    # obtém o conteúdo da resposta
    content = response.json()
    # verifica se a resposta está correta
    assert response.status_code == status.HTTP_201_CREATED
    # verifica se o título do post está correto
    assert content["id"] is not None


async def test_create_post_invalid_payload_fail(client: AsyncClient, access_token: str):
    # Given
    # cria o header de autorização com o token de acesso
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "content": "some content",
        "published_at": "2024-04-12T04:33:14.403Z",
        "published": True
    }

    # When
    # faz a requisição POST para o endpoint de criação de post
    response = await client.post("/posts/", json=data, headers=headers)

    # Then
    content = response.json()  # obtém o conteúdo da resposta
    # verifica se a resposta está correta
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    # verifica se o campo 'title' está presente na mensagem de erro
    assert content["detail"][0]["loc"] == ["body", "title"]


async def test_create_post_not_authenticated_fail(client: AsyncClient):
    # Given
    # cria os dados do post
    data = {
        "content": "some content",
        "published_at": "2024-04-12T04:33:14.403Z",
        "published": True
    }

    # When
    # faz a requisição POST para o endpoint de criação de post sem o header de autorização
    response = await client.post("/posts/", json=data, headers={})

    # Then
    # verifica se a resposta está correta
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
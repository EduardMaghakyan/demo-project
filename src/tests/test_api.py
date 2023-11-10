from http import HTTPStatus


def test_api(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    content = response.json()
    assert content["Hello"] == "World"

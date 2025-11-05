from app.models.planet import Planet
from app.routes.route_utilities import validate_model

def test_validate_model(client, two_saved_planets):
    # Act
    planet = validate_model(Planet, 2)

    # Assert
    assert planet.name == "Venus"
    assert planet.description== "A rocky planet with a thick, toxic atmosphere and surface temperatures hot enough to melt lead."
    assert planet.diameter==12104

# def test_validate_model_invalid_id(client, two_saved_planets):
#     # Arrange
#     test_data = {
#         "title": "New Book",
#         "description": "The Best!"
#     }

#     # Act
#     response = client.put("/books/cat", json=test_data)
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 400
#     assert response_body == {"message": "Book cat invalid"}
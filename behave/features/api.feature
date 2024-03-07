# comentarios
  Feature: Test API

    Scenario: Request to API with specific data
      Given I have an endpoint "https://rickandmortyapi.com/api/character/"
      And I count in the following query params "name" and its value "rick"
      When I do request with query params
      Then I see the statuscode 200
      And replies me with name "Rick Sanchez"

    Scenario: Request to API with fail specific data
      Given I have an endpoint "https://rickandmortyapi.com/api/character/"
      And I count in other query params "name" and its fail value "643"
      When I do request with different query params
      Then I see the statuscode 404
      And  response me with an error "There is nothing here"

    Scenario: Request to API with specie and status
      Given I have an endpoint "https://rickandmortyapi.com/api/character/"
      And I count in the following query params:
        | key     | value |
        | status  | Alive |
        | specie  | Human |
      When I do request with status
      Then I see the statuscode 200
      And  I can see responses with status "Alive" and specie "Human"

    Scenario: Request to API with the gender character
      Given I have an endpoint "https://rickandmortyapi.com/api/character/"
      And I count in the following query params "gender" with "unknown"
      When I do request with gender
      Then I see the statuscode 200
      And The response with gender "unknown"


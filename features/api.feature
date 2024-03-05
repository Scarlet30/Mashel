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





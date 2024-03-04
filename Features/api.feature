# features/api.feature

Feature: Testing API with Selenium and Locust

  Scenario: Verify API response using Selenium
    Given the API endpoint is "https://rickandmortyapi.com/api/character"
    When I open the API endpoint in a browser
    Then the API response should contain "expected_data"

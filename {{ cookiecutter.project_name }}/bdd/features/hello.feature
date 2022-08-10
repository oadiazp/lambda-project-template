Feature: Foo test
  Scenario: Test hello world
    When a GET request to / is made
    Then the REST response is successful

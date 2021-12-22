Feature: Employee should be able to retrieve a request list
  Scenario: Employee should input an id and get back a list of requests
    Given Employee is on the home page
    When Employee inputs <employee id> into the employee box
    When Employee clicks list submit button
    Then Employee receives a list of requests
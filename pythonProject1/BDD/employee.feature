Feature: Employee should be able to submit a request
  Scenario Outline: As a employee I should be able to input information to submit a request
    Given Employee is on the Employee Home page
    When Employee inputs <amount> into the amount box
    When Employee inputs <employee id> into the first employee box
    When Employee inputs <reason> into the reason box
    When Employee inputs <manager id> into the manager box
    When Employee clicks on the submit button on Employee Home Page
    Then an alert is given
    Examples:
      | amount | employee id | reason | manager id |
      | 200    | 1           | travel | 1          |
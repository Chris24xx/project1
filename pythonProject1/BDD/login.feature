Feature: users should be able to login

  Scenario Outline: as a Employee I Should be able to login to the Employee Home Page
    Given Employee is on the login page
    When Employee inputs <username> into username field
    When Employee inputs <password> into password field
    When Employee clicks submit button
    Then Employee should be redirected to the webpage with the title <title>
    Examples:
      | username | password  | title              |  |
      | test     | password1 | Employee Home Page |  |

  Scenario Outline: as a Manager I should be able to login to the Manager Home Page
     Given Manager is on the login page
      When Manager inputs <username> into username field
      When Manager inputs <password> into password field
      When Manager clicks submit button
      Then Manager should be redirected to the webpage with the title <title>
    Examples:
      | username | password | title   |  |
      | usertest | passtest | Manager |  |
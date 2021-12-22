Feature: Manager should be able to manage Requests
  Scenario: As a Manager I should be able to get a list of requests
    Given Manager is on the Manager Home page
    When Manager inputs <manager id> into manager field
    When Manager clicks the pending requests button
    Then Manager receives a list of requests

  Scenario: As a Manager I should be able to get all requests list
    Given Manager is on the Manager Home page
    When Manager inputs <manager id> into second manager field
    When Manager clicks the all requests button
    Then Manager receives a list of all requests

  Scenario: As a Manager I should be able to get statistics
    Given Manager is on the Manager Home page
    When Manager inputs <manager id> into the stat box
    When Manager selects an option
    When  Manager submits the stat data
    Then Manager will receive a statistic

  Scenario Outline: As a Manager I should be able to Approve or Deny a request and provide a comment
    Given Manager is on the Manager Home page
    When Manager inputs <comment> into the comment field
    When Manager inputs <status> into the status field
    When Manger inputs <requests id> into the request field
    When Manager clicks the submit button for update requests
    Then Manager should get an alert
    Examples:
      | comment             | status   | requests id |
      | you ask for to much | Denied   | 10          |
      | fine stop asking    | Approved |8            |




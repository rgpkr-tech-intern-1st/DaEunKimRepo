Feature: check 'count'
  Scenario: check validation of count's results
    Given function `find` searches for a number between two numbers.
    When `count` returns result of `find` and its running time as tuple.
    Then first element in tuple is an integer.
    And second element in tuple is an float greater or equal to 0.

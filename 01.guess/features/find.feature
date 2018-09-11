Feature: check 'find'
  Scenario: check if 'find' return right number
    Given min_ is minimum of integer.
    And max_ is maximum of integer.
    When `find` searches for a number between min_ and max_.
    Then `find` returns 1954421783993232787.

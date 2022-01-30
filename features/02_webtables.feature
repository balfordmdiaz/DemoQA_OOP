Feature: Flowchart of web tables

   Scenario: Modify one register of the option web tables
      Given go to the url
      And select elements
      And select web tables
      And edit one register of the list
      And insert firstname "Balford" and lastname "Montenegro"
      And insert email "balfordm21@gmail.com" and age
      And insert salary and department "QA Automation"
      And submit the modified register
      Then validate the register
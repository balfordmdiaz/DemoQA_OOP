Feature: DemoQA

    Scenario Outline: Fill the test form
        Given go to the url
        And insert the firstname "<firstname>", lastname "<lastname>", email "<email>" 
        And select gender
        And insert mobile "<mobile>", date, subjects
        And insert hobbies, upload the Profile picute and the address "<address>"
        And select state "<state>" and city "<city>"
        Then submit form

        Examples:   firstname, lastname, email
            |   firstname   |   lastname    |   email                       |   mobile          |   address                             |   state       |   city            |
            |   Sander      |   Pacheco     |   narcisocode@gmail.com       |   6265648754      |   St Lucia, 2 blocks south            |   Rajasthan   |   Jaiselmer       |
            |   Balford     |   Montenegro  |   balfordm21@gmail.com        |   5454621369      |   1st street, Bello Horizonte         |   Haryana     |   Panipat         |
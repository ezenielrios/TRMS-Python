## Created by Ezeniel at 5/9/2022

Feature: The Login Feature Works

     Scenario: User Logs in as Employee
          Given The User is on the Log In Page
          When The User types test in the userId field
          When The User types test in the userPw field
          When The User clicks on the login button
          Then The User should be on the form Page


#     Scenario: User Logs in as Manager
#          Given The User is on the Log In Page
#          When The User types supervisor in the userId field
#          When The User types password in the userPw field
#          When The User clicks on the login button
#          Then The User should be on the form Page






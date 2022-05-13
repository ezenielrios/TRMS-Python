## Created by Ezeniel at 5/09/2022

Feature: Create a Form Works

    Scenario Outline: Create a Form
        Given The User is on the Create Form Page
        When The User types <date> in the date input
        When The User types <time> in the time input
        When The User types <location> in the location input
        When The User types <description> in the course description input
        When The User types <cost> in the cost input
        When The User types <grade> in the grade input
        When The User types <event> in the event input
        When The User types <justification> in the justification input
        When The User Clicks the Submit Button
         Then Form should be added successfully
      Examples:
        | date       | time   | location | description | cost | grade | event     | justification |
        | 05/11/2022 | 9:00PM | Remote   | Networking  | 1000 | A     | Seminars  | Yes           |


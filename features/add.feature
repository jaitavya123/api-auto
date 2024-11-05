Feature: Add book in record

 Scenario: verify add book api
     Given we have detail of book
     When we submit book detail in addBook api
     Then sucess in adding book
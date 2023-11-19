*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  seppo  seppo123#
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  seppo123#
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123#
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  £$£$‚£$  kalle123#
    Output Should Contain  Username contains invalid characters

Register With Valid Username And Too Short Password
    Input Credentials  seppo  kille
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  seppo  asdfasdfsaf

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123#
    Input New Command

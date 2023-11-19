*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page1

*** Variables ***
${VALID_USERNAME}  testuser
${VALID_PASSWORD}  testpassword
${TOO_SHORT_USERNAME}  te
${INVALID_PASSWORD}  test


*** Test Cases ***
Register With Valid Username And Password
    Set Username  ${VALID_USERNAME}
    Set Password  ${VALID_PASSWORD}
    Set Password Confirmation  ${VALID_PASSWORD}
    Submit Registration
    Registration Should Be Successful  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  ${TOO_SHORT_USERNAME}
    Set Password  ${VALID_PASSWORD}
    Set Password Confirmation  ${VALID_PASSWORD}
    Submit Registration
    Registration Should Fail  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username  ${VALID_USERNAME}
    Set Password  ${INVALID_PASSWORD}
    Set Password Confirmation  ${INVALID_PASSWORD}
    Submit Registration
    Registration Should Fail  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  ${VALID_USERNAME}
    Set Password  ${VALID_PASSWORD}
    Set Password Confirmation  ${INVALID_PASSWORD}
    Submit Registration
    Registration Should Fail  Password and password confirmation do not match

*** Keywords ***
Go To Register Page1
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Registration Should Be Successful
    [Arguments]  ${message}
    Page Should Contain  ${message}

Registration Should Fail
    [Arguments]  ${message}
    Page Should Contain  ${message}


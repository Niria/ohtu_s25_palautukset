*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testikäyttäjä
    Set Password  hyväSalasana1
    Set Password Confirmation  hyväSalasana1
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  hyväSalasana1
    Set Password Confirmation  hyväSalasana1
    Click Button  Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  testikäyttäjä
    Set Password  testi
    Set Password Confirmation  testi
    Click Button  Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  testikäyttäjä
    Set Password  salasana
    Set Password Confirmation  salasana
    Click Button  Register
    Register Should Fail With Message  Password must contain at least one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username  testikäyttäjä
    Set Password  hyväSalasana1
    Set Password Confirmation  hyväSalasana2
    Click Button  Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Reset Application Create User And Go To Register Page
    Set Username  kalle
    Set Password  hyväsalasana1
    Set Password Confirmation  hyväsalasana1
    Click Button  Register
    Register Should Fail With Message  Username already taken

*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

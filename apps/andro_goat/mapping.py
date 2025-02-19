from service.input_service import do_tap, do_input_text

mock_data = {
    "username":"user",
    "password":"password123"
}

def login_data_storage_1():
    #select data storage
    do_tap(395, 809)
    #select fisrt option
    do_tap(382, 509)
    # type user
    do_input_text(mock_data['username'])
    # tap pass
    do_tap(372, 601)
    # type pass
    do_input_text(mock_data['password'])
    # tap save
    do_tap(391, 703)
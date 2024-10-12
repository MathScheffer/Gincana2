from TestApi import ApiTests

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apiTests = ApiTests("Matheus", "oqibz@example.com", "123456")

    apiTests.createUserTest()
    apiTests.loginTest()
    apiTests.deleteUserTest()
    apiTests.editUserTest()

import password


class TestPassword:
    def test_password_few_letters(self):
        assert password.password("H3ll0") is False

    def test_only_numbers(self):
        assert password.password("12345623") is False

    def test_password_only_letters(self):
        assert password.password("asdfassDg") is False

    def test_not_password(self):
        assert password.password("0psPasSwOrD") is False

    def test_real_password(self):
        assert password.password("Fr3ddyDrrrrr3dd") is True

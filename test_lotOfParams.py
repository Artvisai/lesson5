import lotOfParams


class TestParams:
    def test_no_params(self):
        assert lotOfParams.summ() == 0

    def test_num_params(self):
        assert lotOfParams.summ(1, 2, 3, 4, 5) == 15

    def test_str_params(self):
        assert lotOfParams.summ('q', 'w', 'e', 'r', 't', 'y') == "qwerty"

    def test_err_params(self):
        assert lotOfParams.summ('k', 0, 'm', 'm', 4, 'n', 'd', 0) == "TypeError!"

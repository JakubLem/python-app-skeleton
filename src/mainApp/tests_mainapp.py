class TestMain:
    def test_conftest(self, some_obj):
        assert some_obj() == 11

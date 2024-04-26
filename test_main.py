from main import determine_if_pangram_exists


class TestFinal:
    def test_determine_if_pangram_exists__simple_pangram(self):
        assert (
            determine_if_pangram_exists("The quick brown fox jumpos over the lazy dog.")
            == True
        )

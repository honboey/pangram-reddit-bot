from main import (
    determine_if_pangram_exists,
    string_has_over_25_letters,
    isolate_z_sentence,
)

single_sentence_pangram = "The quick brown fox jumps over the lazy dog."
multi_sentence_pangram = "Here is the first sentence. The quick brown fox jumps over the lazy dog. Here is the last sentence."
single_sentence_non_pangram = "This is not a pangram"
multi_sentence_non_pangram = (
    "Here is the first sentence. This is not a pangram. Here is the last sentence."
)


class TestDetermineIfPangramExists:
    def test_determine_if_pangram_exists__single_sentence_pangram(self):
        assert determine_if_pangram_exists(single_sentence_pangram) == True

    def test_determine_if_pangram_exists__multi_sentence_pangram(self):
        assert determine_if_pangram_exists(multi_sentence_pangram) == True

    def test_determine_if_pangram_exists__single_sentence_non_pangram(self):
        assert determine_if_pangram_exists(single_sentence_non_pangram) == False

    def test_determine_if_pangram_exists__multi_sentence_non_pangram(self):
        assert determine_if_pangram_exists(multi_sentence_non_pangram) == False


class TestStringHasOver25Letters:
    def test_string_has_over_25_letters__true(self):
        assert string_has_over_25_letters(single_sentence_pangram) == True

    def test_string_has_over_25_letters__false(self):
        assert (
            string_has_over_25_letters("The quick brown fox jumps over the lazy")
            == False
        )


class TestDoesStringHaveZ:
    def test_isolate_z_sentence__single_sentence_pangram(self):
        assert (
            isolate_z_sentence(single_sentence_pangram)
            == "The quick brown fox jumps over the lazy dog"
        )

    def test_isolate_z_sentence__multi_sentence_pangram(self):
        assert (
            isolate_z_sentence(multi_sentence_pangram)
            == "The quick brown fox jumps over the lazy dog"
        )

    def test_isolate_z_sentence__single_sentence_non_pangram(self):
        assert isolate_z_sentence(single_sentence_non_pangram) == "No pangram"

    def test_isolate_z_sentence__multi_sentence_non_pangram(self):
        assert isolate_z_sentence(multi_sentence_non_pangram) == "No pangram"

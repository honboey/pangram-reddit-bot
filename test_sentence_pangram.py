from sentence_pangram import (
    reproduce_pangram_if_it_exists,
    determine_if_sentence_is_pangram,
    string_has_over_25_letters,
    isolate_z_sentence,
)

single_sentence_pangram = "The quick brown fox jumps over the lazy dog."
single_sentence_pangram_with_punctuation = (
    "The quick brown fox jumps over the lazy dog!"
)
multi_sentence_pangram = "Here is the first sentence. The quick brown fox jumps over the lazy dog. Here is the last sentence."
multi_sentence_pangram_with_punctuation = "Here is the first sentence. The quick brown fox jumps over the lazy dog! Here is the last sentence."
single_sentence_non_pangram = "This is not a pangram"
multi_sentence_non_pangram = (
    "Here is the first sentence. This is not a pangram. Here is the last sentence."
)


class TestReproducePangramIfItExists:
    def test_reproduce_pangram_if_it_exists__single_sentence_pangram(self):
        assert (
            reproduce_pangram_if_it_exists(single_sentence_pangram)
            == single_sentence_pangram
        )

    def test_reproduce_pangram_if_it_exists__single_sentence_pangram_with_punctuation(
        self,
    ):
        assert (
            reproduce_pangram_if_it_exists(single_sentence_pangram_with_punctuation)
            == single_sentence_pangram_with_punctuation
        )

    def test_reproduce_pangram_if_it_exists__multi_sentence_pangram(self):
        assert (
            reproduce_pangram_if_it_exists(multi_sentence_pangram)
            == single_sentence_pangram
        )

    def test_reproduce_pangram_if_it_exists__multi_sentence_pangram_with_punctuation(
        self,
    ):
        assert (
            reproduce_pangram_if_it_exists(multi_sentence_pangram_with_punctuation)
            == single_sentence_pangram_with_punctuation
        )

    def test_reproduce_pangram_if_it_exists__single_sentence_non_pangram(self):
        assert reproduce_pangram_if_it_exists(single_sentence_non_pangram) == None

    def test_reproduce_pangram_if_it_exists__multi_sentence_non_pangram(self):
        assert reproduce_pangram_if_it_exists(multi_sentence_non_pangram) == None


class TestStringHasOver25Letters:
    def test_string_has_over_25_letters__single_sentence(self):
        assert string_has_over_25_letters(single_sentence_pangram) == True

    def test_string_has_over_25_letters__multi_sentence(self):
        assert string_has_over_25_letters(multi_sentence_pangram) == True

    def test_string_has_over_25_letters__false(self):
        assert string_has_over_25_letters(single_sentence_non_pangram) == False


class TestIsolateZSentence:
    def test_isolate_z_sentence__single_sentence_pangram(self):
        assert (
            isolate_z_sentence(single_sentence_pangram)
            == "The quick brown fox jumps over the lazy dog."
        )

    def test_isolate_z_sentence__single_sentence_pangram_with_punctuation(self):
        assert (
            isolate_z_sentence(single_sentence_pangram_with_punctuation)
            == "The quick brown fox jumps over the lazy dog!"
        )

    def test_isolate_z_sentence__multi_sentence_pangram(self):
        assert (
            isolate_z_sentence(multi_sentence_pangram)
            == "The quick brown fox jumps over the lazy dog."
        )

    def test_isolate_z_sentence__multi_sentence_pangram_with_punctuation(self):
        assert (
            isolate_z_sentence(multi_sentence_pangram_with_punctuation)
            == "The quick brown fox jumps over the lazy dog!"
        )

    def test_isolate_z_sentence__multi_sentence_pangram(self):
        assert (
            isolate_z_sentence(multi_sentence_pangram)
            == "The quick brown fox jumps over the lazy dog."
        )

    def test_isolate_z_sentence__single_sentence_non_pangram(self):
        assert isolate_z_sentence(single_sentence_non_pangram) == "No pangram"

    def test_isolate_z_sentence__multi_sentence_non_pangram(self):
        assert isolate_z_sentence(multi_sentence_non_pangram) == "No pangram"


class TestDetermineIfSentenceIsPangram:
    def test_determine_if_sentence_is_pangram__single_sentence_pangram(self):
        assert determine_if_sentence_is_pangram(single_sentence_pangram) == True

    def test_determine_if_sentence_is_pangram__single_sentence_non_pangram(self):
        assert determine_if_sentence_is_pangram(single_sentence_non_pangram) == False

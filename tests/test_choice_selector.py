import unittest
from drqa.selector import ChoiceSelector
from drqa.reader import DocReader
from drqa.pipeline import DEFAULTS
from drqa.pipeline.drqa import init_tokenizer


class TestChoiceSelector(unittest.TestCase):
    def setUp(self):
        reader_model = 'data/reader/multitask.mdl'
        reader = DocReader.load(reader_model, normalize=False)
        init_tokenizer(DEFAULTS['tokenizer'], {})
        self.selector_ = ChoiceSelector(reader.word_dict, reader.network.embedding)

    def test_choice_selector(self):
        spans = ["By separately analyzing the security into a bond and the embedded option"]
        choices = ["Z-spread minus the option cost.",
                   "Z-spread plus the cost of the option.",
                   "value of the security's embedded option."]
        self.selector_.select_most_similar(spans, choices)
        pass


if __name__ == '__main__':
    unittest.main()
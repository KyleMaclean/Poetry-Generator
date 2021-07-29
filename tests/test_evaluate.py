from unittest import TestCase

import evaluate


class TestGetRhymeLevelScore(TestCase):

    def test_get_rhyme_level_score(self):
        score = evaluate.get_rhyme_level_score(['in the sunshine', 'there was no moon'])
        self.assertEqual(1, score)

    def test_get_rhyme_level_score2(self):
        score = evaluate.get_rhyme_level_score(['dear sunshine', 'please be mine'])
        self.assertEqual(2, score)

    def test_get_rhyme_level_score3(self):
        score = evaluate.get_rhyme_level_score(['there is one day', 'in the array'])
        self.assertEqual(1, score)

    def test_get_rhyme_level_score4(self):
        score = evaluate.get_rhyme_level_score(['a dainty butterfly', 'on my shoulder'])
        self.assertEqual(0, score)

    def test_get_rhyme_level_score5(self):
        score = evaluate.get_rhyme_level_score(['a dainty butterfly', 'on another butterfly'])
        self.assertEqual(0, score)


class TestGetAlliterationFrequencyScore(TestCase):

    def test_get_alliteration_frequency_score(self):
        couplet = ['pick up sticks in the forest', 'null']
        chain, occurrences = evaluate.get_alliteration_scores(couplet)
        self.assertEqual(0, occurrences)
        self.assertEqual(0, chain)

    def test_get_alliteration_frequency_score2(self):
        couplet = ['people pick up sticks', 'null']
        chain, occurrences = evaluate.get_alliteration_scores(couplet)
        self.assertEqual(1, occurrences)
        self.assertEqual(1, chain)

    def test_get_alliteration_frequency_score3(self):
        couplet = ['purple people pick up sticks', 'null']
        chain, occurrences = evaluate.get_alliteration_scores(couplet)
        self.assertEqual(2, occurrences)
        self.assertEqual(2, chain)

    def test_get_alliteration_frequency_score4(self):
        couplet = ['we water the purple plants', 'null']
        chain, occurrences = evaluate.get_alliteration_scores(couplet)
        self.assertEqual(2, occurrences)
        self.assertEqual(1, chain)


class TestGetCoupletPhonemeConsistencyScore(TestCase):
    def test_get_couplet_phoneme_consistency_score(self):
        couplet = ['we sat down', 'we sat down']
        score = evaluate.get_couplet_phoneme_consistency_score(couplet)
        self.assertEqual(10, score)

    def test_get_couplet_phoneme_consistency_score2(self):
        couplet = ['we sat down', 'we sat down too']
        score = evaluate.get_couplet_phoneme_consistency_score(couplet)
        self.assertEqual(8, score)

    def test_get_couplet_phoneme_consistency_score3(self):
        couplet = ['we sat down', 'we sat down there with you']
        score = evaluate.get_couplet_phoneme_consistency_score(couplet)
        self.assertEqual(2, score)

    def test_get_couplet_phoneme_consistency_score4(self):
        couplet = ['we sat down', 'we sat down there with you and all your friends']
        score = evaluate.get_couplet_phoneme_consistency_score(couplet)
        self.assertEqual(0, score)

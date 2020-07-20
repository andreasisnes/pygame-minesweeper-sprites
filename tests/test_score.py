import unittest
import pygame

try:
    from .context import minesweeper
except ImportError:
    from context import minesweeper
sprites = minesweeper.sprites

class TestScoreSheets(unittest.TestCase):
    def test_Init_ScoreSheetMonochrome_ToString(self):
        sheet = sprites.ScoreSheets(sprites.ScoreSheets.monochrome)
        self.assertEqual(sprites.ScoreSheets.monochrome, str(sheet))

    def test_Init_ScoreSheetTwoNine_ToString(self):
        sheet = sprites.ScoreSheets(sprites.ScoreSheets.two_thousand)
        self.assertEqual(sprites.ScoreSheets.two_thousand, str(sheet))

    def test_Init_WrongArguementType_RaiseException(self):
        self.assertRaises(ValueError, sprites.ScoreSheets, "testing")
        

class TestScoreBuilder(unittest.TestCase):
    def test_Init_DefaultSheet_ReturnNewBuilder(self):
        builder = sprites.ScoreBuilder()
        self.assertEqual(10 * 1, len(builder._sheet.keys()))
    
    def test_Init_WrongTypeOfArgument_RaiseTypeError(self):
        self.assertRaises(TypeError, sprites.ScoreBuilder, sprites.ScoreSheets.monochrome)
    
    def test_Init_MonochromeSheet_ValidateExcludedInternalSheetDictKeys(self):
        builder = sprites.ScoreBuilder(sprites.ScoreSheets(sprites.ScoreSheets.monochrome))
        self.assertFalse(any(["build" == x for x in builder._sheet.keys()]))
        self.assertFalse(any([x.startswith("__") for x in builder._sheet.keys()]))
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyZero(self):
        self.validate_key("zero")
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyOne(self):
        self.validate_key("one")
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyTwo(self):
        self.validate_key("two")
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyThree(self):
        self.validate_key("three")
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyFour(self):
        self.validate_key("four")

    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyFive(self):
        self.validate_key("five")

    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeySix(self):
        self.validate_key("six")

    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeySeven(self):
        self.validate_key("seven")

    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyEight(self):
        self.validate_key("eight")
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyNine(self):
        self.validate_key("nine")
    
    def test_SetZero_InvalidSheet_RaiseValueError(self):
        builder = sprites.ScoreBuilder(sprites.ScoreSheets(sprites.ScoreSheets.monochrome))
        self.assertRaises(TypeError, builder.zero, "testing")

    def validate_key(self, key):
        builder = sprites.ScoreBuilder(sprites.ScoreSheets(sprites.ScoreSheets.monochrome))
        self.assertTrue(key in builder._sheet.keys())
    
class TestScore(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1,1))
    
    def test_GetItem_IndexWith0_ReturnScoreZero(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.zero, score[0][0])
        self.assertEqual(score.zero, score["0"][0])
        self.assertIsInstance(score.zero, pygame.Surface)
        
    def test_GetItem_IndexWith1_ReturnScoreOne(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.one, score[1][0])
        self.assertEqual(score.one, score["1"][0])
        self.assertIsInstance(score.one, pygame.Surface)
    
    def test_GetItem_IndexWith2_ReturnScoreTwo(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.two, score[2][0])
        self.assertEqual(score.two, score["2"][0])
        self.assertIsInstance(score.two, pygame.Surface)
    
    def test_GetItem_IndexWith3_ReturnScoreThree(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.three, score[3][0])
        self.assertEqual(score.three, score["3"][0])
        self.assertIsInstance(score.three, pygame.Surface)
    
    def test_GetItem_IndexWith4_ReturnScoreFour(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.four, score[4][0])
        self.assertEqual(score.four, score["4"][0])
        self.assertIsInstance(score.four, pygame.Surface)
    
    def test_GetItem_IndexWith5_ReturnScoreFive(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.five, score[5][0])
        self.assertEqual(score.five, score["5"][0])
        self.assertIsInstance(score.five, pygame.Surface)
    
    def test_GetItem_IndexWith6_ReturnScoreSix(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.six, score[6][0])
        self.assertEqual(score.six, score["6"][0])
        self.assertIsInstance(score.six, pygame.Surface)
    
    def test_GetItem_IndexWith7_ReturnScoreSeven(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.seven, score[7][0])
        self.assertEqual(score.seven, score["7"][0])
        self.assertIsInstance(score.seven, pygame.Surface)
    
    def test_GetItem_IndexWith8_ReturnScoreEight(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.eight, score[8][0])
        self.assertEqual(score.eight, score["8"][0])
        self.assertIsInstance(score.eight, pygame.Surface)
    
    def test_GetItem_IndexWith9_ReturnScoreNine(self):
        score = sprites.ScoreBuilder().build()
        self.assertEqual(score.nine, score[9][0])
        self.assertEqual(score.nine, score["9"][0])
        self.assertIsInstance(score.nine, pygame.Surface)

class ScoreIntegrationTests(unittest.TestCase):
    def test_GlobalCache_TwoInstances_SameObject(self):
        tile_1 = sprites.ScoreBuilder().build().zero
        tile_2 = sprites.ScoreBuilder().build().zero
        self.assertEqual(tile_1, tile_2)
    
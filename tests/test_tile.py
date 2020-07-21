import unittest
import pygame

try:
    from .context import minesweeper
except ImportError:
    from context import minesweeper
sprites = minesweeper.sprites


class TestTileSheets(unittest.TestCase):
    def test_tile_sheet_two_to_string(self):
        sheet = sprites.TileSheets(sprites.TileSheets.two)
        self.assertEqual(sprites.TileSheets.two, str(sheet))

    def test_tile_sheet_two_nine_to_string(self):
        sheet = sprites.TileSheets(sprites.TileSheets.two_nine)
        self.assertEqual(sprites.TileSheets.two_nine, str(sheet))

    def test_tile_sheet_ninety_five_to_string(self):
        sheet = sprites.TileSheets(sprites.TileSheets.ninety_five)
        self.assertEqual(sprites.TileSheets.ninety_five, str(sheet))

    def test_tile_sheet_two_thousand_to_string(self):
        sheet = sprites.TileSheets(sprites.TileSheets.two_thousand)
        self.assertEqual(sprites.TileSheets.two_thousand, str(sheet))

    def test_tile_sheet_fiorito_two_thousand_to_string(self):
        sheet = sprites.TileSheets(sprites.TileSheets.fiorito_two_thousand)
        self.assertEqual(sprites.TileSheets.fiorito_two_thousand, str(sheet))

    def test_tile_sheet_fiorito_monochrome_to_string(self):
        sheet = sprites.TileSheets(sprites.TileSheets.fiorito_monochrome)
        self.assertEqual(sprites.TileSheets.fiorito_monochrome, str(sheet))

    def test_tile_sheet_fiorito_xp_to_string(self):
        sheet = sprites.TileSheets(sprites.TileSheets.fiorito_xp)
        self.assertEqual(sprites.TileSheets.fiorito_xp, str(sheet))

    def test_tile_sheet_monochrome_to_string(self):
        sheet = sprites.TileSheets(sprites.TileSheets.monochrome)
        self.assertEqual(sprites.TileSheets.monochrome, str(sheet))

    def test_wrong_arguement_type_raise_exception(self):
        self.assertRaises(ValueError, sprites.TileSheets, "testing")


class TestTileBuilder(unittest.TestCase):
    def test_Init_DefaultSheet_ReturnNewBuilder(self):
        builder = sprites.TileBuilder()
        self.assertEqual(8 * 2, len(builder._sheet.keys()))

    def test_Init_WrongTypeOfArgument_RaiseTypeError(self):
        self.assertRaises(TypeError, sprites.TileBuilder,
                          sprites.TileSheets.two)

    def test_Init_MonochromeSheet_ValidateExcludedInternalSheetDictKeys(self):
        builder = sprites.TileBuilder(
            sprites.TileSheets(sprites.TileSheets.monochrome))
        self.assertFalse(any(["build" == x for x in builder._sheet.keys()]))
        self.assertFalse(any([x.startswith("__")
                              for x in builder._sheet.keys()]))

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyUnopened(self):
        self.validate_key("unopened")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyEmpty(self):
        self.validate_key("empty")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyFlag(self):
        self.validate_key("flag")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyQuestionMark(self):
        self.validate_key("question_mark")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyQuestionMarkClick(self):
        self.validate_key("question_mark_click")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyMine(self):
        self.validate_key("mine")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyMineRed(self):
        self.validate_key("mine_red")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyMineRedCross(self):
        self.validate_key("mine_red_cross")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyOne(self):
        self.validate_key("one")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyTwo(self):
        self.validate_key("two")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyThree(self):
        self.validate_key("three")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyFour(self):
        self.validate_key("four")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyFive(self):
        self.validate_key("five")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeySix(self):
        self.validate_key("six")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeySeven(self):
        self.validate_key("seven")

    def test_Init_NinetyNineSheet_ValidateIncludedInternalSheetDictKeyEight(self):
        self.validate_key("eight")

    def validate_key(self, key):
        builder = sprites.TileBuilder(
            sprites.TileSheets(sprites.TileSheets.ninety_five))
        self.assertTrue(key in builder._sheet.keys())


class TestTile(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1, 1))

    def test_GetItem_IndexWith0_ReturnTileEmpty(self):
        tile = sprites.TileBuilder().build()
        self.assertEqual(tile.empty, tile[0])
        self.assertEqual(tile.empty, tile["0"])
        self.assertIsInstance(tile.empty, pygame.Surface)

    def test_GetItem_IndexWith1_ReturnTileOne(self):
        tile = sprites.TileBuilder().build()
        self.assertEqual(tile.one, tile[1])
        self.assertEqual(tile.one, tile["1"])
        self.assertIsInstance(tile.one, pygame.Surface)

    def test_GetItem_IndexWith2_ReturnTileTwo(self):
        tile = sprites.TileBuilder().build()
        self.assertEqual(tile.two, tile[2])
        self.assertEqual(tile.two, tile["2"])
        self.assertIsInstance(tile.two, pygame.Surface)

    def test_GetItem_IndexWith3_ReturnTileThree(self):
        tile = sprites.TileBuilder().build()
        self.assertEqual(tile.three, tile[3])
        self.assertEqual(tile.three, tile["3"])
        self.assertIsInstance(tile.three, pygame.Surface)

    def test_GetItem_IndexWith4_ReturnTileFour(self):
        tile = sprites.TileBuilder().build()
        self.assertEqual(tile.four, tile[4])
        self.assertEqual(tile.four, tile["4"])
        self.assertIsInstance(tile.four, pygame.Surface)

    def test_GetItem_IndexWith5_ReturnTileFive(self):
        tile = sprites.TileBuilder().build()
        self.assertEqual(tile.five, tile[5])
        self.assertEqual(tile.five, tile["5"])
        self.assertIsInstance(tile.five, pygame.Surface)

    def test_GetItem_IndexWith6_ReturnTileSix(self):
        tile = sprites.TileBuilder().build()
        self.assertEqual(tile.six, tile[6])
        self.assertEqual(tile.six, tile["6"])
        self.assertIsInstance(tile.six, pygame.Surface)

    def test_GetItem_IndexWith7_ReturnTileSeven(self):
        tile = sprites.TileBuilder().build()
        self.assertEqual(tile.seven, tile[7])
        self.assertEqual(tile.seven, tile["7"])
        self.assertIsInstance(tile.seven, pygame.Surface)

    def test_GetItem_IndexWith8_ReturnTileEight(self):
        tile = sprites.TileBuilder().build()
        self.assertEqual(tile.eight, tile[8])
        self.assertEqual(tile.eight, tile["8"])
        self.assertIsInstance(tile.eight, pygame.Surface)

    def test_GetItem_IndexWith9_RaiseValueError(self):
        self.assertRaises(
            ValueError, sprites.TileBuilder().build().__getitem__, 9)
        self.assertRaises(
            ValueError, sprites.TileBuilder().build().__getitem__, "9")

    def test_Unopened_Property_PygameSurface(self):
        tile = sprites.TileBuilder().build().unopened
        self.assertIsInstance(tile, pygame.Surface)

    def test_Flag_Property_PygameSurface(self):
        tile = sprites.TileBuilder().build().flag
        self.assertIsInstance(tile, pygame.Surface)

    def test_QuestionMark_Property_PygameSurface(self):
        tile = sprites.TileBuilder().build().question_mark
        self.assertIsInstance(tile, pygame.Surface)

    def test_QuestionMarkClick_Property_PygameSurface(self):
        tile = sprites.TileBuilder().build().question_mark_click
        self.assertIsInstance(tile, pygame.Surface)

    def test_Mine_Property_PygameSurface(self):
        tile = sprites.TileBuilder().build().mine
        self.assertIsInstance(tile, pygame.Surface)

    def test_MineRed_Property_PygameSurface(self):
        tile = sprites.TileBuilder().build().mine_red
        self.assertIsInstance(tile, pygame.Surface)

    def test_MineRedCross_Property_PygameSurface(self):
        tile = sprites.TileBuilder().build().mine_red_cross
        self.assertIsInstance(tile, pygame.Surface)


class TileIntegrationTests(unittest.TestCase):
    def test_GlobalCache_TwoInstances_SameObject(self):
        tile_1 = sprites.TileBuilder().build().mine_red_cross
        tile_2 = sprites.TileBuilder().build().mine_red_cross
        self.assertEqual(tile_1, tile_2)


if __name__ == '__main__':
    unittest.main()

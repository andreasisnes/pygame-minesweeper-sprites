import unittest
import pygame

try:
    from .context import minesweeper
except ImportError:
    from context import minesweeper
sprites = minesweeper.sprites

class TestFaceSheets(unittest.TestCase):
    def test_Init_FaceSheetMonochrome_ToString(self):
        sheet = sprites.FaceSheets(sprites.FaceSheets.monochrome)
        self.assertEqual(sprites.FaceSheets.monochrome, str(sheet))

    def test_Init_FaceSheetTwoNine_ToString(self):
        sheet = sprites.FaceSheets(sprites.FaceSheets.two_thousand)
        self.assertEqual(sprites.FaceSheets.two_thousand, str(sheet))

    def test_Init_WrongArguementType_RaiseException(self):
        self.assertRaises(ValueError, sprites.FaceSheets, "testing")

class TestFaceBuilder(unittest.TestCase):
    def test_Init_DefaultSheet_ReturnNewBuilder(self):
        builder = sprites.FaceBuilder()
        self.assertEqual(5 * 1, len(builder._sheet.keys()))
    
    def test_Init_WrongTypeOfArgument_RaiseTypeError(self):
        self.assertRaises(TypeError, sprites.FaceBuilder, sprites.FaceSheets.monochrome)
    
    def test_Init_MonochromeSheet_ValidateExcludedInternalSheetDictKeys(self):
        builder = sprites.FaceBuilder(sprites.FaceSheets(sprites.FaceSheets.monochrome))
        self.assertFalse(any(["build" == x for x in builder._sheet.keys()]))
        self.assertFalse(any([x.startswith("__") for x in builder._sheet.keys()]))
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeySmile(self):
        self.validate_key("smile")
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeySmileClick(self):
        self.validate_key("smile_click")
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyExcited(self):
        self.validate_key("excited")
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyWinner(self):
        self.validate_key("winner")
    
    def test_Init_Monochrome_ValidateIncludedInternalSheetDictKeyDead(self):
        self.validate_key("dead")

    def validate_key(self, key):
        builder = sprites.FaceBuilder(sprites.FaceSheets(sprites.FaceSheets.monochrome))
        self.assertTrue(key in builder._sheet.keys())

class TestFace(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1,1))
    
    def test_Smile_Property_PygameSurface(self):
        face = sprites.FaceBuilder().build().smile
        self.assertIsInstance(face, pygame.Surface)

    def test_Dead_Property_PygameSurface(self):
        face = sprites.FaceBuilder().build().dead
        self.assertIsInstance(face, pygame.Surface)

    def test_Excited_Property_PygameSurface(self):
        face = sprites.FaceBuilder().build().excited
        self.assertIsInstance(face, pygame.Surface)

    def test_SmileClick_Property_PygameSurface(self):
        face = sprites.FaceBuilder().build().smile_click
        self.assertIsInstance(face, pygame.Surface)

    def test_Winner_Property_PygameSurface(self):
        face = sprites.FaceBuilder().build().winner
        self.assertIsInstance(face, pygame.Surface)

class FaceIntegrationTests(unittest.TestCase):
    def test_GlobalCache_TwoInstances_SameObject(self):
        tile_1 = sprites.FaceBuilder().build().winner
        tile_2 = sprites.FaceBuilder().build().winner
        self.assertEqual(tile_1, tile_2)
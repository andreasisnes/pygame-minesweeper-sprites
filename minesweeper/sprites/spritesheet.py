from os.path import join, dirname
import pygame


class Spritesheet:
    """ Spritesheet """

    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print("Unable to load spritesheet image: %s" % filename)
            raise SystemExit(message)

    def image_at(self, rectangle, colorkey=None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey=None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_grid(self, grid, colorkey=None):
        "load grids of images and returns them as a list"
        rects = []
        size_x = self.sheet.get_width() // grid[0]
        size_y = self.sheet.get_height() // grid[1]
        for pos_y in range(0, self.sheet.get_height(), size_y):
            for pos_x in range(0, self.sheet.get_width(), size_x):
                rects.append((pos_x, pos_y, size_x, size_y))
        return self.images_at(rects, colorkey)


class SpritesheetIndex:
    def __init__(self, sheet, index: int):
        self.sheet = sheet
        self.index = index


class SpritesheetBuilder:
    def __init__(self, sheet, sheet_type):
        self._sheet = {}
        self._sheet_type = sheet_type
        if isinstance(sheet, self._sheet_type):
            self.__init_sheet__(sheet)
        else:
            self.__type_error__()

    def __init_sheet__(self, sheet):
        for method in [method for method in dir(self) if self.__exclusive__(method)]:
            getattr(self, method)(sheet)

    def __exclusive__(self, method: str) -> bool:
        return callable(getattr(self, method)) and not any(method.startswith(x) for x in ["__", "build"])

    def __setter__(self, sheet, name: str, index: int):
        if not isinstance(sheet, self._sheet_type):
            self.__type_error__()
        self._sheet[name] = SpritesheetIndex(sheet, index)

    def __type_error__(self):
        raise TypeError("Argument 'sheet' is not of type '{}'".format(
            self._sheet_type.__name__))


def new_spritesheet(folder: str, file: str) -> Spritesheet:
    return Spritesheet(join(dirname(dirname(__file__)), "images", folder, file + ".png"))


def spritesheet_faces(file: str) -> Spritesheet:
    return new_spritesheet("faces", file)


def spritesheet_scores(file: str) -> Spritesheet:
    return new_spritesheet("scores", file)


def spritesheet_tiles(file: str) -> Spritesheet:
    return new_spritesheet("tiles", file)

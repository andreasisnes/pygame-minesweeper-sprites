from .spritesheet import spritesheet_faces, SpritesheetIndex, SpritesheetBuilder
from pygame import Surface

_face_cache = {}


class FaceSheets:
    two_thousand = "2000"
    monochrome = "monochrome"
    __sheets__ = [
        two_thousand,
        monochrome
    ]

    def __init__(self, sheet: str):
        if str(sheet) not in self.__sheets__:
            raise ValueError("Argument 'sheet = {}' is not valid. Must be either {}".format(
                sheet, self.__sheets__))
        self._sheet = str(sheet)

    def __str__(self):
        return self._sheet


class Face:
    def __init__(self, faces: dict):
        self._faces = faces

    @property
    def smile(self) -> Surface:
        return self.__load__(self._faces["smile"])

    @property
    def smile_click(self) -> Surface:
        return self.__load__(self._faces["smile_click"])

    @property
    def excited(self) -> Surface:
        return self.__load__(self._faces["excited"])

    @property
    def winner(self) -> Surface:
        return self.__load__(self._faces["winner"])

    @property
    def dead(self) -> Surface:
        return self.__load__(self._faces["dead"])

    def __load__(self, face_index: SpritesheetIndex) -> Surface:
        sheet = str(face_index.sheet)
        if sheet not in _face_cache:
            _face_cache[sheet] = spritesheet_faces(sheet).load_grid((5, 1))
        return _face_cache[sheet][face_index.index]


class FaceBuilder(SpritesheetBuilder):
    def __init__(self, sheet=FaceSheets(FaceSheets.two_thousand)):
        super().__init__(sheet, FaceSheets)

    def smile(self, sheet: FaceSheets) -> 'FaceBuilder':
        self.__setter__(sheet, self.smile.__name__, 0)
        return self

    def smile_click(self, sheet: FaceSheets) -> 'FaceBuilder':
        self.__setter__(sheet, self.smile_click.__name__, 1)
        return self

    def excited(self, sheet: FaceSheets) -> 'FaceBuilder':
        self.__setter__(sheet, self.excited.__name__, 2)
        return self

    def winner(self, sheet: FaceSheets) -> 'FaceBuilder':
        self.__setter__(sheet, self.winner.__name__, 3)
        return self

    def dead(self, sheet: FaceSheets) -> 'FaceBuilder':
        self.__setter__(sheet, self.dead.__name__, 4)
        return self

    def build(self) -> Face:
        return Face(self._sheet)

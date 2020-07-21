from .spritesheet import spritesheet_tiles, SpritesheetIndex, SpritesheetBuilder
from pygame import Surface

_tile_cache = {}


class TileSheets:
    two = "2.0"
    two_nine = "2.9"
    ninety_five = "95"
    two_thousand = "2000"
    fiorito_two_thousand = "fiorito-2000"
    fiorito_monochrome = "fiorito-monochrome"
    fiorito_xp = "fiorito-xp"
    monochrome = "monochrome"

    __sheets__ = [
        two,
        two_nine,
        ninety_five,
        two_thousand,
        fiorito_two_thousand,
        fiorito_monochrome,
        fiorito_xp,
        monochrome
    ]

    def __init__(self, sheet: str):
        if str(sheet) not in self.__sheets__:
            raise ValueError("Argument 'sheet = {}' is not valid. Must be either {}".format(
                sheet, self.__sheets__))
        self._sheet = str(sheet)

    def __str__(self):
        return self._sheet


class Tile:
    def __init__(self, tiles: dict):
        self._tiles = tiles
        self._num2method = {
            "0": lambda: self.empty,
            "1": lambda: self.one,
            "2": lambda: self.two,
            "3": lambda: self.three,
            "4": lambda: self.four,
            "5": lambda: self.five,
            "6": lambda: self.six,
            "7": lambda: self.seven,
            "8": lambda: self.eight,
        }

    @property
    def unopened(self) -> Surface:
        return self.__load__(self._tiles["unopened"])

    @property
    def empty(self) -> Surface:
        return self.__load__(self._tiles["empty"])

    @property
    def flag(self) -> Surface:
        return self.__load__(self._tiles["flag"])

    @property
    def question_mark(self) -> Surface:
        return self.__load__(self._tiles["question_mark"])

    @property
    def question_mark_click(self) -> Surface:
        return self.__load__(self._tiles["question_mark_click"])

    @property
    def mine(self) -> Surface:
        return self.__load__(self._tiles["mine"])

    @property
    def mine_red(self) -> Surface:
        return self.__load__(self._tiles["mine_red"])

    @property
    def mine_red_cross(self) -> Surface:
        return self.__load__(self._tiles["mine_red_cross"])

    @property
    def one(self) -> Surface:
        return self.__load__(self._tiles["one"])

    @property
    def two(self) -> Surface:
        return self.__load__(self._tiles["two"])

    @property
    def three(self) -> Surface:
        return self.__load__(self._tiles["three"])

    @property
    def four(self) -> Surface:
        return self.__load__(self._tiles["four"])

    @property
    def five(self) -> Surface:
        return self.__load__(self._tiles["five"])

    @property
    def six(self) -> Surface:
        return self.__load__(self._tiles["six"])

    @property
    def seven(self) -> Surface:
        return self.__load__(self._tiles["seven"])

    @property
    def eight(self) -> Surface:
        return self.__load__(self._tiles["eight"])

    def __load__(self, tile_index: SpritesheetIndex):
        sheet = str(tile_index.sheet)
        if sheet not in _tile_cache:
            _tile_cache[sheet] = spritesheet_tiles(sheet).load_grid((8, 2))
        return _tile_cache[sheet][tile_index.index]

    def __getitem__(self, value: int):
        if int(value) >= 0 and int(value) < 9:
            return self._num2method[str(value)]()
        raise ValueError(
            "Argument 'value = {}' must be in range 0 < value < 9".format(value))


class TileBuilder(SpritesheetBuilder):
    def __init__(self, sheet=TileSheets(TileSheets.two_thousand)):
        super().__init__(sheet, TileSheets)

    def unopened(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.unopened.__name__, 0)
        return self

    def empty(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.empty.__name__, 1)
        return self

    def flag(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.flag.__name__, 2)
        return self

    def question_mark(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.question_mark.__name__, 3)
        return self

    def question_mark_click(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.question_mark_click.__name__, 4)
        return self

    def mine(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.mine.__name__, 5)
        return self

    def mine_red(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.mine_red.__name__, 6)
        return self

    def mine_red_cross(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.mine_red_cross.__name__, 7)
        return self

    def one(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.one.__name__, 8)
        return self

    def two(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.two.__name__, 9)
        return self

    def three(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.three.__name__, 10)
        return self

    def four(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.four.__name__, 11)
        return self

    def five(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.five.__name__, 12)
        return self

    def six(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.six.__name__, 13)
        return self

    def seven(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.seven.__name__, 14)
        return self

    def eight(self, sheet: TileSheets) -> 'TileBuilder':
        self.__setter__(sheet, self.eight.__name__, 15)
        return self

    def build(self) -> Tile:
        return Tile(self._sheet)

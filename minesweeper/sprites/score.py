from .spritesheet import spritesheet_scores, SpritesheetIndex, SpritesheetBuilder
from pygame import Surface

_score_cache = {}


class ScoreSheets:
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


class Score:
    def __init__(self, scores: dict):
        self._scores = scores
        self._num2method = {
            "0": lambda: self.zero,
            "1": lambda: self.one,
            "2": lambda: self.two,
            "3": lambda: self.three,
            "4": lambda: self.four,
            "5": lambda: self.five,
            "6": lambda: self.six,
            "7": lambda: self.seven,
            "8": lambda: self.eight,
            "9": lambda: self.nine,
        }

    @property
    def zero(self) -> Surface:
        return self.__load__(self._scores["zero"])

    @property
    def one(self) -> Surface:
        return self.__load__(self._scores["one"])

    @property
    def two(self) -> Surface:
        return self.__load__(self._scores["two"])

    @property
    def three(self) -> Surface:
        return self.__load__(self._scores["three"])

    @property
    def four(self) -> Surface:
        return self.__load__(self._scores["four"])

    @property
    def five(self) -> Surface:
        return self.__load__(self._scores["five"])

    @property
    def six(self) -> Surface:
        return self.__load__(self._scores["six"])

    @property
    def seven(self) -> Surface:
        return self.__load__(self._scores["seven"])

    @property
    def eight(self) -> Surface:
        return self.__load__(self._scores["eight"])

    @property
    def nine(self) -> Surface:
        return self.__load__(self._scores["nine"])

    def __load__(self, score_index: SpritesheetIndex):
        sheet = str(score_index.sheet)
        if sheet not in _score_cache:
            _score_cache[sheet] = spritesheet_scores(sheet).load_grid((10, 1))
        return _score_cache[sheet][score_index.index]

    def __getitem__(self, value):
        return [self._num2method[i]() for i in str(value)]


class ScoreBuilder(SpritesheetBuilder):
    def __init__(self, sheet=ScoreSheets(ScoreSheets.two_thousand)):
        super().__init__(sheet, ScoreSheets)

    def zero(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.zero.__name__, 0)
        return self

    def one(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.one.__name__, 1)
        return self

    def two(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.two.__name__, 2)
        return self

    def three(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.three.__name__, 3)
        return self

    def four(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.four.__name__, 4)
        return self

    def five(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.five.__name__, 5)
        return self

    def six(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.six.__name__, 6)
        return self

    def seven(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.seven.__name__, 7)
        return self

    def eight(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.eight.__name__, 8)
        return self

    def nine(self, sheet: ScoreSheets) -> 'ScoreBuilder':
        self.__setter__(sheet, self.nine.__name__, 9)
        return self

    def build(self) -> Score:
        return Score(self._sheet)

from enum import Enum


class Screen(Enum):
    loading = 'loading_screen'
    main = 'main_screen'
    pokestop = 'pokestop_screen'
    unknown = 'unknown_screen'


def detect_screen() -> Screen:
    return Screen.unknown

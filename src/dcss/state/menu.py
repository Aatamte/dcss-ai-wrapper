from enum import Enum


class Menu(Enum):
    NO_MENU = 1
    CHARACTER_CREATION_SELECT_SPECIES = 2
    CHARACTER_CREATION_SELECT_BACKGROUND = 3
    CHARACTER_CREATION_SELECT_WEAPON = 4
    CHARACTER_INVENTORY_MENU = 5
    CHARACTER_ITEM_SPECIFIC_MENU = 6
    TUTORIAL_SELECTION_MENU = 7
    SPRINT_MAP_SELECTION_MENU = 8
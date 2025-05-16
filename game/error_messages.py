from enum import StrEnum

class ErrorMsg(StrEnum):
    CodeHasNotEnoughSigns = "Not enough signs entered."
    CodeHasInvalidSigns = "Invalid signs entered."
    CodeHasTooManySigns = "Too many signs entered."
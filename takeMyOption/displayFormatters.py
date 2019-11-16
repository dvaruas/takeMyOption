from .displayFrame import DisplayFrame
from .exceptions import DisplayFrameException
from .options import OptionData


def getDefaultDisplayFormatter(optionDataObj):
    displayFormat = DisplayFrame()

    if not isinstance(optionDataObj, OptionData):
        raise DisplayFrameException(displayFormat, "optionDataObj argument "
            "must be an instance of OptionData class")

    displayFormat.startFrameRow(showBorder=False)
    displayFormat.frameData(optionDataObj.getBanner(), align="center", colSpan=2)
    displayFormat.endFrameRow()

    displayFormat.startFrameRow()
    displayFormat.frameData("-", align="fill", colSpan=2)
    displayFormat.endFrameRow()

    optionsIDs = optionDataObj.getAllOptionIDs()
    for id in optionsIDs:
        displayFormat.startFrameRow()
        displayFormat.frameData(id, align="right")
        displayFormat.frameData(optionDataObj.getOptionText(id))
        displayFormat.endFrameRow()

    displayFormat.insertBlankRow(colSpan=2)

    return displayFormat

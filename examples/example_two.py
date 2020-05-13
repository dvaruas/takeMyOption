from takeMyOption.displayFormatters import getDefaultDisplayFormatter
from takeMyOption.inputStrategies import InputStrategies
from takeMyOption.options import OptionData

"""This example shows how to create a custom Display Format to show Options.

Output of a run :

|======================|
|    Options at Home   |
| -------------------- |
|    1  |  Read        | Reading is Fun
|    2  |  Movies      | Movies is also Fun
|    3  |  Study       | Study is not so Fun
|    4  |  Sleep       | Sleeping means no Fun

What do you want to do today (1/2/3/4) [4] :

Selected Option : 4
"""
if __name__ == "__main__":
    option_obj = OptionData()

    read_option = option_obj.addNewOption("Read", add="Reading is Fun")
    movie_option = option_obj.addNewOption("Movies", add="Movies is also Fun")
    study_option = option_obj.addNewOption("Study", add="Study is not so Fun")
    sleep_option = option_obj.addNewOption("Sleep", add="Sleeping means no Fun")

    option_obj.setBanner("Options at Home")
    option_obj.setPrompt("What do you want to do today")
    option_obj.setDefaultOption(sleep_option)

    display_formatter = DisplayFrame()

    display_formatter.startFrameRow()
    display_formatter.frameData("=", align="fill", colSpan=2)
    display_formatter.frameData(" ")
    display_formatter.endFrameRow()

    display_formatter.startFrameRow()
    display_formatter.frameData(optionDataObj.getBanner(), align="center", colSpan=2)
    display_formatter.frameData(" ")
    display_formatter.endFrameRow()

    display_formatter.startFrameRow()
    display_formatter.frameData()
    display_formatter = getDefaultDisplayFormatter(optionDataObj=option_obj)
    get_input = InputStrategies(prompt=option_obj.getPrompt())

    print(display_formatter.render(divider=" | ", leftBorder="|"))
    opt = get_input.inputAnOption(options=option_obj.getAllOptionIDs(),
            showOptions=True, defaultInput=option_obj.getDefaultOption())
    print("\nSelected Option : {}".format(opt))

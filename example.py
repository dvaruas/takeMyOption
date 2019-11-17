from takeMyOption.displayFormatters import getDefaultDisplayFormatter
from takeMyOption.inputStrategies import InputStrategies
from takeMyOption.options import OptionData


option_obj = OptionData()

read_option = option_obj.addNewOption("Read")
movie_option = option_obj.addNewOption("Movies")
study_option = option_obj.addNewOption("Study")
sleep_option = option_obj.addNewOption("Sleep")

option_obj.setBanner("Options at Home")
option_obj.setPrompt("What do you want to do today")
option_obj.setDefaultOption(sleep_option)

display_formatter = getDefaultDisplayFormatter(optionDataObj=option_obj)
get_input = InputStrategies(prompt=option_obj.getPrompt())

print(display_formatter.render(divider=" | ", leftBorder="|", rightBorder="|"))
opt = get_input.inputAnOption(options=option_obj.getAllOptionIDs(),
        showOptions=True, defaultInput=option_obj.getDefaultOption())
print("\nSelected Option : {}".format(opt))

from .exceptions import OptionException


class OptionData:
    def __init__(self, strictCheck=True):
        self.__banner = "Options"
        self.__options = {}
        self.__default_option = None
        self.__prompt = "Enter choice"
        self.__strictCheck = strictCheck

    def setBanner(self, bannerText):
        if bannerText and isinstance(bannerText, str):
            self.__banner = bannerText
        elif self.__strictCheck:
            raise OptionException(self, "bannerText argument must be a valid string, "
                "invalid entry : {}(type : {})".format(bannerText, type(bannerText).__name__))

    def getBanner(self):
        return self.__banner

    def setPrompt(self, prompt):
        if prompt and isinstance(prompt, str):
            self.__prompt = prompt
        elif self.__strictCheck:
            raise OptionException(self, "prompt argument must be a valid string, "
                "invalid entry : {}(type : {})".format(prompt, type(prompt).__name__))

    def getPrompt(self):
        return self.__prompt

    def addNewOption(self, optionText, optionID=None, **kwargs):
        if optionID != None and type(optionID) not in [str, int]:
            if self.__strictCheck:
                raise OptionException(self, "optionID specified must be of either "
                    "integer or string type. Invalid Entry : {}(type : {})"
                    .format(optionID, type(optionID).__name__))
            else:
                optionID = None

        if not optionID:
            try_value = 1
            while True:
                if try_value in self.__options or str(try_value) in self.__options:
                    try_value += 1
                else:
                    optionID = str(try_value)
                    break
        elif not isinstance(optionID, str):
            optionID = str(optionID)

        if optionText and isinstance(optionText, str):
            self.__options[optionID] = {"text" : optionText, **kwargs}
        elif self.__strictCheck:
            raise OptionException(self, "optionText argument must be a valid string, "
                "invalid entry : {}(type : {})".format(optionText, type(optionText).__name__))
        return optionID

    def setDefaultOption(self, optionID):
        if str(optionID) in self.__options:
            self.__default_option = str(optionID)
        elif self.__strictCheck:
            raise OptionException(self, "optionID must be an among already added options, "
                "use addNewOption to add the option first before setting it to default")

    def getOptionText(self, optionID):
        if str(optionID) not in self.__options:
            raise OptionException(self, "optionID {} provided was not found among "
                "options set".format(optionID))
        return self.__options[str(optionID)]["text"]

    def getOptionArgs(self, optionID):
        if str(optionID) not in self.__options:
            raise OptionException(self, "optionID {} provided was not found among "
                "options set".format(optionID))
        args = dict(self.__options[str(optionID)])
        args.pop("text")
        return args

    def getAllOptionIDs(self):
        return list(self.__options.keys())

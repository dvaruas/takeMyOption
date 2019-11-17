from .exceptions import OptionException


class OptionData:
    def __init__(self, strictCheck=True):
        """Constructor for OptionData.

        Args:
            strictCheck: Whether to strictly check entries made as options. (Boolean, default : True)
                         Better to have it as True, else might cause inconsistencies.

        Raises:
            OptionException: If strictCheck is not a Boolean Value.
        """
        if not isinstance(strictCheck, bool):
            raise OptionException(self, "strictCheck argument must be Boolean, "
                "invalid value : {}(type : {})".format(strictCheck, type(strictCheck).__name__))
        self.__banner = "Options"
        self.__options = {}
        self.__default_option = None
        self.__prompt = "Enter choice"
        self.__strictCheck = strictCheck

    def setBanner(self, bannerText="Options"):
        """Set the banner for the options.

        Args:
            bannerText: Text to be the banner for the options. (String, default : "Options")

        Raises:
            OptionException: if bannerText is not a valid String.
        """
        if bannerText and isinstance(bannerText, str):
            self.__banner = bannerText
        elif self.__strictCheck:
            raise OptionException(self, "bannerText argument must be a valid string, "
                "invalid value : {}(type : {})".format(bannerText, type(bannerText).__name__))

    def getBanner(self):
        """Return the banner for the options."""
        return self.__banner

    def setPrompt(self, prompt="Enter choice"):
        """Set the prompt text for options.

        Args:
            prompt: Text to be the prompt for the options. (String, default : "Enter choice")

        Raises:
            OptionException: if prompt is not a valid String.
        """
        if prompt and isinstance(prompt, str):
            self.__prompt = prompt
        elif self.__strictCheck:
            raise OptionException(self, "prompt argument must be a valid string, "
                "invalid value : {}(type : {})".format(prompt, type(prompt).__name__))

    def getPrompt(self):
        """Return the prompt for the options."""
        return self.__prompt

    def addNewOption(self, optionText, optionID=None, **kwargs):
        """Add a new option choice.

        Args:
            optionText: Text to display with the Option. (String)
            optionID: The ID to be associated with this option. (String or Integer, default : None)
                      If not provided, one will be generated internally.
            **kwargs : Additional Keyword arguments associated with option.

        Returns:
            The optionID for this option. (String)
            Returns None if strictCheck is disabled and option was not inserted.

        Raises:
            OptionException: If optionID is not a valid Integer or String.
                             If optionText is not a valid String.
        """
        if optionID != None and type(optionID) not in [str, int]:
            if self.__strictCheck:
                raise OptionException(self, "optionID specified must be of either "
                    "integer or string type, invalid value : {}(type : {})"
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
                "invalid value : {}(type : {})".format(optionText, type(optionText).__name__))
        else:
            return None
        return optionID

    def setDefaultOption(self, optionID):
        """Set a default option among the Options.

        Args:
            optionID: The option ID to be set as default. (String)

        Raises:
            OptionException: If the option ID has not been added as an option previously.
        """
        if str(optionID) in self.__options:
            self.__default_option = str(optionID)
        elif self.__strictCheck:
            raise OptionException(self, "optionID must be an among already added options, "
                "use addNewOption to add the option first before setting it to default")

    def getDefaultOption(self):
        """Return the default option ID."""
        return self.__default_option

    def getOptionText(self, optionID):
        """Return the Option Text for given ID.

        Args:
            optionID: The ID for which to get option text. (String)

        Returns:
            Text for the Option. (String)

        Raises:
            OptionException: If the optionID provided was not found.
        """
        if str(optionID) not in self.__options:
            raise OptionException(self, "optionID {} provided was not found among "
                "options set".format(optionID))
        return self.__options[str(optionID)]["text"]

    def getOptionArgs(self, optionID):
        """Return dictionary of additional keyword arguments saved with an option.

        Args:
            optionID: The ID for which to return keyword arguments.

        Returns:
            Keyword Arguments. (Dictionary)

        Raises:
            OptionException: If the optionID provided was not found.
        """
        if str(optionID) not in self.__options:
            raise OptionException(self, "optionID {} provided was not found among "
                "options set".format(optionID))
        args = dict(self.__options[str(optionID)])
        args.pop("text")
        return args

    def getAllOptionIDs(self):
        """Return all the option IDs set."""
        return list(self.__options.keys())

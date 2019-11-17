from .exceptions import DisplayFrameException


class DisplayFrame:
    def __init__(self):
        self.__rows = {}
        self.__current_row = []
        self.__padding = 1
        self.__row_indx = -1

    def setPadding(self, paddingVal):
        """Set padding value for the Display Frame.

        Args:
            paddingVal: padding value (Integer)

        Raises:
            DisplayFrameException: If paddingVal is not a positive integer.
        """
        if not isinstance(paddingVal, int):
            raise DisplayFrameException(self, "paddingVal argument should be an integer, "
                "invalid value : {}(type : {})".format(paddingVal, type(paddingVal).__name__))
        elif paddingVal < 0:
            raise DisplayFrameException(self, "paddingVal argument cannot be less than zero")
        self.__padding = paddingVal

    def startFrameRow(self, showBorder=True, showDivider=True):
        """Start a new row in the Display Frame.

        Args:
            showBorder: Determines whether to display Border for the row. (Boolean, default : True)
            showDivider: Determines whether to display divider between rows. (Boolean, default : True)

        Raises:
            DisplayFrameException: If showBorder or showDivider is not a boolean value.
        """
        if not isinstance(showBorder, bool):
            raise DisplayFrameException(self, "showBorder argument should be a boolean, "
                "invalid value : {}(type : {})".format(showBorder, type(showBorder).__name__))
        if not isinstance(showDivider, bool):
            raise DisplayFrameException(self, "showDivider argument should be a boolean, "
                "invalid value : {}(type : {})".format(showDivider, type(showDivider).__name__))
        self.__row_indx += 1
        self.__rows[self.__row_indx] = {"data" : [], "showBorder" : showBorder,
            "showDivider" : showDivider}
        self.__current_row = []

    def frameData(self, data, align="left", colSpan=1):
        """Add a data cell to the Display Frame Row.

        Args:
            data: The Raw data which is to be added to the cell. (String)
            align: Alignment choice for cell data. (String, default : "left")
                   Valid align choices :
                   "left" : left-align the data
                   "right" : right-align the data
                   "center" : center-align the data
                   "fill" : fill the complete cell width with data repeated
            colSpan: Number of columns the cell spans for. (Integer, default : 1)

        Raises:
            DisplayFrameException: If align is not a valid keyword or
                                   if colSpan is not a positive Integer
        """
        if align not in ["left", "right", "center", "fill"]:
            raise DisplayFrameException(self, "align argument has to be one among"
                " these options - left, right, center, fill. Invalid value : "
                "{}(type : {})".format(align, type(align).__name__))
        if not isinstance(colSpan, int) or colSpan <= 0:
            raise DisplayFrameException(self, "colSpan argument has to be a positive"
                " integer value. Invalid value : {}(type : {})"
                .format(colSpan, type(colSpan).__name__))
        self.__current_row.append([str(data), align, colSpan])

    def endFrameRow(self):
        """End a row in the Display Frame."""
        if self.__current_row:
            self.__rows[self.__row_indx]["data"] = self.__current_row

    def insertBlankRow(self, colSpan=1):
        """Insert a completely Blank Row.

        Args:
            colSpan: Number of columns the cell spans for. (Integer, default : 1)

        Raises:
            DisplayFrameException: If colSpan is not a positive Integer
        """
        if not isinstance(colSpan, int) or colSpan <= 0:
            raise DisplayFrameException(self, "colSpan argument has to be a positive"
                " integer value. Invalid value : {}(type : {})"
                .format(colSpan, type(colSpan).__name__))
        self.__row_indx += 1
        self.__rows[self.__row_indx] = {"data" : [(" ", "fill", colSpan)],
            "showBorder" : False, "showDivider" : False}

    def __measureColumnWidths(self, dividerLen):
        __columnWidths = {}
        __span = 1
        while True:
            __no_more_update = True
            for __row_indx in self.__rows.keys():
                __row = self.__rows[__row_indx]["data"]
                __i = 0
                for (__c_data, __c_align, __c_span) in __row:
                    if __c_span == __span:
                        __no_more_update = False
                        __width_now = sum([__columnWidths.get(__j, 0) \
                            for __j in range(__i, __i + __span)]) + (dividerLen * (__span - 1))
                        __data_len = len(__c_data)
                        while __width_now < __data_len:
                            for __j in range(__i, __i + __span):
                                __columnWidths[__j] = __columnWidths.get(__j, 0) + 1
                                __width_now += 1
                    __i += 1
            if __no_more_update:
                break
            __span += 1
        return __columnWidths

    def render(self, divider=" ", leftBorder="", rightBorder=""):
        """Renders the complete Display Frame.

        Args:
            divider: The divider to use between columns in Frame. (String, default : " ")
            leftBorder : The left-most border for the Frame. (String, default : "")
            rightBorder : The right-most border for the Frame. (String, default : "")

        Returns:
            The complete Display Frame to be printed. (String)

        Raises:
            DisplayFrameException: If either of divider, leftBorder or rightBorder
                                   is not a String.
        """
        for (__n, __t) in [("divider", divider), ("leftBorder", leftBorder), ("rightBorder", rightBorder)]:
            if not isinstance(__t, str):
                raise DisplayFrameException(self, "{} argument should be a String,"
                    " invalid value : {}(type : {})".format(__n, __t, type(__t).__name__))

        __col_widths = self.__measureColumnWidths(dividerLen=len(divider))

        __row_strings = []
        for __row_indx in sorted(self.__rows.keys()):
            __row = self.__rows[__row_indx]["data"]
            __showBorder = self.__rows[__row_indx]["showBorder"]
            __showDivider = self.__rows[__row_indx]["showDivider"]
            __row_str = []
            __col_index = 0
            for (__col_data, __col_align, __col_span) in __row:
                __col_width = sum([__col_widths[__i] \
                    for __i in range(__col_index, __col_index + __col_span)]) \
                    + ((len(divider) + (2 * self.__padding)) * (__col_span - 1))
                __row_cell_data = ""
                if __col_align == "left":
                    __row_cell_data = "{s:<{w}}".format(s=__col_data, w=__col_width)
                elif __col_align == "right":
                    __row_cell_data = "{s:>{w}}".format(s=__col_data, w=__col_width)
                elif __col_align == "center":
                    __row_cell_data = "{s:^{w}}".format(s=__col_data, w=__col_width)
                elif __col_align == "fill":
                    __row_cell_data = __col_data * __col_width
                    __row_cell_data = __row_cell_data[:__col_width]
                __row_str.append("{padding}{data}{padding}".format(
                    padding=" " * self.__padding,
                    data=__row_cell_data))
                __col_index += 1
            __row_strings.append("{lBorder}{content}{rBorder}".format(
                lBorder=leftBorder if __showBorder else " ",
                rBorder=rightBorder if __showBorder else " ",
                content=divider.join(__row_str) if __showDivider else " ".join(__row_str)))
        return "\n".join(__row_strings)

    def clearFrame(self):
        """Clear all data from the current Display Frame."""
        self.__rows = {}
        self.__current_row = []
        self.__row_indx = -1

    def __str__(self):
        return self.render()

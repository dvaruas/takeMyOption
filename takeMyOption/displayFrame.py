import math

from .exceptions import DisplayFrameException


class DisplayFrame:
    def __init__(self):
        self.__rows = {}
        self.__current_row = []
        self.__padding = 1
        self.__row_indx = -1

    def setPadding(self, padding_val):
        if not isinstance(padding_val, int):
            raise DisplayFrameException(self, "padding_val argument should be an integer, "
                "invalid entry : {}(type : {})".format(padding_val, type(padding_val).__name__))
        self.__padding = padding_val

    def startFrameRow(self, showBorder=True, showDivider=True):
        self.__row_indx += 1
        self.__rows[self.__row_indx] = {"data" : [], "showBorder" : showBorder,
            "showDivider" : showDivider}
        self.__current_row = []

    def frameData(self, data, align="left", colSpan=1):
        self.__current_row.append([data, align, colSpan])

    def endFrameRow(self):
        if self.__current_row:
            self.__rows[self.__row_indx]["data"] = self.__current_row

    def insertBlankRow(self, colSpan=1):
        self.__row_indx += 1
        self.__rows[self.__row_indx] = {"data" : [(" ", "fill", colSpan)],
            "showBorder" : False, "showDivider" : False}

    def measureColumnWidths(self, dividerLen):
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
        for (__n, __t) in [("divider", divider), ("leftBorder", leftBorder), ("rightBorder", rightBorder)]:
            if not isinstance(__t, str):
                raise DisplayFrameException(self, "{} argument should be a String,"
                    " invalid entry : {}(type : {})".format(__n, __t, type(__t).__name__))

        __col_widths = self.measureColumnWidths(dividerLen=len(divider))

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
        self.__rows = {}
        self.__current_row = []
        self.__row_indx = -1

    def __str__(self):
        return self.render()

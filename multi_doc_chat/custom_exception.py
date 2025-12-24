import sys
import traceback


class DocumentPortalException(Exception):
    def __init__(self, message: str, error: Exception | None = None):
        exc_type, exc_value, exc_tb = sys.exc_info()

        if error and error.__traceback__:
            exc_type = type(error)
            exc_value = error
            exc_tb = error.__traceback__

        if exc_tb:
            while exc_tb.tb_next:
                exc_tb = exc_tb.tb_next
            self.file_name = exc_tb.tb_frame.f_code.co_filename
            self.line_no = exc_tb.tb_lineno
        else:
            self.file_name = "<unknown>"
            self.line_no = -1

        self.message = message

        self.traceback_str = (
            "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
            if exc_type and exc_tb
            else ""
        )

        super().__init__(self.__str__())

    def __str__(self):
        base = (
            f"Error in [{self.file_name}] at line [{self.line_no}] "
            f"| Message: {self.message}"
        )
        return f"{base}\nTraceback:\n{self.traceback_str}**************" if self.traceback_str else base

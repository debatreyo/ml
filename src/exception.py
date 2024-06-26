# for fetching details on raised exceptions
import sys
# for logging exceptions
import logging


# custom error message
def error_message_detail(error:str, error_detail:sys):
    """
    Returns a custom error message
    that can be shown to the user for
    debugging purpose.
    """
    # sys.exc_info() returns ->
    # Exception type,
    # Exception value,
    # Traceback object (point where the exception last occured)
    
    _, _, exc_traceback = error_detail.exc_info()

    # python file name where exception was raised
    file_name = exc_traceback.tb_frame.f_code.co_filename
    # line number in the .py sript where exception was raised
    line_number = exc_traceback.tb_lineno
    # error message
    error_message = str(error)

    # custom error message
    custom_error_message = f"Error occured in Python script named {file_name} at line no. {line_number}. Error message: {error_message}"

    return custom_error_message

# custom exception
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)

        # get and store custom error message
        self.custom_error_message = error_message_detail(error=error_message, error_detail=error_detail)

    def __str__(self):
        return self.custom_error_message
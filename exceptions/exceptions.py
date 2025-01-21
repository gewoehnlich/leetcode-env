class NoFilesSelectedException(Exception):
    def __init__(self):
        error_message = ( 
            "You have to select at least one HTML file!"
        )

        super().__init__(error_message)

class ParseException(Exception):
    def __init__(self):
        error_message = (
            "Something went wrong while parsing the file!"
        )

        super().__init__(error_message)


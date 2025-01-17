"""
Module for validating citations
"""
import re

class UserInputError(Exception):
    """
    UserInputError
    """


class CitationService(): # pylint: disable=too-few-public-methods
    """
    Class for validating citations
    """

    def __init__(self):
        self.cite_as = ""
        self.fieldtypes = ""

    def validate(self, citation):
        """
        Function checks citations on fields that are prone to errors
        """
        cite_as = citation.cite_as
        fields = citation.fieldtypes

        checked = ["month","year","doi","chapter","volume","pages"]

        if len(cite_as) < 2:
            raise UserInputError("Cite should be over two characters long")

        for field in fields:
            if field[0] == "month" and (not re.match('[0-1][0-9]{1}',
                str(field[1])) or int(field[1]) > 12):

                raise UserInputError("Month should be a valid month in form of: ##")

            if field[0] == "year" and (not re.match('[1-3][0-9]{3}', str(field[1]))):
                raise UserInputError("Not a valid year")

            if field[0] == "doi" and (not re.match('^10[.][0-9]{4,}', str(field[1]))):
                raise UserInputError("Not a valid doi")

            if field[0] == "chapter" or field[0] == "volume":
                if not re.match('[0-9]', str(field[1])):
                    raise UserInputError("Chapter and/or volume should be a number(s)")

            if field[0] == "pages" and (not re.match('[0-9,;]', str(field[1]))):
                raise UserInputError("Page numbers should be separated either by ',' or ';' ")

            if field[0] not in checked and len(str(field[1])) < 2:
                raise UserInputError("Text fields should contain atleast two characters")

        return True

__all__ = ["FieldsDatabase"]

class FieldsDatabase(object):

    FIELDS_DB = "Fields.db"

    def __init__(self):
        """Initialize the class.
        """
        self.fields_db_name = self.FIELDS_DB

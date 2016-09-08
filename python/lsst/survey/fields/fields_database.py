from __future__ import unicode_literals

import os
import sqlite3

__all__ = ["FieldsDatabase"]

class FieldsDatabase(object):

    FIELDS_DB = "Fields.db"
    """Internal file containing the standard 3.5 degree FOV survey field information."""

    def __init__(self):
        """Initialize the class.
        """
        self.fields_db_name = self.FIELDS_DB
        self.connect = sqlite3.connect(os.path.join(os.path.dirname(__file__), self.fields_db_name))

    def __del__(self):
        """Delete the class.
        """
        self.connect.close()


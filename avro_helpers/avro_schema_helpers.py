"""
    Purpose:
        Avro Schema Helpers.

        This library is used to interact with .avsc files
"""

# Python Library Imports
import logging
import os
from avro.schema import Parse

# Local Library Imports
from avro_helpers.avro_exceptions import AvscInvalid, AvscNotFound


###
# Schema Helpers
###


def get_schema_from_avsc_file(avsc_filename):
    """
    Purpose:
        Get the file schema from an .avsc filename (with path in the filename)
    Args:
        avsc_filename (String): Path/filename of the .avsc file to get the schema from
    Return:
        avro_schema (AVRO Schema Object): Schema object from the avro library
    """
    logging.info(f"Getting AVRO Schema from {avsc_filename}")

    if not os.path.isfile(avsc_filename):
        raise AvscNotFound(f"{avsc_filename} not found")

    avro_schema = None
    try:
        with open(avsc_filename) as avsc_file_obj:
            avro_schema = Parse(avsc_file_obj.read())
    except Exception as err:
        error_msg = f"Error Reading {avsc_filename} into Schema: {err}"
        logging.exception(error_msg)
        raise AvscInvalid(error_msg)

    return avro_schema

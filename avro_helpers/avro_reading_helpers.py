"""
    Purpose:
        Avro Reading Helpers.

        This library is used to aid in the task of reading .avro files
"""

# Python Library Imports
import logging
import os
from avro.datafile import DataFileReader
from avro.io import DatumReader

# Local Library Imports
from avro_helpers.avro_exceptions import AvroNotFound


###
# Reading Helpers
###


def get_record_from_avro_generator(avro_filename):
    """
    Purpose:
        Generator of records from a .avro filename (with path in the filename)
    Args:
        avro_filename (String): Path/filename of the .avro file to get records from
    Yields:
        avro_record (Record Obj from .avro): Record read from the .avro file
    """
    logging.info(f"Generating Records from {avro_filename}")

    if not os.path.isfile(avro_filename):
        raise AvroNotFound(f"{avro_filename} not found")

    with open(avro_filename, "rb") as avro_binary_reader:
        avro_reader = DataFileReader(avro_binary_reader, DatumReader())
        for avro_record in avro_reader:
            yield avro_record


def get_record_from_avro_buffered(avro_filename):
    """
    Purpose:
        Buffered Get records from a .avro filename (with path in the filename)
    Args:
        avro_filename (String): Path/filename of the .avro file to get records from
    Returns:
        avro_records (List of Record Objs from .avro): List of Records read from
            the .avro file
    """
    logging.info(f"Getting Records from {avro_filename}")

    if not os.path.isfile(avro_filename):
        raise AvroNotFound(f"{avro_filename} not found")

    avro_records = []
    with open(avro_filename, "rb") as avro_binary_reader:
        avro_reader = DataFileReader(avro_binary_reader, DatumReader())
        avro_records = [avro_record for avro_record in avro_reader]

    return avro_records

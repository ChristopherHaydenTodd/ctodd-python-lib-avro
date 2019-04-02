"""
    Purpose:
        Avro Converter Helpers.

        This library is used to convert avro to other formats (first .json)
"""

# Python Library Imports
import logging
import os
import simplejson as json
from avro.datafile import DataFileReader
from avro.io import DatumReader

# Local Library Imports
from avro_helpers import avro_reading_helpers
from avro_helpers.avro_exceptions import AvroNotFound


###
# Converter Helpers
###


def convert_avro_file_to_json(avro_filename, json_filename=None):
    """
    Purpose:
        Convert an .avro file into a .json file
    Args:
        avro_filename (String): Path/filename of the .avro file to convert to .json
        json_filename (String): Path/filename of the .json file to generate. if none
            is specified, just use the same .avro path and change the extension
    Yields:
        json_filename (String): Path/filename of the .json file generated
    """

    if not json_filename:
        json_filename = avro_filename.replace(".avro", ".json")

    logging.info(f"Getting .avro records from {avro_filename}")
    avro_records = avro_reading_helpers.get_record_from_avro_buffered(avro_filename)

    logging.info(f"Converting {avro_filename} into {json_filename}")
    with open(json_filename, "w") as json_file_obj:
        json.dump(
            avro_records, json_file_obj, sort_keys=True, indent=4, separators=(',', ': ')
        )

#!/usr/bin/env python3
"""
    Purpose:
        Convert an .avro File into a .json file

    Steps:
        - Either
            - Read .avro File as Buffered List
            - Write records to .json file

    function call:python3 convert_avro_to_json.py --avro="./data/test_data.avro"
"""

# Python Library Imports
import logging
import os
import sys
from argparse import ArgumentParser

# Local Library Imports
from avro_helpers import avro_converter_helpers


def main():
    """
    Purpose:
        Read an .avro File
    """
    print("Starting .avro Converting Process")

    opts = get_options()

    json_filename = avro_converter_helpers.convert_avro_file_to_json(
        opts.avro_filename, json_filename=opts.json_filename
    )

    print(".avro Converting Process Complete")


###
# General/Helper Methods
###


def get_options():
    """
    Purpose:
        Parse CLI arguments for script
    Args:
        N/A
    Return:
        N/A
    """

    parser = ArgumentParser(description="Read .avro File")
    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    # Optional Arguments
    optional.add_argument(
        "--json",
        dest="json_filename",
        help="Filename (and path) of .json file to write",
        required=False,
    )

    # Required Arguments
    required.add_argument(
        "--avro",
        dest="avro_filename",
        help="Filename (and path) of .avro file to read",
        required=True,
    )

    return parser.parse_args()


if __name__ == "__main__":

    log_level = logging.INFO
    logging.getLogger().setLevel(log_level)
    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format="[convert_avro_to_json] %(asctime)s %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S"
    )

    try:
        main()
    except Exception as err:
        print(
            "{0} failed due to error: {1}".format(os.path.basename(__file__), err)
        )
        raise err

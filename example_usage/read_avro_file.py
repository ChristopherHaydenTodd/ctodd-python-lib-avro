#!/usr/bin/env python3
"""
    Purpose:
        Read an .avro File

    Steps:
        - Either
            - Read .avro File as Buffered List
            - Read .avro File as Generator

    function call:python3 read_avsc_file.py --avro="./data/test_data.avro"
"""

# Python Library Imports
import logging
import os
import sys
from argparse import ArgumentParser

# Local Library Imports
BASE_PROJECT_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/../"
sys.path.insert(0, BASE_PROJECT_PATH)
from avro_helpers import avro_reading_helpers


def main():
    """
    Purpose:
        Read an .avro File
    """
    print("Starting .avro Reading Process")

    opts = get_options()

    # avro_records = avro_reading_helpers.get_record_from_avro_buffered(opts.avro_filename)
    for avro_record in avro_reading_helpers.get_record_from_avro_generator(opts.avro_filename):
        import pdb; pdb.set_trace()

    import pdb; pdb.set_trace()

    print(".avro Reading Process Complete")


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
    # N/A

    # Required Arguments
    required.add_argument(
        "--avro",
        dest="avro_filename",
        help="Filename (and path) of .avro file to read",
        required=True,
    )

    return parser.parse_args()


if __name__ == "__main__":

    try:
        main()
    except Exception as err:
        print(
            "{0} failed due to error: {1}".format(os.path.basename(__file__), err)
        )
        raise err

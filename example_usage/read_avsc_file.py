#!/usr/bin/env python3.6
"""
    Purpose:
        Read an .avsc File to get the schema

    Steps:
        - Read .avsc Schema

    function call:
        python3.6 read_avsc_file.py {--avsc=avsc_filename}

    example call:
        python3.6 read_avsc_file.py --avsc="./avsc/test_schema.avsc"
"""

# Python Library Imports
import logging
import os
import sys
from argparse import ArgumentParser

# Local Library Imports
BASE_PROJECT_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/../"
sys.path.insert(0, BASE_PROJECT_PATH)
from avro_helpers import avro_schema_helpers


def main():
    """
    Purpose:
        Read an .avro File
    """
    print("Starting .avsc Reading Process")

    opts = get_options()

    avro_schema = avro_schema_helpers.get_schema_from_avsc_file(opts.avsc_filename)

    import pdb; pdb.set_trace()

    print(".avsc Reading Process Complete")


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

    parser = ArgumentParser(description="Read .avsc File")
    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    # Optional Arguments
    # N/A

    # Required Arguments
    required.add_argument(
        "--avsc",
        dest="avsc_filename",
        help="Filename (and path) of .avsc file to read",
        required=True,
    )

    return parser.parse_args()


if __name__ == "__main__":

    log_level = logging.INFO
    logging.getLogger().setLevel(log_level)
    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format="[read_avsc_file] %(asctime)s %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S"
    )

    try:
        main()
    except Exception as err:
        print(
            "{0} failed due to error: {1}".format(os.path.basename(__file__), err)
        )
        raise err

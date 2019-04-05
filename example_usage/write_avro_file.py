datingd #!/usr/bin/env python3.6
"""
    Purpose:
        Write an .avro File

    Steps:
        - Either
            - Write .avro File

    function call:
        python3.6 write_avro_file.py {--avro=avro_filename} \
            {--avsc=avsc_filename}

    example call:
        python3.6 write_avro_file.py --avro="./data/generated_data.avro" \
            --avsc="./avsc/test_schema.avsc"
"""

# Python Library Imports
import logging
import os
import sys
from argparse import ArgumentParser

# Local Library Imports
BASE_PROJECT_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/../"
sys.path.insert(0, BASE_PROJECT_PATH)
from avro_helpers import avro_writing_helpers
from avro_helpers import avro_schema_helpers


def main():
    """
    Purpose:
        Read an .avro File
    """
    logging.info("Starting .avro Writing Process")

    opts = get_options()

    if opts.avsc_filename:
        avro_schema =\
            avro_schema_helpers.get_schema_from_avsc_file(opts.avsc_filename)
    else:
        avro_schema =\
            avro_schema_helpers.get_schema_from_avsc_file("./avsc/User.avsc")

    raw_records = [
        {
            "name": "Person 1",
            "favorite_number": 1,
            "favorite_color": "Purple",
        },
        {
            "name": "Person 2",
            "favorite_number": 2,
        },
        {
            "name": "Person 3",
            "favorite_color": "Gold",
        },
    ]

    serialized_records =\
        avro_writing_helpers.serialize_data(raw_records, avro_schema)

    avro_writing_helpers.write_raw_records_to_avro(
        raw_records, opts.avro_filename, avro_schema
    )

    logging.info(".avro Writing Process Complete")


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

    parser = ArgumentParser(description="Write .avro File")
    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    # Optional Arguments
    optional.add_argument(
        "--avsc",
        dest="avsc_filename",
        help="Filename (and path) of .avsc file to read",
        required=False,
    )

    # Required Arguments
    required.add_argument(
        "--avro",
        dest="avro_filename",
        help="Filename (and path) of .avro file to write",
        required=True,
    )

    return parser.parse_args()


if __name__ == "__main__":

    log_level = logging.INFO
    logging.getLogger().setLevel(log_level)
    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format="[write_avro_file] %(asctime)s %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S"
    )

    try:
        main()
    except Exception as err:
        print(
            "{0} failed due to error: {1}".format(os.path.basename(__file__), err)
        )
        raise err

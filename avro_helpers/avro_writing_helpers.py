"""
    Purpose:
        Avro Writing Helpers.

        This library is used to aid in the task of writing .avro files
"""

# Python Library Imports
import logging
import avro
import avro.io
import avro.schema
import io


###
# Writing Helpers
###


def write_raw_records_to_avro(raw_records, avro_filename, avro_schema):
    """
    Purpose:
        Write Records to .avro File
    Args:
        raw_records (List of Dicts): List of Recrods to Write to AVRO as Bytes
        avro_filename (String): Filename and path of .avro to write
        avro_schema (AVRO Schema Object): Schema object from the avro library
    Returns:
        N/A
    """
    logging.info(f"Writing Records To {avro_filename}")

    datum_writer = avro.io.DatumWriter()

    with open(avro_filename, "wb") as avro_file_obj:

        avro_writer = avro.datafile.DataFileWriter(
            avro_file_obj, datum_writer, avro_schema
        )

        for record in raw_records:
            avro_writer.append(record)
        avro_writer.flush()

    logging.info(f"Complete Writing Records To {avro_filename}")


###
# Serialization Helpers
###


def serialize_data(raw_records, avro_schema):
    """
    Purpose:
        Serialize a record as bytes
    Args:
        raw_records (List of Dicts): List of Records to Serialize
        avro_schema (AVRO Schema Object): Schema object from the avro library
    Return:
        serialized_records (List of Byte Array): Records Serialized into Byte-Array
    """

    bytes_writer = io.BytesIO()

    avro_writer = avro.io.DatumWriter(avro_schema)
    avro_encoder = avro.io.BinaryEncoder(bytes_writer)

    serialized_records = []
    for record in raw_records:
        avro_writer.write(record, avro_encoder)
        serialized_records.append(bytes_writer.getvalue())

    return serialized_records

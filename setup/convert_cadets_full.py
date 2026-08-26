import ast
import json
import glob
import os
from datetime import datetime, timezone

import pyarrow.parquet as pq

"""
Adjust if needed 
"""

INPUT_DIR = "/home/splunk_user/cadets/parquet"
OUTPUT_DIR = "/home/splunk_user/cadets/splunk"

ROWS_PER_FILE = 250000
BATCH_SIZE = 50000

os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_record_info(datum):
    if not isinstance(datum, dict) or not datum:
        return "Unknown", None, None

    key = next(iter(datum))
    record_type = key.split(".")[-1]

    inner = datum[key]

    timestamp_nanos = None

    if isinstance(inner, dict):
        timestamp_nanos = inner.get("timestampNanos")

    return record_type, inner, timestamp_nanos


def nanos_to_iso(timestamp_nanos):
    if timestamp_nanos is None:
        return None

    seconds = timestamp_nanos / 1_000_000_000

    dt = datetime.fromtimestamp(
        seconds,
        tz=timezone.utc
    )

    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def open_output(chunk_number):
    path = os.path.join(
        OUTPUT_DIR,
        f"cadets_{chunk_number:05d}.ndjson"
    )

    print(f"Writing: {path}")

    return open(path, "w", encoding="utf-8"), path


parquet_files = sorted(
    glob.glob(os.path.join(INPUT_DIR, "*"))
)

print(f"Found {len(parquet_files)} parquet files.")

chunk_number = 1
rows_in_chunk = 0
total_rows = 0
failed_rows = 0

outfile, current_path = open_output(chunk_number)

try:

    for parquet_path in parquet_files:

        print(f"\nReading: {parquet_path}")

        pf = pq.ParquetFile(parquet_path)

        for batch in pf.iter_batches(
            batch_size=BATCH_SIZE,
            columns=["datum", "CDMVersion", "source"]
        ):

            table = batch.to_pydict()

            for datum_raw, cdm_version, source in zip(
                table["datum"],
                table["CDMVersion"],
                table["source"]
            ):

                try:

                    datum = ast.literal_eval(datum_raw)

                    record_type, inner, timestamp_nanos = \
                        get_record_info(datum)

                    record = {
                        "record_type": record_type,
                        "CDMVersion": cdm_version,
                        "source": source,
                        "event_time": nanos_to_iso(timestamp_nanos),
                        "timestampNanos": timestamp_nanos,
                        "datum": datum
                    }

                    outfile.write(
                        json.dumps(
                            record,
                            separators=(",", ":")
                        ) + "\n"
                    )

                    rows_in_chunk += 1
                    total_rows += 1

                except Exception as e:

                    failed_rows += 1

                    if failed_rows <= 20:
                        print(f"Failed row: {e}")

                if rows_in_chunk >= ROWS_PER_FILE:

                    outfile.close()

                    print(
                        f"Completed chunk {chunk_number}: "
                        f"{rows_in_chunk:,} events"
                    )

                    chunk_number += 1
                    rows_in_chunk = 0

                    outfile, current_path = \
                        open_output(chunk_number)

finally:
    outfile.close()


# Remove the final empty chunk if one was created
if rows_in_chunk == 0 and os.path.exists(current_path):
    os.remove(current_path)
    chunk_number -= 1


print()
print("Conversion complete")
print(f"Total events: {total_rows:,}")
print(f"Failed rows: {failed_rows:,}")
print(f"Output chunks: {chunk_number}")

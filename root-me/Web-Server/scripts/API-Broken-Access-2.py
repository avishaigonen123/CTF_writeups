import uuid
import datetime
import sys

def regenerate_uuid_list(ref_uuid_str, ref_dt, target_dt, delta_ticks=100):
    ref_uuid = uuid.UUID(ref_uuid_str)

    # Extract node and clock sequence
    node = ref_uuid.node
    clock_seq = ref_uuid.clock_seq

    # UUID epoch
    uuid_epoch = datetime.datetime(1582, 10, 15)

    # Reference timestamp in 100-ns intervals
    ref_intervals = int((ref_dt - uuid_epoch).total_seconds() * 10_000_000)

    # Base target timestamp in 100-ns intervals
    delta_intervals = int((target_dt - ref_dt).total_seconds() * 10_000_000)
    target_intervals_base = ref_intervals + delta_intervals

    uuids = []

    for tick_offset in range(-delta_ticks, delta_ticks + 1):  # ±delta_ticks ticks
        ts_intervals = target_intervals_base + tick_offset

        time_low = ts_intervals & 0xFFFFFFFF
        time_mid = (ts_intervals >> 32) & 0xFFFF
        time_hi_and_version = ((ts_intervals >> 48) & 0x0FFF) | (1 << 12)  # version 1

        # Correctly set variant bits in clock_seq_hi_and_reserved
        clock_seq_hi = ((clock_seq >> 8) & 0x3F) | 0x80  # top two bits = 10
        clock_seq_low = clock_seq & 0xFF

        new_uuid = uuid.UUID(fields=(
            time_low,
            time_mid,
            time_hi_and_version,
            clock_seq_hi,
            clock_seq_low,
            node
        ))
        uuids.append(str(new_uuid))

    return uuids


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_uuid.py <ref_token> <ref_time> <target_time>")
        print("Time format: YYYY-MM-DD_HH:MM:SS.ssssss")
        sys.exit(1)

    ref_token = sys.argv[1]
    ref_time = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d_%H:%M:%S.%f")
    target_time = datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d_%H:%M:%S.%f")

    possible_uuids = regenerate_uuid_list(ref_token, ref_time, target_time, delta_ticks=10)

    for u in possible_uuids:
        print(u)

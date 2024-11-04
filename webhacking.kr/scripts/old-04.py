import hashlib
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def generate_hash(start, end):
    """Generate hashed values for a given range with 500 SHA-1 iterations per value."""
    result = []
    for i in range(start, end):
        data = f"{i}salt_for_you"
        hashed_data = data
        for _ in range(500):
            hashed_data = hashlib.sha1(hashed_data.encode()).hexdigest()
        result.append(f"{data}: {hashed_data}\n")
    return result

def process_and_write(filename, ranges, batch_size=100000):
    """Processes hash ranges in parallel and writes results to file in batches."""
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(generate_hash, start, end): (start, end) for start, end in ranges}
        completed_batches = 0
        start_time = time.time()

        with open(filename, 'w') as file:
            for future in as_completed(futures):
                batch = future.result()
                file.writelines(batch)
                completed_batches += 1

                # Progress and timing updates
                elapsed_time = time.time() - start_time
                estimated_total_time = (elapsed_time / completed_batches) * len(ranges)
                remaining_time = estimated_total_time - elapsed_time
                print(f"Completed batch {completed_batches}/{len(ranges)}. "
                      f"Estimated time left: {remaining_time / 60:.2f} minutes.")

    print("All data written to file.")

if __name__ == "__main__":
    # Configuration
    start_range = 10000000
    end_range = 99999999
    batch_size = 100000

    # Creating ranges to distribute across processes
    ranges = [(i, min(i + batch_size, end_range)) for i in range(start_range, end_range, batch_size)]
    print(f"Total batches to process: {len(ranges)}")

    # Process and write to file
    output_file = "optimized_hash_dictionary.txt"
    process_and_write(output_file, ranges)

    total_time = time.time() - time.time()
    print(f"All batches completed in {total_time / 60:.2f} minutes.")

def split_file(input_file, output_prefix, tracking_data_file, chunk_size=500, tracking_interval=50):
    with open(input_file, 'r') as f:
        data = [line.strip() for line in f.readlines()]  # Remove leading/trailing whitespace

    num_chunks = (len(data) + chunk_size - 1) // chunk_size

    with open(tracking_data_file, 'r') as tracking:
        tracking_data = tracking.read().strip()

    for i in range(num_chunks):
        chunk_start = i * chunk_size
        chunk_end = (i + 1) * chunk_size
        chunk = data[chunk_start:chunk_end]

        # Insert tracking data every tracking_interval entries in each chunk
        for j in range(tracking_interval, chunk_size, tracking_interval):
            chunk.insert(j, tracking_data)

        output_file = f"{output_prefix}_{i + 1}.txt"
        with open(output_file, 'w') as f:
            f.write('\n'.join(chunk))

# Prompt user for chunk size and tracking interval
def prompt_parameters():
    while True:
        try:
            chunk_size = int(input("Enter the amount of data to split (chunk size): "))
            tracking_interval = int(input("Enter the interval for adding tracking data: "))
            if chunk_size > 0 and tracking_interval > 0:
                return chunk_size, tracking_interval
            else:
                print("Please enter positive numbers.")
        except ValueError:
            print("Please enter valid numbers.")

# Example usage:
input_file = 'large_data.txt'
output_prefix = 'split_data_chunk'
tracking_data_file = 'tracking_data.txt'

chunk_size, tracking_interval = prompt_parameters()  # Prompt user for chunk size and tracking interval
split_file(input_file, output_prefix, tracking_data_file, chunk_size, tracking_interval)

import datetime

# Define the function to process the input file
def extract_prices(input_file):
    try:
        # Get the current date and time for the filename
        current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        output_file = f"{current_time}_output.txt"

        # Open the input file and process the lines
        with open(input_file, "r") as infile:
            lines = infile.readlines()

        # Extract lines that start with "$"
        prices = [line.strip() for line in lines if line.strip().startswith("$")]

        # Write the extracted prices to the output file
        with open(output_file, "w") as outfile:
            outfile.write("\n".join(prices))

        print(f"Prices have been written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the input file name
input_file = "input.txt"

# Call the function
extract_prices(input_file)
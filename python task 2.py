# Task 2: Write and Append Data to a File

def write_and_append():
    file_name = "output.txt"

    try:
        # Write to file
        text = input("Enter text to write to the file: ")
        with open(file_name, "w") as file:
            file.write(text + "\n")
        print("Data successfully written to output.txt.\n")

        # Append to file
        additional_text = input("Enter additional text to append: ")
        with open(file_name, "a") as file:
            file.write(additional_text + "\n")
        print("Data successfully appended.\n")

        # Read final content
        print("Final content of output.txt:\n")
        with open(file_name, "r") as file:
            print(file.read())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    write_and_append()
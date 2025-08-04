def get_valid_filename():
    """
    Prompt the user for a filename and handle potential errors.
    Returns the filename if valid, None otherwise.
    """
    while True:
        try:
            filename = input("Enter the name of the file to read: ")
            with open(filename, 'r') as file:
                pass  # Just checking if file can be opened
            return filename
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except PermissionError:
            print(f"Error: Permission denied when trying to read '{filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        
        retry = input("Would you like to try another filename? (yes/no): ").lower()
        if retry != 'yes':
            return None

def process_file_content(content):
    """
    Process the file content. This example converts text to uppercase.
    Modify this function to implement different transformations as needed.
    """
    return content.upper()

def main():
    print("=== File Processing Program ===")
    
    # Get input filename with error handling
    input_filename = get_valid_filename()
    if not input_filename:
        print("No valid filename provided. Exiting...")
        return
    
    # Read the input file
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
            
        # Process the content
        modified_content = process_file_content(content)
        
        # Create output filename
        output_filename = f"modified_{input_filename}"
        
        # Write to output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
            
        print(f"Success! Modified content has been written to '{output_filename}'")
        
    except Exception as e:
        print(f"An error occurred while processing the file: {str(e)}")

if __name__ == "__main__":
    main()

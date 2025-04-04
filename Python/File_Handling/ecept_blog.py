try:
    """
    Try to open the file and read its content.
    Additional operations can be performed here, such as counting words or processing the file data.
    """
    file = open('example.txt', 'r')
    content = file.read()
    print("File Content:\n")
    print(content)
    
    word_count = len(content.split())
    print(f"\nTotal Word Count: {word_count}")

except FileNotFoundError:
    """
    Handle the case where the file is not found.
    """
    print("Error: The file does not exist.")
    
except PermissionError:
    """
    Handle the case where there are insufficient permissions to access the file.
    """
    print("Error: You do not have permission to access the file.")
    
except IOError as e:
    """
    Handle input/output errors that may occur when reading from the file.
    """
    print(f"IO Error: {e}")

except Exception as e:
    """
    Catch any other unexpected exceptions.
    """
    print(f"An unexpected error occurred: {e}")
    
else:
    """
    This block will execute if no exceptions were raised in the try block.
    It confirms that the file reading was successful.
    """
    print("\nFile reading was successful.")
    
finally:
    """
    This block will always execute, regardless of whether an exception occurred or not.
    It's used to clean up resources, like closing the file.
    """
    try:
        if 'file' in locals():  # Check if the file was successfully opened
            file.close()
            print("\nFile has been closed.")
    except NameError:
        print("\nFile was not opened, no need to close.")

    print("\nFinally block executed. Cleanup done.")

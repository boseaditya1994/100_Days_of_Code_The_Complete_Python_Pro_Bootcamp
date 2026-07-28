def format_name(first_name, last_name):
    """
    Formats the first and last name with proper capitalization.
    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
    Returns:
        str: The formatted full name with proper capitalization.
    """
    formatted_name = f"{first_name.title()} {last_name.title()}"
    return formatted_name;

formatted_name = format_name("Aditya", "Bose")
print(formatted_name)  # Output: Aditya Bose
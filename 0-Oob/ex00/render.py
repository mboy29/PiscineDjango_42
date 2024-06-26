# Imports
# -------
import sys
import settings


# Tools
# -----

def t_err(msg: str, usage: bool = False, code: int = 1) -> None:
    """
    Prints an error message in red and, if required, 
    the usage of the program.

    Parameters:
        msg (str) - The error message to print.
        usage (bool) - Whether to print the usage of 
            the program, defaults to False.    
        code (int) - The error code to exit, defaults
            to 1.

    Returns: None
    """
    print(f"\033[0;31m[ERROR] {msg}\033[0m")
    if usage:
        print("\033[0;33m[USAGE] python3 render.py <template file>\033[0m")
    exit(code)

def t_open(path: str) -> str:
    """
    Opens a file and returns its content. 
    Also checks if the file exists, is not a directory and 
    is readable.

    Parameters:
        path (str) - The path to the file to open.

    Returns:
        str - The content of the file.
    """
    try:
        # check if path ends with .template
        if not path.endswith(".template"):
            raise Exception(f"'{path}' is not a .template file.")
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise Exception(f"'{path}' does not exist.")
    except IsADirectoryError:
        return t_err(f"'{path}' is a directory.")
    except PermissionError:
        return t_err(f"No permission to read '{path}'.")
    except Exception as exc:
        return t_err(exc)

def t_create(path: str, content: str) -> None:

    """
    Creates a file with the given content, overwrites if already 
    existant.

    Parameters:
        path (str) - The path to the file to create.
        content (str) - The content of the file.

    Returns: None
    """

    try:
        with open(path, "w") as f:
            f.write(content)
    except PermissionError:
        t_err(f"No permission to write '{path}'.")
    except Exception as exc:
        t_err(exc)


# Functions
# ---------

def render(path: str) -> None:

    """
    Renders the template with the settings values.

    Parameters:
        template (str) - The template to render.
    
    Returns: None
    """
    
    template = t_open(path)
    settings_content = {attr: str(getattr(settings, attr)) for attr in dir(settings) if not callable(getattr(settings, attr)) and not attr.startswith("__")}
    render = path.split(".")[0]
    for key, value in settings_content.items():
        template = template.replace(f"{{{{ {key} }}}}", value)
    t_create(f"{render}.html", template)
    print(f"\033[0;32m[SUCCESS] Render completed !\033[0m")


# Main Function
# -------------

def main(arg: list) -> None:

    """
    Calls the render function with the content of the file
    to render a CV based on a template and specific settings.

    Parameters:
        arg (list) - The list of arguments.
    
    Returns: None
    """

    if len(arg) != 1:
        t_err("Invalid number of arguments", True)
    render(arg[0])
    

# Main
# ----

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exc:
        t_err(exc)

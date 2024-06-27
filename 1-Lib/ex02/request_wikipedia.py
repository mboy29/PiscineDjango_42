# Imports
# -------
import sys, requests, dewiki


# Global Variables
# ----------------

ERROR = '\033[0;31m'
SUCCESS = '\033[0;32m'
INFO = '\033[0;34m'
WARNING = '\033[0;33m'
NC = '\033[0m'

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"


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
    
    print(f"{ERROR}[ERROR] {msg}{NC}")
    if usage:
        print(f"{WARNING}[USAGE] python3 request_wikipedia.py{NC}")
    exit(code)

def t_create(path: str, content: str) -> None:

    """
    Creates a file in the given path with the given content.

    Parameters:
        path (str) - The path to create the file.
        content (str) - The content of the file.
    
    Returns: None
    """

    try:
        with open(path, "w") as file:
            file.write(content)
        print(f"{SUCCESS}[SUCCESS] File created: {path}")
    except Exception as e:
        t_err(f"Failed to create file: {e}")


# Functions
# ---------

def request_wikipedia(search: str) -> None:

    """
    Makes a request to the Wikipedia API to get a specific
    page and returns the content of the page.
    Raises am exception if the page does not exist.

    Parameters:
        page (str) - The page to request.
    
    Returns: None
    """

    response = requests.get(WIKI_API_URL, params={
        "action": "parse",
        "page": search,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    })
    response.raise_for_status()
    data = response.json()
    if data.get("error") is not None:
        raise Exception(data["error"]["info"])
    return dewiki.from_string(data["parse"]["wikitext"]["*"]).strip()


# Main Function
# -------------

def main(args: list) -> None:
    
    """
    Main function of the program. It receives a search term
    and requests the Wikipedia API to get the content of the
    page. It then creates a file with the content.

    Parameters:
        args (list) - The arguments passed to the program.

    Returns: None
    """

    try:

        if len(args) != 1:
            t_err("Invalid number of arguments", usage=True)
        response = request_wikipedia(args[0])
        t_create(f"{args[0]}.wiki", response)

    except Exception as exc:
        t_err(exc, usage=True)


# Main
# ----

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Exception as exc:
        t_err(f"Unhandled exception: {exc}", usage=True)


# python3 -m venv env
# source env/bin/activate
# pip install -r requirement.txt
# deactivate
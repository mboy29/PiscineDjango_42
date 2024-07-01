# Imports
# -------
import sys, requests
from bs4 import BeautifulSoup


# Global Variables
# ----------------

ERROR = '\033[0;31m'
SUCCESS = '\033[0;32m'
INFO = '\033[0;34m'
WARNING = '\033[0;33m'
NC = '\033[0m'

WIKI_URL = "https://en.wikipedia.org/wiki/"

WIKI_INVALID_SUBSTRINGS = [
    "/wiki/Help:", 
    "/wiki/Wikipedia:", 
    "/wiki/File:", 
    "/wiki/Special:", 
    "/wiki/Template:", 
    "/wiki/Category:", 
    "/wiki/Portal:", 
    "/wiki/Talk:"
]


# Exceptions
# ----------

class DeadEnd(Exception):

    def __init__(self, message: str = "It leads to a dead end !") -> None:
        super().__init__(message)
    
    def __str__(self) -> str:
        return super().__str__()

class InfiniteLoop(Exception):

    def __init__(self, message: str = "It leads to an infinite loop !") -> None:
        super().__init__(message)
    
    def __str__(self) -> str:
        return super().__str__()

class RoadsToPhilosophy(Exception):

    def __init__(self, roads: list, message: str = "It leads to Philosophy.") -> None:
        super().__init__(message)
        self.roads = roads
    
    def __str__(self) -> str:
        ret = f"{len(self.roads)} roads from {self.roads[0] if len(self.roads) != 0 else 'Philosophy'} to Philosophy"
        if len(self.roads) > 0:
            ret += ":"
        for road in self.roads:
            ret += f"\n - {road}"
        return ret


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
        print(f"{WARNING}[USAGE] python3 roads_to_philosophy.py <key word(s) to search>{NC}")
    exit(code)

def t_success(msg: str) -> None:

    """
    Prints a success message in green.

    Parameters:
        msg (str) - The success message to print.
    
    Returns: None
    """

    print(f"{SUCCESS}[SUCCESS] {msg}{NC}")

def t_info(msg: str) -> None:

    """
    Prints an information message in blue.

    Parameters:
        msg (str) - The information message to print.

    Returns: None
    """

    print(f"{INFO}[INFO] {msg}{NC}")


# Functions
# ---------

def roads_to_philosophy(key_words: str, roads: list = []) -> None:

    """
    Function that recursively searches for the first link
    in the content of the Wikipedia page corresponding to
    the given search key words, and continues the search
    until it reaches the Philosophy page, or a dead end, or
    an infinite loop (exception raised in each case).

    Parameters:
        key_words (str) - The key words to search for in 
            Wikipedia.
        roads (list) - The list of roads to Philosophy, 
            defaults to an empty list.
    
    Returns: None
    """

    if roads == [] and key_words.title() == "Philosophy":
        raise RoadsToPhilosophy(roads)
    response = requests.get(WIKI_URL + key_words)
    if response.status_code != 200:
        raise DeadEnd()
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find(id="firstHeading").text
    if title in roads:
        raise InfiniteLoop()
    roads.append(title)
    if title == "Philosophy":    
        raise RoadsToPhilosophy(roads)
    content = soup.find(id="mw-content-text")
    for paragraph in content.find_all("p", recursive=True):
        for link in paragraph.find_all("a", recursive=True):
            href = link.get("href")
            if href is not None and href.startswith("/wiki/") and all(sub not in href for sub in WIKI_INVALID_SUBSTRINGS):
                return roads_to_philosophy(href[6:], roads)
    raise DeadEnd()


# Main Function
# -------------

def main(args: list) -> None:

    """
    Main function of the program, checks the number of arguments
    and starts the search for roads to Philosophy from the given
    key words.

    Parameters:
        args (list) - The list of arguments passed to the program.
    
    Returns: None
    """

    try:
        if len(args) != 1:
            t_err("Invalid number of arguments", usage=True)
        t_info(f'Searching roads to Philosophy starting from "{args[0]}"...')
        roads_to_philosophy(' '.join(args[0].split()).title())
    except RoadsToPhilosophy as exc:
        t_success(exc)
    except (DeadEnd, InfiniteLoop) as exc:
        t_err(exc)
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
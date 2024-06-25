# Required Function
# -----------------

def my_var() -> None:
    
    """
    Define a seires of variables and print them and their types.

    Parameters: None

    Returns: None
    """

    # Define variables
    v_int = 42
    v_str_digit = "42"
    v_str_alpha = "quarante-deux"
    v_float = 42.0
    v_bool = True
    v_list = [42]
    v_dict = {42: 42}
    v_tuple = (42,)
    v_set = set()

    # Print variables and their types
    print(f"{v_int} has a type {type(v_int)}")
    print(f"{v_str_digit} has a type {type(v_str_digit)}")
    print(f"{v_str_alpha} has a type {type(v_str_alpha)}")
    print(f"{v_float} has a type {type(v_float)}")
    print(f"{v_bool} has a type {type(v_bool)}")
    print(f"{v_list} has a type {type(v_list)}")
    print(f"{v_dict} has a type {type(v_dict)}")
    print(f"{v_tuple} has a type {type(v_tuple)}")
    print(f"{v_set} has a type {type(v_set)}")
    

# Main Function
# -------------

def main() -> None:

    """
    Main function for the program.
    Calls the required function.

    Parameters: None

    Returns: None
    """
    
    my_var()
    

# Main
# ----

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\033[0;31m'Error: {exc}\033[0m'")
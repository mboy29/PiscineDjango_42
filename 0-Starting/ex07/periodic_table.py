# Imports
# -------
import sys

# Constants
# ---------
style = """
            body {
                background-color: white;
                display: flex;
                flex-direction: column;
                justify-content: center; 
                align-items: center; 
                height: 100vh;
                margin: 0;
                padding: 40px;
                box-sizing: border-box;
            }

            h1 {
                color: #424242;
                font-family: 'Arial', sans-serif;
                font-size: 21pt;
                text-transform: uppercase;
                text-align: center;
                margin: 5px 0;
            }

            h2 {
                color: black;
                font-family: 'Arial', sans-serif;
                font-size: 14pt;
                text-transform: uppercase;
                font-weight: lighter;
                margin: 5px 0;
            }

            h3 {
                color: black;
                font-family: 'Arial', sans-serif;
                font-size: 10pt;
                text-transform: uppercase;
                clear: both;
                margin: 0 0;
            }

            h4 {
                font-family: 'Arial', sans-serif;
                font-weight: lighter;
                font-size: 10px;
                margin: 0px;
            }

            ul {
                padding: 0;
                margin: 0;
            }

            li {
                list-style: none;
            }

            strong {
                color: #424242;
                font-family: 'Arial', sans-serif;
                font-size: 10pt;
                font-weight: bold;
                text-transform: uppercase;
            }

            table {
                background-color: #f1f1f1;
                padding: 10px;
                box-sizing: border-box;
                max-width: 100%;
                overflow: auto;
            }

            .element {
                background-color: #e2e2e2;
                border: 1px solid #cccccc;
                text-align: center;
                padding: 10px;
                position: relative;
                box-sizing: border-box;
            }
            .element-number {
                position: absolute;
                top: 5px;
                right: 5px;
                font-family: 'Arial', sans-serif;
                font-size: 12px;
            }
            .element-symbol {
                font-family: 'Arial', sans-serif;
                font-size: 18px;
                font-weight: bold;
            }
            .element-name {
                font-family: 'Arial', sans-serif;
                font-size: 12px;
                margin-top: 5px;
            }
            .element-molar {
                font-family: 'Arial', sans-serif;
                font-size: 10px;
                margin-top: 5px;
            }
            .element-electron {
                font-family: 'Arial', sans-serif;
                font-size: 8px;
                margin-top: 5px;
            }

            .legend {
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 20px;
            }

            .legend-item {
                font-family: 'Arial', sans-serif;
                font-size: 12px;
                text-transform: uppercase;
                padding: 5px 15px;
                margin: 0 10px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
"""

element_categories = {
    "Alkali Metals": {
        "color": "#567662",
        "elements": ["Lithium", "Sodium", "Potassium", "Rubidium", "Cesium", "Francium", "Caesium"]
    },
    "Alkaline Earth Metals": {
        "color": "#719880",
        "elements": ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
    },
    "Transition Metals": {
        "color": "#89A995",
        "elements": ["Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt",
            "Nickel", "Copper", "Zinc", "Yttrium", "Zirconium", "Niobium", "Molybdenum",
            "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Hafnium",
            "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
            "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium",
            "Darmstadtium", "Roentgenium", "Copernicium", "Ununtrium", "Flerovium", "Ununpentium",
            "Livermorium", "Ununseptium", "Ununoctium"]
    },
    "Post-Transition Metals": {
        "color": "#A0BAAA",
        "elements": ["Aluminium", "Gallium", "Indium", "Thallium", "Lead", "Bismuth", "Polonium", "Tin", "Astatine"]
    },
    "Metalloids": {
        "color": "#B8CCC0",
        "elements": ["Boron", "Silicon", "Germanium", "Arsenic", "Antimony", "Tellurium"],
    },
    "Reactive Non-Metals": {
        "color": "#D0DDD4",
        "elements": ["Hydrogen", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Phosphorus", "Sulfur", "Chlorine", "Selenium", "Bromine", "Iodine", "Carbon"]
    },
    "Noble Gases": {
        "color": "#E8EEEA",
        "elements": ["Helium", "Argon", "Krypton", "Xenon", "Radon"],
    }
}


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
    if usage == True:
        print("\033[0;33m[USAGE] python3 periodic_table.py <path>\033[0m")
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
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise Exception(f"'{path}' does not exist.")
    except IsADirectoryError:
        return t_err(f"'{path}' is a directory.")
    except PermissionError:
        return t_err(f"No permission to read '{path}'.")

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


def t_parse(data) -> dict:
   
    """
    Parses the data into a dictionary where the key is the name
    of the element and the value is a dictionary with the properties
    of the element (position, number, small, molar & electron).
    It then sorts the elements by position and number.

    Parameters:
        data (str) - The data to parse.

    Returns:
        dict - The parsed data.
    """
    parse_data = []
    for line in data.strip().split('\n'):
        if ' = ' in line:
            name, properties = line.split(' = ', 1)
            properties_data = {}
            for prop in properties.split(', '):
                key, value = prop.split(':')
                properties_data[key] = value
            parse_data.append((name, properties_data))
        else:
            raise ValueError(f"Invalid line format: {line}")
    parse_data.sort(key=lambda x: int(x[1]['number']))
    sorted_data = {name: properties_data for name, properties_data in parse_data}
    return sorted_data

def t_get_category(name: str) -> tuple:
    
    """
    Returns the category and color of the element.

    Parameters:
        name (str) - The name of the element.

    Returns:
        str - The category of the element.
        str - The color of the element.
    """

    for category, data in element_categories.items():
        if name in data['elements']:
            return category, data['color']
    print(f"Unknown category for element: {name}")
    return "Unknown", "#FFFFFF"


# Functions
# ---------

def periodic_table_legend() -> str:

    """
    Generates the legend HTML content for the periodic table.

    Returns:
        str - The HTML content for the legend.
    """

    legend_content = """
            <div class="legend">
    """
    for category, data in element_categories.items():
        color = data['color']
        legend_content += f"""
                <div style="background-color: {color};" class="legend-item">{category}</div>
        """
    legend_content += """
            </div>
    """
    return legend_content

def periodic_table_elements(elements: dict) -> str:
   
    """
    Generates the HTML content for the elements in the periodic table using an HTML table structure.

    Parameters:
        elements (dict) - A dictionary with the element's information.

    Returns:
        str - The HTML content for the elements.
    """
    
    table_content = """
            <table class="table">
                <tbody>
    """
    
    for row in range(1, 8):
        table_content += "<tr>"
        for col in range(0, 18):
            found = False
            for name, properties in elements.items():
                
                position = int(properties['position'])
                number = int(properties['number'])
                small = properties['small']
                molar = properties['molar']
                electron = properties['electron']

                period = 1
                if number > 2:
                    period = 2
                if number > 10:
                    period = 3
                if number > 18:
                    period = 4
                if number > 36:
                    period = 5
                if number > 54:
                    period = 6
                if number > 86:
                    period = 7

                if col == position and row == period:
                    found = True
                    category, color = t_get_category(name)
                    table_content += f"""
                        <td class="element" style="background-color: {color};">
                            <ul>
                                <li class="element-number">{number}</li>
                                <li class="element-symbol">{small}</li>
                                <li class="element-name"><h4>{name}</h4></li>
                                <li class="element-molar">{molar}</li>
                                <li class="element-electron">{electron}</li>
                            </ul>
                        </td>
                    """
                    break
            
            if not found:
                table_content += "<td></td>"
            
        table_content += "</tr>"
    
    table_content += """
                </tbody>
            </table>
    """
    return table_content



def periodic_table(elements: dict) -> str:
    
    """
    Generates the HTML content for the periodic table.

    Parameters:
        elements (dict) - A dictionary with the element's information.

    Returns:
        str - The HTML content.
    """
    
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Periodic Table</title>
            <style>
                """ + style + """
            </style>
        </head>
        <body>
            <h1>Periodic Table</h1>
    """
    html_content += periodic_table_legend()
    html_content += periodic_table_elements(elements)
    html_content += """
        </body>
    </html>
    """
    t_create("periodic_table.html", html_content)
    print("\033[0;32m[SUCCESS] Periodic Table generated !\033[0m")


# Main Function
# -------------

def main(arg: list) -> None:
    
    """
    Main function to generate the periodic table.

    Parameters:
        arg (list) - The list of arguments.

    Returns: None
    """

    # Check number of arguments
    if len(arg) != 1:
        t_err("Invalid number of arguments", True)

    # Open file, parse data and generate the periodic table
    file_content: str = t_open(arg[0])
    parsed_content: dict = t_parse(file_content)
    periodic_table(parsed_content)


# Main
# ----

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exc:
        t_err(exc)

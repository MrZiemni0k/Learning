import json

DIVIDE = 30
COLOR = ['#f39c12', '#046582', '#c1a1d3', '#16a085', '#4f4c1c', '#27ae60',
         '#1c7a44', '#40805b', '#876787', '#595b83', '#966c3b', '#683800',
         '#548c8d', '#14274e', '#5b035d', '#00204d', '#3498db', '#3d403f',
         '#7cc1cc', '#8066ad', '#9e215b', '#9eb837', '#8f8cad', '#d180bd']

POSSIBLE_KEYS = ['ID', 'VAT_', 'KOD_', 'SYM_']
C_SPACE = 25

# ----------------------------- 💡💻 GET DATA 💻💡 -----------------------------
# SQL most often repetitive keys in my DB.
with open('./keys.json', encoding='utf8') as file:
    json_data = json.load(file)
try:
    with open('./keys.json', encoding='utf8') as file:
        JSON_DATA = json.load(file)
except FileNotFoundError:
    print("File not found.")


def filter_sql(text: str) -> dict:
    """
    Filters SQL-SERVER's\n
    "Script table as -> Create to"\n
    \n
    ↩️RETURNS dict\n
    'table'⠀⠀⠀ - str: Table name\n
    'keys'⠀⠀⠀⠀- dict: Key columns dict:\n
    ⠀⠀⠀⠀'name'⠀⠀⠀⠀ - str: Column key name\n
    ⠀⠀⠀⠀'type'⠀⠀⠀⠀⠀ - str: Column key type\n
    ⠀⠀⠀⠀'null'⠀⠀⠀⠀⠀⠀ - str: 'NULL' or 'NOT NULL'\n
    ⠀⠀⠀⠀'value'⠀⠀⠀⠀⠀ - str: Value of type\n
    ⠀⠀⠀⠀'primary'⠀⠀⠀ - int: 1:Primary key, 0:Not\n
    'columns'⠀- dict: Other columns dict:\n
    ⠀⠀⠀⠀'name'⠀⠀⠀⠀ - str: Column name\n
    ⠀⠀⠀⠀'type'⠀⠀⠀⠀⠀ - str: Column type\n
    ⠀⠀⠀⠀'null'⠀⠀⠀⠀⠀⠀ - str: 'NULL' or 'NOT NULL'\n
    ⠀⠀⠀⠀'value'⠀⠀⠀⠀⠀ - str: Value of type\n
    'length'⠀⠀⠀- list: Max length of columns\n

    :param text: SQL-SERVER's "CREATE TO"
    """
    column_length = 0       # Track max column length
    max_column_length = []  # For each DIVIDE part, store max len(column_name)
    current_column = 0      # Track COLUMN NAME(Not key) number
    create_index = None     # Index for CREATE TABLE statement
    key_index = None        # Index for PRIMARY KEY statement
    column_names = []       # Column names that are not keys
    key_names = []          # Key column names
    text_lines = text.splitlines()

    # Filter to (From SELECT to FROM statement)
    for line_num in range(len(text_lines)):
        if "CREATE TABLE" in text_lines[line_num]:
            create_index = line_num
        elif "PRIMARY KEY" in text_lines[line_num]:
            key_index = line_num

    # Table name
    table_name = text_lines[create_index]
    table_name = table_name[table_name.rfind("[") + 1:
                            table_name.rfind("]")]

    # Column names with attributes
    columns = text_lines[create_index+1:key_index]
    for line in columns:
        # COLUMN TYPE
        c_type = line[line.rfind("[") + 1: line.rfind("]")]
        # TYPE VALUE
        c_value = line[line.find("("): line.rfind(")")+1]
        # COLUMN NAME
        c_name = line[line.find("[")+1: line.find("]")]
# ----------------------------- 💡💻 SQL KEYS 💻💡  ----------------------------
        # Check if column is a 'possible' key.
        is_primary = 0
        for pos_key in POSSIBLE_KEYS:
            if c_name[:len(pos_key)] == pos_key:
                if c_name in text_lines[key_index + 2]:
                    is_primary = 1

                # NULLS
                if "NOT NULL" in line:
                    c_null = "NOT NULL"
                else:
                    c_null = "NULL"
                key_names.append({'name': c_name, 'type': c_type,
                                  'null': c_null, 'value': c_value,
                                  'primary': is_primary})
# -------------------------- 💡💻 OTHER COLUMNS 💻💡 ---------------------------
        if not is_primary:
            # NULLS
            if "NOT NULL" in line:
                c_name = '[!]' + c_name
                c_null = "NOT NULL"
            else:
                c_null = "NULL"

            # CHECK FOR LENGTH CONFIGURATION
            current_column += 1
            if len(c_name) > column_length:
                column_length = len(c_name)  # New maximum

            if current_column % DIVIDE == 0:  # New 'INNE' section
                max_column_length.append(column_length)
                column_length = 0
            elif current_column == len(columns)-len(key_names) - 1:
                max_column_length.append(column_length)  # Last 'INNE' section
            column_names.append({'name': c_name, 'type': c_type,
                                 'null': c_null, 'value': c_value})

    return {'table': table_name, 'keys': key_names,
            'columns': column_names, 'length': max_column_length}


def make_lists(db_dict: dict) -> str:
    """
    Makes unordered lists of column names that are not keys.
    These lists are separated by number: global DIVIDE.\n
    :param db_dict: Filtered dictionary from filter_sql function.
    :return: str - Styled string for additional dbdiagram.io columns.
    """
    column_lens = db_dict['length']
    which_section = 0  # WHICH dbdiagram.io column
    which_column = 0   # Track number of column names

    # Add heading
    output = 'KOLUMNA' + ' ' * (column_lens[which_section] - 6) + \
             '| OPIS\n' + '‾' * (column_lens[which_section] + C_SPACE) + '\n'

    # Add columns
    for column in db_dict['columns']:
        which_column += 1
        if which_column % DIVIDE == 0:
            which_section += 1
            output += 'KOLUMNA' + ' ' * (column_lens[which_section] - 6) \
                      + '| OPIS\n' + '‾' * \
                      (column_lens[which_section] + C_SPACE) + '\n'

        c_name = column['name']
        c_type = f'{column["type"]}{column["value"]}'

        # 📌COLUMN_NAME....⭕varchar(20)..
        # BIG_COLUMN_NAME.⭕tinyint....... etc.
        if column['null'] == 'NOT NULL':
            dots_num = column_lens[which_section] - len(column['name']) - 1
            output += (c_name + (dots_num + 2) * '.' + '⭕' + c_type + '\n')
        else:
            dots_num = column_lens[which_section] - len(c_name)
            output += (c_name + (dots_num+1) * '.' + '⭕' + c_type + '\n')
    return output


def make_keys(db_dict: dict) -> str:
    """
    Makes dbdiagram.io columns with keys and its basic notes.\n
    :param db_dict: Filtered dictionary from filter_sql function.
    :return: str - Styled string for dbdiagram.io key columns
    """
    output = ''
    table_name = db_dict["table"]
    for key in db_dict["keys"]:
        if key["primary"]:
            output += '        "🔑'
        else:
            output += '        "'
        # check_length = 0    # Placeholder for dbdiagram.io note size expand.
        replaced_text = 0  # Placeholder for string template

        # To reduce typing I provided some string templates for often used keys
        if key["name"] in list(json_data.keys()) and not key["primary"]:
            replaced_text = json_data[key['name']].replace(
                    '[TABELA]', table_name)
            split_text = replaced_text.splitlines()
            check_length = len(split_text[2])
        else:
            check_length = len(f' 1️⃣ ---> ♾️{table_name} ')

        check_length -= (len(key["name"]) + 5)
        if check_length < 0:
            check_length = 0

        output += f'{key["name"]}' + '⠀' * check_length + \
                  f'" {key["type"]} [{key["null"]},\n'

        if key['primary']:
            output += f'note:\n\'🔑 - Identyfikator\n\']\n'
        elif key['name'] in list(json_data.keys()):
            output += 'note:\n\'' + replaced_text + '\n\']\n'
        else:
            output += f'note:\n\'⚿ - Identyfikator\n\n 1️⃣ ---> ♾️ '
            output += f'{table_name}\n(🔑ID_)\n\']\n'
    return output


def make_dbtable(text: str, color: str = COLOR[0]) -> str:
    """
    Use filter_sql function and converts\n
    the text to styled one for dbdiagram.io\n
    :param text: SQL-SERVER's "CREATE TO"
    :param color: #Hex Color || Default(COLOR[0])
    :return: str: Styled string for dbdiagram.io
    """
    db_dict = filter_sql(text)
    columns = make_lists(db_dict).splitlines()  # Columns that are no keys
    table_length = 25 - len(db_dict["table"])  # For dbdiagram table note size

    if table_length < 0:
        table_length = 0
    table_output = table_length * '⠀'

    output = '/' * 50 + '\n' + f'//*{db_dict["table"]}*\n' + '/'*50+'\n'
    output += (f'Table "{db_dict["table"]}{table_output}" [\n'
               f'headercolor: {color},\n''note:\n''\'\n''\n''\']{\n')
    output += make_keys(db_dict)

    for length in range(len(db_dict['length'])):
        output += f'    "📝INNE{length+1}'+'⠀' * \
                  (db_dict['length'][length] + C_SPACE - 15) + \
                  '" list [\n''note:\n\''
        if length == 0:
            for column in columns[0: DIVIDE + 1]:
                output += column + '\n'
        else:
            for column in columns[
                    (length * (DIVIDE + 2) - 1): DIVIDE + 1 + (DIVIDE * length)
                    ]:
                output += column + '\n'
        output += '\']\n'
    return output + "}"

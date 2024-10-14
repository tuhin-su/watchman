def load_config(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            # Ignore empty lines and comments
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Split the key-value pair
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()

            # Convert values to appropriate types
            if value.startswith('[') and value.endswith(']'):
                # Parse list
                value = eval(value)  # Use eval carefully; consider using ast.literal_eval for safety
            elif value.lower() in ['true', 'false']:
                # Convert to boolean
                value = value.lower() == 'true'
            else:
                # Try to convert to int, if not boolean
                try:
                    value = int(value)
                except ValueError:
                    pass  # Leave it as string if not convertible

            config[key] = value

    return config
# Hoppscotch to Postman Converter

## Overview

The **Hoppscotch to Postman Converter** is a Python tool designed to facilitate the conversion of API requests from Hoppscotch format to Postman collections. This project aims to streamline the workflow for developers who use both tools, making it easier to manage and share API requests.

## Features

- Convert Hoppscotch API requests to Postman collections.
- Convert Hoppscotch environment variables to Postman environment format.
- Supports various request types (GET, POST, PUT, DELETE, etc.).
- Maintains request headers, parameters, and body formats.

## Installation

To get started with the Hoppscotch to Postman Converter, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hoppscotch-to-postman-converter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hoppscotch-to-postman-converter
   ```

## Usage

### Converting Hoppscotch API Requests

1. Prepare your Hoppscotch exported JSON file. Place it in the project directory or specify the path in the code.
2. Open the `main.py` file and uncomment the line to convert the Hoppscotch exported file:
   ```python
   # Convert to Postman v2.1
   convert_hoppscotch_to_postman_collection_v21('hoppscotch_exported_file.json')
   ```
3. Run the script:
   ```bash
   python main.py
   ```

### Converting Hoppscotch Environment Variables

1. Place your Hoppscotch environment JSON files in the `hoppscotch_exported_files` directory.
2. The script will automatically convert each `.json` file in that directory to a Postman environment format when you run `main.py`.

### Example

To convert a Hoppscotch exported file named `hoppscotch_exported_file.json` and all environment files in the `hoppscotch_exported_files` directory, your `main.py` should look like this:

```python
import os

from hoppscotch_to_postman_converter import (
    convert_hoppscotch_to_postman_collection_v21,
    convert_hoppscotch_env_to_postman_env
)

# Convert to Postman v2.1
convert_hoppscotch_to_postman_collection_v21('hoppscotch_exported_file.json')

# Convert to Postman environment
for file in os.listdir('hoppscotch_exported_files'):
    if file.endswith('.json'):
        convert_hoppscotch_env_to_postman_env(f'hoppscotch_exported_files/{file}')
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of Hoppscotch and Postman for their amazing tools.
- Inspiration from various open-source projects.

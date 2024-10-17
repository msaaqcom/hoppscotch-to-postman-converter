import os

from hoppscotch_to_postman_converter import (
    convert_hoppscotch_to_postman_collection_v21,
    convert_hoppscotch_env_to_postman_env
)

# Convert to Postman v2.1
# convert_hoppscotch_to_postman_collection_v21('hoppscotch_exported_file.json')


# Convert to Postman environment

# map hoppscotch_exported_files folder to convert each file end with .json to postman collection
for file in os.listdir('hoppscotch_exported_files'):
    if file.endswith('.json'):
        convert_hoppscotch_env_to_postman_env(f'hoppscotch_exported_files/{file}')

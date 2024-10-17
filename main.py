import json

from hoppscotch_to_postman_converter import (
    convert_hoppscotch_to_postman_collection_v21,
    convert_hoppscotch_env_to_postman_env
)

# Convert to Postman v2.1
convert_hoppscotch_to_postman_collection_v21('hoppscotch_exported_file.json')


# Convert to Postman environment
convert_hoppscotch_env_to_postman_env('hoppscotch_environment.json')



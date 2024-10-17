import json
import re


def convert_hoppscotch_to_postman_collection_v21(hoppscotch_json_exported_file):
    # Load Hoppscotch JSON file with UTF-8 encoding
    with open(hoppscotch_json_exported_file, 'r', encoding='utf-8') as hoppscotch_file:
        hoppscotch_data = json.load(hoppscotch_file)

    # Initialize Postman Collection structure
    postman_collection = {
        "info": {
            "name": hoppscotch_data["name"],
            "_postman_id": "",
            "description": "",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": [],
        "auth": {},
        "event": [],
        "variable": [],
        "protocolProfileBehavior": {}
    }

    # Helper function to replace <<...>> with {{...}} for Postman variables
    def replace_placeholders(value):
        if isinstance(value, str):
            return re.sub(r"<<(.*?)>>", r"{{\1}}", value)
        return value

    # Helper function to convert auth details
    def convert_auth(hoppscotch_auth):
        postman_auth = []
        if hoppscotch_auth["authType"] == "bearer":
            postman_auth = {
                "type": "bearer",
                "bearer": [
                    {"key": "token", "value": replace_placeholders(hoppscotch_auth.get("token", "")), "type": "string"}]
            }
        elif hoppscotch_auth["authType"] == "inherit":
            postman_auth = {
                "type": "inherit"
            }
        elif hoppscotch_auth["authType"] == "none":
            postman_auth = {"type": "noauth"}
        return postman_auth

    # Helper function to convert headers
    def convert_headers(hoppscotch_headers):
        return [
            {"key": replace_placeholders(header["key"]), "value": replace_placeholders(header["value"]), "type": "text"}
            for header in hoppscotch_headers if header["active"]]

    # Helper function to convert body
    def convert_body(hoppscotch_body):
        if hoppscotch_body and hoppscotch_body["contentType"] == "multipart/form-data":
            return {
                "mode": "formdata",
                "formdata": [{"key": replace_placeholders(item["key"]), "value": replace_placeholders(item["value"]),
                              "type": "text"} for item in hoppscotch_body["body"]]
            }
        return {"mode": "raw", "raw": ""} if hoppscotch_body else None

    # Helper function to convert individual requests
    def convert_request(hoppscotch_request):
        return {
            "name": hoppscotch_request["name"],
            "request": {
                "method": hoppscotch_request["method"],
                "header": convert_headers(hoppscotch_request.get("headers", [])),
                "body": convert_body(hoppscotch_request.get("body", None)),
                "url": {
                    "raw": replace_placeholders(hoppscotch_request["endpoint"]),
                    "host": replace_placeholders(hoppscotch_request["endpoint"]).split("/")[:1],
                    "path": replace_placeholders(hoppscotch_request["endpoint"]).split("/")[1:]
                },
                "auth": convert_auth(hoppscotch_request["auth"]),
                "description": hoppscotch_request.get("description", "")
            }
        }

    # Recursively convert folders and requests
    def convert_folder(hoppscotch_folder):
        folder_item = {
            "name": hoppscotch_folder["name"],
            "item": []
        }

        for subfolder in hoppscotch_folder.get("folders", []):
            folder_item["item"].append(convert_folder(subfolder))

        for request in hoppscotch_folder.get("requests", []):
            folder_item["item"].append(convert_request(request))

        return folder_item

    # Convert folders and add to Postman collection
    for folder in hoppscotch_data.get("folders", []):
        postman_collection["item"].append(convert_folder(folder))

    # Add global auth if present
    if "auth" in hoppscotch_data:
        postman_collection["auth"] = convert_auth(hoppscotch_data["auth"])

    # Save the Postman collection to a file with UTF-8 encoding
    with open('postman_collection_v2.1.json', 'w', encoding='utf-8') as postman_file:
        json.dump(postman_collection, postman_file, indent=2, ensure_ascii=False)

    print("Conversion completed. Postman collection saved as postman_collection_v2.1.json")

    return postman_collection


def convert_hoppscotch_env_to_postman_env(hoppscotch_json_env):
    # Load Hoppscotch environment JSON file
    with open(hoppscotch_json_env, 'r', encoding='utf-8') as hoppscotch_file:
        hoppscotch_env_data = json.load(hoppscotch_file)

    # Initialize Postman Environment structure
    postman_env = {
        "id": hoppscotch_env_data["id"],
        "name": hoppscotch_env_data["name"],
        "values": [],
        "_postman_variable_scope": "environment",
        "_postman_exported_at": "",
        "_postman_exported_using": "Postman Environment Converter"
    }

    # Convert variables from Hoppscotch to Postman format
    for variable in hoppscotch_env_data["variables"]:
        postman_env["values"].append({
            "key": variable["key"],
            "value": variable["value"],
            "enabled": True,
            "type": "text",  # Postman uses "text" type for environment variables
            "secret": variable["secret"]
        })

    # Generate file name based on the environment name
    postman_env_file_name = hoppscotch_json_env.replace('.json', '_postman_environment.json')

    # Save the Postman environment to a file with UTF-8 encoding
    with open(postman_env_file_name, 'w', encoding='utf-8') as postman_env_file:
        json.dump(postman_env, postman_env_file, indent=2, ensure_ascii=False)

    print("Environment conversion completed. Postman environment saved as postman_environment.json")

    return postman_env

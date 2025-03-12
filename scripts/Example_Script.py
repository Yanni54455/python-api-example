# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 07:34:50 2025

@author: YHalkiadakis
"""

import os, sys, json
parent_folder = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_folder)
from moveshelf_api.api import MoveshelfApi

## Setup the API
# Load config
personal_config = os.path.join(parent_folder, "mvshlf-config.json")
if not os.path.isfile(personal_config):
    raise FileNotFoundError(
        f"Configuration file '{personal_config}' is missing.\n"
        "Ensure the file exists with the correct name and path."
    )

with open(personal_config, "r") as config_file:
    data = json.load(config_file)

api = MoveshelfApi(
    api_key_file=os.path.join(parent_folder, data["apiKeyFileName"]),
    api_url=data["apiUrl"],
)

projects = api.getUserProjects()
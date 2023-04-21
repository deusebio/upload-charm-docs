# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Shared constants.

The use of this module should be limited to cases where the constant is not better placed in
another module or to resolve circular imports.
"""
import re

DEFAULT_BRANCH = "main"
DOCUMENTATION_TAG = "upload-docs-tag"

DOCUMENTATION_FOLDER_NAME = "docs"
DOCUMENTATION_INDEX_FILENAME = "index.md"
NAVIGATION_TABLE_START = """

# Navigation

| Level | Path | Navlink |
| -- | -- | -- |"""

NAVIGATION_TABLE_START_REGEX = re.compile(
    r"\n*\# Navigation\W*\|\W*Level\W*\|\W*Path\W*\|\W*Navlink\W*\|\n"
)

REDIRECT_TABLE_START = """

# Redirects

[details=Mapping table]
| Path | Location |
| ---- | -------- |"""

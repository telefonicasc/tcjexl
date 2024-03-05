# Copyright 2024 Telefónica Soluciones de Informática y Comunicaciones de España, S.A.U.
#
# This file is part of tcjexl
#
# tcjexl is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# tcjexl is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with IoT orchestrator. If not, see http://www.gnu.org/licenses/.

import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.0.post'
PACKAGE_NAME = 'tcjexl'
AUTHOR = ''
AUTHOR_EMAIL = ''
URL = ''

LICENSE = '' #License type
DESCRIPTION = 'Wrapper of pyjexl with additional set of transformations' # Short description
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') # Reference to the README.md document with a longer description
LONG_DESC_TYPE = "text/markdown"

# Required packages. They will be installed if not already installed
INSTALL_REQUIRES = [
    'pyjexl==0.3.0'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)

#  Copyright 2021 Jeremy Schulman
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from itertools import chain
from setuptools import setup, find_packages

package_name = "macaddr"
package_version = "2.0"


with open("README.md", "r") as fh:
    long_description = fh.read()


# -----------------------------------------------------------------------------
#
#                                 Main Setup
#
# -----------------------------------------------------------------------------

setup(
    name=package_name,
    version=package_version,
    description="Working with network MAC addresses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jeremy Schulman",
    py_modules=["macaddr"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
)

# Remover Tool allows you to remove unwanted files from target directory.
# Copyright (C) 2022  Michael Da Rosa (micheldarosazxc@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>
# or see <https://github.com/Michelzxc/remover-tool/>.
#
# ----------------------------------------------------------------------

import os
import sys
import argparse
from fclib import printq, notice


class RemoverTool(object):
    """
    Remover Tool allows you to remove unwanted files from target directory.
    """

    def __init__(self) -> None:
        self.raw_version = None
        self.raw_date = None

        self._version = None
        self._copyright = None
        self._cwd = None
        self._mude = True

        self.exclude_files = []  # Files and extensions excluded

    def run(self) -> None:
        """Run application."""

    def _build(self):
        """Load and configure the class"""

        # Build version
        self._version = "Remover Tool %s %s" % (self.raw_version, self.raw_date)
        self._copyright = (f"Remover Tool %s \n\n" % self._version,
                           "Copyright (C) 2022  Michael Da Rosa "
                           "(micheldarosazxc@gmail.com).\n"
                           "This is free software, and you are welcome "
                           "to redistribute it\nunder certain conditions; "
                           "see source code for more information.\n"
                           "This program comes with ABSOLUTELY NO WARRANTY.")

        # Get Current Working Directory
        self._cwd = os.getcwd()

    def load_rmignore(self):
        """Load content of .rmignore file."""

        try:
            with open(self._cwd, "r") as rmignorefile:
                for row in rmignorefile:
                    if "\n" in row:
                        self.exclude_files.append(row[:-1])
                    else:
                        self.exclude_files.append(row)

        except FileNotFoundError:
            printq("")
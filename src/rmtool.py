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

__version__ = "0.1.0"
__date__ = "2022-12-13"


def make_usr_folders(platform: str) -> None:
    """Make main, config and data folders in platform win32 or linux.
    .remover-tool/ folder save configuration and data of user.
    """

    # Make folders for Linux
    if platform == "linux":
        home_path = os.getenv("HOME")
        main_folder = home_path + "/.remover-tool"
        config_folder = main_folder + "/config"
        data_folder = main_folder + "/data"

        for path in [main_folder, config_folder, data_folder]:
            try:
                os.mkdir(path)

            except FileExistsError:
                print("[!] Folder is already exist: %s" % path)

    # Make folders for Windows
    elif platform == "win32":

        # <<< It is necessary to verify the working of this block. >>>

        home_path = os.getenv("HOME")
        main_folder = home_path + "/AppData/Local/remover-tool"
        config_folder = main_folder + "/config"
        data_folder = main_folder + "/data"

        for path in [main_folder, config_folder, data_folder]:
            try:
                os.mkdir(path)

            except FileExistsError:
                print("[!] Folder is already exist: %s" % path)

    else:
        print("[!] Platform [%s] isn't defined.")


def help_flag() -> None:
    """Print manual page."""

    print("Usage: rmtool [options] folder")
    print("Options:")
    print("<<< definir opciones posteriormente >>>")


def version_flag(version: str, date: str) -> None:
    """Print a notice of program information."""

    print("Remover Tool %s %s" % (version, date.replace("-", "")))

    print("Copyright (C) 2022  Michael Da Rosa "
          "(micheldarosazxc@gmail.com)\n"
          "This is free software, and you are welcome "
          "to redistribute it\nunder certain conditions;"
          "see source code for more information.\n"
          "This program comes with ABSOLUTELY NO WARRANTY.")


def main() -> None:
    pass


# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()

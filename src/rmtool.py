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

__version__ = "0.1.0"
__date__ = "2022-12-17"


def print2(*values, end="\n", mude=False) -> None:
    """A builtins function print with power switch.
    If mude is True, print nothing.
    """

    if not mude:
        print(*values, end=end)


class RemoverTool(object):
    """
    Remover Tool allows you to remove unwanted files from target directory.
    """

    def __init__(
            self,
            version: str = None,
            date: str = None
    ) -> None:
        self.version = f"Remover Tool {version} {date}"

        self.copyright = (f"Remover Tool {version} \n\n"
                          "Copyright (C) 2022  Michael Da Rosa "
                          "(micheldarosazxc@gmail.com).\n"
                          "This is free software, and you are welcome "
                          "to redistribute it\nunder certain conditions; "
                          "see source code for more information.\n"
                          "This program comes with ABSOLUTELY NO WARRANTY.")

        self.platform = sys.platform[:]
        self.home_path = os.getenv("HOME")

        # Input
        self.target_path = None
        self.flag_recursion = False
        self.flag_noconfirm = False
        self.flag_quiet = False
        self.flag_undo = False
        self.flag_delete = False

    def run(self) -> None:
        """Execute application script."""

        self.get_argparse()  # First input arguments

    def get_argparse(self) -> None:
        """Get argument from shell."""

        parser = argparse.ArgumentParser(
            prog="Remover Tool",
            description="Remove unwanted files from target directory.",
            epilog=self.copyright
        )

        # Flags
        parser.add_argument(
            "-q", "--quiet",
            action="store_true",
            help="Not print operations in stdout."
        )
        parser.add_argument(
            "-y", "--yes",
            action="store_true",
            help="Does not ask for confirmation."
        )
        parser.add_argument(
            "-r", "--recursive",
            action="store_true",
            help="Allow recursivity."
        )
        parser.add_argument(
            "-u", "--undo",
            action="store_true",
            help="Undo is if possible the previous removing"
        )
        parser.add_argument(
            "-D", "--delete",
            action="store_true",
            help="Permanently delete the files in cache."
        )
        parser.add_argument(
            "-v", "--version",
            action="version",
            version=self.version
        )

        # Names
        parser.add_argument(
            "path",
            help="Directory target for remove files."
        )

        # Get arguments
        args = parser.parse_args()

        self.target_path = args.path
        self.flag_noconfirm = args.yes
        self.flag_quiet = args.quiet
        self.flag_recursion = args.recursive
        self.flag_delete = args.delete
        self.flag_undo = args.undo

    def make_usr_folders(self) -> None:
        """Make main, global config and cache folders.
        .remover-tool/ folder save global configuration and data cache of user.
        """

        # Make folders for Linux
        if self.platform == "linux":
            main_folder = self.home_path + "/.remover-tool"
            config_folder = main_folder + "/config"
            cache_folder = main_folder + "/cache"

            for path in [main_folder, config_folder, cache_folder]:
                try:
                    os.mkdir(path)

                except FileExistsError:
                    print2(
                        "[!] Folder is already exist: %s" % path,
                        mude=self.flag_quiet
                    )

        # Make folders for Windows
        elif platform == "win32":

            # <<< It is necessary to verify the working of this block. >>>

            main_folder = self.home_path + "/AppData/Local/remover-tool"
            config_folder = main_folder + "/config"
            cache_folder = main_folder + "/cache"

            for path in [main_folder, config_folder, cache_folder]:
                try:
                    os.mkdir(path)

                except FileExistsError:
                    print2(
                        "[!] Folder is already exist: %s" % path,
                        mude=self.flag_quiet
                    )

        else:
            print2("[!] Platform [%s] isn't defined.", mude=self.flag_quiet)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    RemoverTool(
        __version__,
        __date__.replace("-", "")
    ).run()

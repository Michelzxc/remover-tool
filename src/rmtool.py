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


def menu_select_task(show_menu=True) -> int:
    """Print list of tasks and ask for one."""

    if show_menu:
        print(
            "select task:\n"
            # -1. return failed ask
            "0. exit\n"
            "1. save configure\n"
            "2. delete a current exclude\n"
            "3. clear current excludes\n"
            "4. set new excludes\n"
        )

    task = input(">>> ")
    try:
        int_task = int(task)

    except ValueError:
        print("[!] unexpected value '%s'" % task)
        return -1

    if int_task <= 0:
        return 0

    elif int_task >= 4:
        return 4

    else:
        return int_task


def set_new_file_exclusion_menu() -> list:
    """Set new files excludes."""

    print(
        "=> Set new excluded files and extensions, "
        "(type 0 to return, or 1 to save)."
    )
    content_list = []
    while True:
        new_entry = input(">>> ")
        if new_entry == "1":
            return content_list

        elif new_entry == "0":
            return []

        content_list.append(new_entry)


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
        # self.flag_recursion = False
        self.flag_noconfirm = False
        self.flag_verbose = False
        self.flag_quiet = False
        self.flag_undo = False
        self.flag_delete = False
        self.flag_exclude_mode = False

        self.exclude = []

    def run(self) -> None:
        """Execute application script."""

        self.get_argparse()  # First input arguments
        self.make_usr_folders()
        self.get_excluded_files()
        if self.flag_exclude_mode:
            self.exclusion_interface()
            sys.exit()

    def get_argparse(self) -> None:
        """Get argument from shell."""

        parser = argparse.ArgumentParser(
            prog="Remover Tool",
            description="Remove unwanted files from target directory.",
            epilog=self.copyright
        )

        qv_group = parser.add_mutually_exclusive_group()
        du_group = parser.add_mutually_exclusive_group()

        # Names
        parser.add_argument(
            "dirpath",
            help="directory target for remove files."
        )

        # Flags
        qv_group.add_argument(
            "-v", "--verbose",
            action="store_true",
            help="show all messages."
        )
        qv_group.add_argument(
            "-q", "--quiet",
            action="store_true",
            help="not print operations in stdout."
        )
        parser.add_argument(
            "-e", "--exclude",
            action="store_true",
            help="add new files and extensions types to exclude"
        )
        parser.add_argument(
            "-y", "--yes",
            action="store_true",
            help="does not ask for confirmation."
        )
        # parser.add_argument(
        #     "-r", "--recursive",
        #     action="store_true",
        #     help="Allow recursive."
        # )
        du_group.add_argument(
            "-u", "--undo",
            action="store_true",
            help="undo is if possible the previous removing"
        )
        du_group.add_argument(
            "-D", "--delete",
            action="store_true",
            help="permanently delete the files in cache."
        )
        parser.add_argument(
            "--version",
            action="version",
            version=self.version
        )

        # Get arguments
        args = parser.parse_args()

        self.target_path = args.dirpath
        self.flag_noconfirm = args.yes
        self.flag_verbose = args.verbose
        self.flag_quiet = args.quiet
        # self.flag_recursion = args.recursive
        self.flag_delete = args.delete
        self.flag_undo = args.undo
        self.flag_exclude_mode = args.exclude

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
                        mude=not self.flag_verbose
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
                        mude=not self.flag_verbose
                    )

        else:
            print2(
                "[!] Platform [%s] isn't defined.",
                mude=not self.flag_verbose
            )

    def exclusion_interface(self) -> None:
        """Make interface for set exclusions."""

        print("# Exclusion mode\n")
        print("allow set files and extensions exclude for tarjet directory.\n")
        if len(self.exclude) < 1:
            print("current exclusions: \n...\n")
        else:
            print("current exclusions: \n%s\n" % ", ".join(self.exclude))
        print("current directory tarjet: \n%s\n" % self.target_path)

        excluded_content = []
        excluded_content.extend(self.exclude)
        show_menu_tasks = True
        while True:
            answer = menu_select_task(show_menu_tasks)
            show_menu_tasks = False
            if answer == -1:
                continue

            elif answer == 4:
                pass

            elif answer == 3:
                excluded_content.clear()

            elif answer == 2:
                excluded_content.extend(set_new_file_exclusion_menu())
                show_menu_tasks = True

            elif answer == 1:
                self.exclude.clear()
                self.exclude.extend(excluded_content)

            elif answer == 0:
                sys.exit()

    def get_excluded_files(self) -> None:
        """Get exclusion files and extensions."""

    def set_excluded_files(self) -> None:
        """Set exclusion files and extensions."""


# ----------------------------------------------------------------------
if __name__ == "__main__":
    RemoverTool(
        __version__,
        __date__.replace("-", "")
    ).run()

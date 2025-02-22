"""This is deprecated, and has been renamed to powershell-core.py and pwsh.py
Module will get a proper library interface soon."""

import os
import platform


def main():

    cmd_table: dict[str, str] = {}
    match os.platform():
        case "win32":
            from table import win_stdin_cmds

            cmd_table = win_stdin_cmds
        case "linux":
            from table import lx_stdin_cmds

            cmd_table = lx_stdin_cmds
        case "darwin":
            from table import mac_stdin_cmds

            cmd_table = mac_stdin_cmds
        case _:
            print("Unsupported platform")


if __name__ == "__main__":
    main()

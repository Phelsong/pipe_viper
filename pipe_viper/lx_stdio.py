"""stdin/stdout for supported commands"""

from subprocess import PIPE, Popen
from .table import lx_stdin_cmds


def run_stdin_cmd(command, args):
    try:
        sesh = Popen(
            [command, args],
            universal_newlines=True,
            stdin=PIPE,
            stdout=PIPE,
        )
    except Exception as error:
        return error
    finally:
        out, err = sesh.communicate()
        return out, err


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        run_stdin_cmd(lx_stdin_cmds[sys.argv[1]], sys.argv[2])

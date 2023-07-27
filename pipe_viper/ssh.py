""" ssh pipeline core functionality """
from subprocess import PIPE, Popen
import sys
from asyncio import ensure_future


async def run_ssh_script(script_file_path: str) -> tuple[str, str]:
    try:
        sesh = await Popen(
            [f"ssh.exe {host}", script_file_path], universal_newlines=True, stdout=PIPE
        )
    except Exception as error:
        return error
    finally:
        out, err = sesh.communicate()
        return out, err


async def run_ssh_command(host: str, command: str) -> tuple[str, str]:
    print(f"ssh.exe {host}")
    try:
        sesh = await Popen(
            [f"ssh.exe {host}", command],
            universal_newlines=True,
            stdin=PIPE,
            stdout=PIPE,
        )
    except Exception as error:
        return error
    finally:
        out, err = sesh.communicate()
        print(out)
        return out, err


if __name__ == "__main__":
    args: list = sys.argv[1:]
    host: str = args[0]
    command = " ".join(args[1:])
    ensure_future(run_ssh_command(host, command))

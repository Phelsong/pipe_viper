
from subprocess import PIPE, Popen, Process
from pathlib import Path


def run_file_sync(cmd_file: Path) -> tuple[str, str]:
    try:
        sesh: Process = Popen(
            cmd_file, universal_newlines=True, stdout=PIPE, stderr=PIPE
        )
        out, err = sesh.communicate()
        return out, err
    except Exception as error:
        return (str(error), error)



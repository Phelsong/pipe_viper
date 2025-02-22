from asyncio import create_subprocess_shell
from asyncio.subprocess import PIPE as aPIPE, Process as aProcess
from pathlib import Path


async def run_file_async(cmd_file: Path) -> tuple[str, str]:
    try:
        sesh: aProcess = await create_subprocess_shell(
            cmd_file, universal_newlines=True, stdin=aPIPE, stdout=aPIPE, stderr=aPIPE
        )
        out, err = await sesh.communicate()
        return out, err
    except Exception as error:
        return (str(error), error)

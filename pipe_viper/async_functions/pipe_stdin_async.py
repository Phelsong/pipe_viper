from asyncio import run, create_subprocess_shell
from asyncio.subprocess import PIPE
import tempfile

TEST_CMD = "hyprctl activewindow -j"


async def to_stdin():

    with tempfile.TemporaryFile() as stream:
        stream.write(b"test")
        stream.seek(0)
        shell = await create_subprocess_shell(
            TEST_CMD,
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        )
        output = await shell.communicate(input=stream.read())
    print(output)
    # await p_stdin.wait()


if __name__ == "__main__":
    run(to_stdin())

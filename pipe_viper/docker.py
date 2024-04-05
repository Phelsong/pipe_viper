""" pwsh (powershell 7+) pipeline core functions."""

from subprocess import PIPE, Popen


def run_docker_compose_f(compose_path):
    try:
        sesh = Popen(
            ["docker compose -f", compose_path], universal_newlines=True, stdout=PIPE
        )
    except Exception as error:
        return error
    finally:
        out, err = sesh.communicate()
        return out, err


if __name__ == "__main__":
    run_docker_compose_f("./test.docker-compose.yaml")

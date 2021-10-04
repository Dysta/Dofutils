import subprocess


def run_cmd(cmd: list) -> None:
    """
    Run a command. Equivalent to:
    `poetry run <command>`
    """
    result = subprocess.run(cmd, capture_output=True)
    print(result.stdout.decode("utf8"), end="")
    print(result.stderr.decode("utf8"), end="")
    exit(code=result.returncode)


def tests() -> None:
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover`
    """
    TESTS_CMD = ["python", "-m", "unittest", "discover", "-v"]
    run_cmd(TESTS_CMD)


def fmt() -> None:
    """
    Run Black formatter to project. Equivalent to:
    `poetry run python -m black .`
    """
    FMT_CMD = ["python", "-m", "black", "."]
    run_cmd(FMT_CMD)


def type_check() -> None:
    """
    Run mypy typechecker to project. Equivalent to:
    `poetry run python -m mypy .`
    """
    TYPE_CHECK_CMD = ["python", "-m", "mypy", "."]
    run_cmd(TYPE_CHECK_CMD)

import subprocess


def launch() -> None:
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover`
    """
    subprocess.run(["python", "-m", "unittest", "discover", "-v"])

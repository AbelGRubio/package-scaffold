import os

from {{ cookiecutter.project_slug }}.configuration import __version__


if __name__ == "__main__":
    print(f"Package {{ cookiecutter.project_slug }} with version {__version__}")




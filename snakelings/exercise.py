"""Defines models for exercies."""

# standard library
from pathlib import Path

# third-party
from pydantic import BaseModel  # pylint: disable=no-name-in-module

# first-party


class Exercise(BaseModel):
    """A single exercise."""
    path: Path
    executable: str = 'python'
    pytest_args = ['--tb=short', '--no-header', '-p', 'no:cacheprovider']

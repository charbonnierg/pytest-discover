from __future__ import annotations

from pathlib import Path

import pytest
from pytest_discover import __version__

from ._utils import CommonTestSetup


@pytest.mark.basic
class TestErrors(CommonTestSetup):
    """Errors test suite."""

    def make_basic_test(self) -> Path:
        """A helper function to make a test file which emits errors on collection."""

        return self.make_testfile(
            "test_errors.py",
            """
            '''This is a module docstring.'''
            def some_function():
                '''Some docstring'''
                raise RuntimeError("BOOM")
            some_function()
            """,
        ).parent

    def test_json(self):
        """Test JSON report for test file with emit warnings on collection."""

        directory = self.make_basic_test()
        result = self.test_dir.runpytest(
            "--collect-only", "--collect-report", self.json_file.as_posix()
        )
        assert result.ret == 3
        assert self.json_file.exists()
        assert self.read_json_file() == {
            "pytest_version": pytest.__version__,
            "plugin_version": __version__,
            "exit_status": 3,
            "warnings": [],
            "errors": [
                {
                    "event": "ErrorMessage",
                    "when": "collect",
                    "location": {
                        "filename": directory.joinpath("test_errors.py").as_posix(),
                        "lineno": 4,
                    },
                    "traceback": {
                        "lines": [
                            f"{directory.joinpath('test_errors.py').as_posix()}:4: "
                            "RuntimeError: BOOM",
                        ],
                    },
                    "exception_type": "RuntimeError",
                    "exception_value": "BOOM",
                }
            ],
            "collect_reports": [
                {
                    "event": "CollectReport",
                    "node_id": None,
                    "items": [
                        {
                            "node_id": ".",
                            "node_type": "directory",
                            "name": directory.name,
                            "path": directory.as_posix(),
                        }
                    ],
                },
            ],
        }

    def test_jsonl(self):
        """Test JSON Lines report for test file which emits warnings on collection."""

        directory = self.make_basic_test()
        result = self.test_dir.runpytest(
            "--collect-only", "--collect-log", self.json_lines_file.as_posix()
        )
        assert result.ret == 3
        assert self.json_lines_file.exists()
        assert self.read_json_lines_file() == [
            {
                "pytest_version": pytest.__version__,
                "plugin_version": __version__,
                "event": "SessionStart",
            },
            {
                "event": "CollectReport",
                "node_id": None,
                "items": [
                    {
                        "node_id": ".",
                        "node_type": "directory",
                        "name": directory.name,
                        "path": directory.as_posix(),
                    }
                ],
            },
            {
                "event": "ErrorMessage",
                "when": "collect",
                "location": {
                    "filename": directory.joinpath("test_errors.py").as_posix(),
                    "lineno": 4,
                },
                "traceback": {
                    "lines": [
                        f"{directory.joinpath('test_errors.py').as_posix()}:4: "
                        "RuntimeError: BOOM",
                    ],
                },
                "exception_type": "RuntimeError",
                "exception_value": "BOOM",
            },
            {"exit_status": 3, "event": "SessionFinish"},
        ]
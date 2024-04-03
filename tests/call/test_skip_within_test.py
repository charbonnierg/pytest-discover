from __future__ import annotations

from pathlib import Path

import pytest
from pytest_discover import __version__

from ._utils import CommonTestSetup


@pytest.mark.basic
class TestSkipWithinTest(CommonTestSetup):
    """Scenario: A single test case within a single test file which calls skip() during execution."""

    def make_test_directory(self) -> Path:
        return self.make_testfile(
            "test_basic_skipped.py",
            """
            '''This is a module docstring.'''
            import pytest

            def test_skipped():
                '''This is a test docstring.'''
                pytest.skip("skipping this test")
                raise ValueError("BOOM")
            """,
        ).parent

    def test_json(self):
        """Test JSON report for single test case within single test file."""

        directory = self.make_test_directory()
        result = self.test_dir.runpytest("--collect-report", self.json_file.as_posix())
        assert result.ret == 0
        assert self.json_file.exists()
        assert self.read_json_file() == {
            "pytest_version": pytest.__version__,
            "plugin_version": __version__,
            "exit_status": 0,
            "errors": [],
            "warnings": [],
            "test_reports": [
                {
                    "node_id": "test_basic_skipped.py::test_skipped",
                    "outcome": "skipped",
                    "setup": {
                        "event_type": "case_setup",
                        "node_id": "test_basic_skipped.py::test_skipped",
                        "outcome": "passed",
                    },
                    "call": {
                        "event_type": "case_call",
                        "node_id": "test_basic_skipped.py::test_skipped",
                        "outcome": "skipped",
                    },
                    "teardown": {
                        "event_type": "case_teardown",
                        "node_id": "test_basic_skipped.py::test_skipped",
                        "outcome": "passed",
                    },
                    "finished": {
                        "event_type": "case_finished",
                        "node_id": "test_basic_skipped.py::test_skipped",
                        "outcome": "skipped",
                    },
                }
            ],
            "collect_reports": [
                {
                    "event": "CollectReport",
                    "node_id": "",
                    "items": [
                        {
                            "node_id": ".",
                            "node_type": "directory",
                            "name": directory.name,
                            "path": directory.name,
                        }
                    ],
                },
                {
                    "event": "CollectReport",
                    "node_id": "test_basic_skipped.py",
                    "items": [
                        {
                            "node_id": "test_basic_skipped.py::test_skipped",
                            "node_type": "case",
                            "name": "test_skipped",
                            "doc": "This is a test docstring.",
                            "markers": [],
                            "parameters": {},
                            "path": directory.joinpath("test_basic_skipped.py")
                            .relative_to(directory.parent)
                            .as_posix(),
                            "module": "test_basic_skipped",
                            "suite": None,
                            "function": "test_skipped",
                        }
                    ],
                },
                {
                    "event": "CollectReport",
                    "node_id": ".",
                    "items": [
                        {
                            "node_id": "test_basic_skipped.py",
                            "name": "test_basic_skipped.py",
                            "path": directory.joinpath("test_basic_skipped.py")
                            .relative_to(directory.parent)
                            .as_posix(),
                            "doc": "This is a module docstring.",
                            "markers": [],
                            "node_type": "module",
                        }
                    ],
                },
            ],
        }

    def test_jsonl_basic(self):
        """Test JSON Lines report for single test case within single test file."""

        directory = self.make_test_directory()
        result = self.test_dir.runpytest(
            "--collect-log", self.json_lines_file.as_posix()
        )
        assert result.ret == 0
        assert self.json_lines_file.exists()
        assert self.read_json_lines_file() == [
            {
                "pytest_version": pytest.__version__,
                "plugin_version": __version__,
                "event": "SessionStart",
            },
            {
                "event": "CollectReport",
                "node_id": "",
                "items": [
                    {
                        "node_id": ".",
                        "node_type": "directory",
                        "name": directory.name,
                        "path": directory.name,
                    }
                ],
            },
            {
                "event": "CollectReport",
                "node_id": "test_basic_skipped.py",
                "items": [
                    {
                        "node_id": "test_basic_skipped.py::test_skipped",
                        "node_type": "case",
                        "name": "test_skipped",
                        "doc": "This is a test docstring.",
                        "markers": [],
                        "parameters": {},
                        "path": directory.joinpath("test_basic_skipped.py")
                        .relative_to(directory.parent)
                        .as_posix(),
                        "module": "test_basic_skipped",
                        "suite": None,
                        "function": "test_skipped",
                    },
                ],
            },
            {
                "event": "CollectReport",
                "node_id": ".",
                "items": [
                    {
                        "node_id": "test_basic_skipped.py",
                        "name": "test_basic_skipped.py",
                        "path": directory.joinpath("test_basic_skipped.py")
                        .relative_to(directory.parent)
                        .as_posix(),
                        "doc": "This is a module docstring.",
                        "markers": [],
                        "node_type": "module",
                    }
                ],
            },
            {
                "event_type": "case_setup",
                "node_id": "test_basic_skipped.py::test_skipped",
                "outcome": "passed",
            },
            {
                "event_type": "case_call",
                "node_id": "test_basic_skipped.py::test_skipped",
                "outcome": "skipped",
            },
            {
                "event_type": "case_teardown",
                "node_id": "test_basic_skipped.py::test_skipped",
                "outcome": "passed",
            },
            {
                "event_type": "case_finished",
                "node_id": "test_basic_skipped.py::test_skipped",
                "outcome": "skipped",
            },
            {"exit_status": 0, "event": "SessionFinish"},
        ]

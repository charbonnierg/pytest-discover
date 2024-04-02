from __future__ import annotations

from pathlib import Path

import pytest
from pytest_discover import __version__

from ._utils import CommonTestSetup


@pytest.mark.suites
@pytest.mark.filetree
class TestMultiSuite(CommonTestSetup):
    """Scenario: Several test suites within several test files."""

    def make_test_directory(self) -> Path:
        self.make_testfile(
            "test_module_1.py",
            """
            class TestSuite1:
                '''This is a suite docstring'''
                def test_1():
                    '''This is a first docstring.'''
                    pass
                def test_2():
                    '''This is a second docstring.'''
                    pass
            class TestSuite2:
                '''This is a suite docstring'''
                def test_3():
                    '''This is a third docstring.'''
                    pass
                def test_4():
                    '''This is a fourth docstring.'''
                    pass
            """,
        )
        return self.make_testfile(
            "test_module_2.py",
            """
            class TestSuite3:
                '''This is a suite docstring'''
                def test_5():
                    '''This is a fifth docstring.'''
                    pass
                def test_6():
                    '''This is a sixth docstring.'''
                    pass
            class TestSuite4:
                '''This is a suite docstring'''
                def test_7():
                    '''This is a seventh docstring.'''
                    pass
                def test_8():
                    '''This is a eighth docstring.'''
                    pass
            """,
        ).parent

    def test_json(self):
        """Test JSON report for several test suites within several test files."""

        directory = self.make_test_directory()
        result = self.test_dir.runpytest(
            "--collect-only", "--collect-report", self.json_file.as_posix()
        )
        assert result.ret == 0
        assert self.json_file.exists()
        assert self.read_json_file() == {
            "pytest_version": pytest.__version__,
            "plugin_version": __version__,
            "exit_status": 0,
            "errors": [],
            "warnings": [],
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
                            "markers": [],
                        }
                    ],
                },
                {
                    "event": "CollectReport",
                    "node_id": "test_module_1.py::TestSuite1",
                    "items": [
                        {
                            "node_id": "test_module_1.py::TestSuite1::test_1",
                            "node_type": "case",
                            "name": "test_1",
                            "doc": "This is a first docstring.",
                            "markers": [],
                            "parameters": {},
                            "file": "test_module_1.py",
                            "module": "test_module_1",
                            "parent": "TestSuite1",
                            "function": "test_1",
                        },
                        {
                            "node_id": "test_module_1.py::TestSuite1::test_2",
                            "node_type": "case",
                            "name": "test_2",
                            "doc": "This is a second docstring.",
                            "markers": [],
                            "parameters": {},
                            "file": "test_module_1.py",
                            "module": "test_module_1",
                            "parent": "TestSuite1",
                            "function": "test_2",
                        },
                    ],
                },
                {
                    "event": "CollectReport",
                    "node_id": "test_module_1.py::TestSuite2",
                    "items": [
                        {
                            "node_id": "test_module_1.py::TestSuite2::test_3",
                            "node_type": "case",
                            "name": "test_3",
                            "doc": "This is a third docstring.",
                            "markers": [],
                            "parameters": {},
                            "file": "test_module_1.py",
                            "module": "test_module_1",
                            "parent": "TestSuite2",
                            "function": "test_3",
                        },
                        {
                            "node_id": "test_module_1.py::TestSuite2::test_4",
                            "node_type": "case",
                            "name": "test_4",
                            "doc": "This is a fourth docstring.",
                            "markers": [],
                            "parameters": {},
                            "file": "test_module_1.py",
                            "module": "test_module_1",
                            "parent": "TestSuite2",
                            "function": "test_4",
                        },
                    ],
                },
                {
                    "event": "CollectReport",
                    "node_id": "test_module_2.py::TestSuite3",
                    "items": [
                        {
                            "node_id": "test_module_2.py::TestSuite3::test_5",
                            "node_type": "case",
                            "name": "test_5",
                            "doc": "This is a fifth docstring.",
                            "markers": [],
                            "parameters": {},
                            "file": "test_module_2.py",
                            "module": "test_module_2",
                            "parent": "TestSuite3",
                            "function": "test_5",
                        },
                        {
                            "node_id": "test_module_2.py::TestSuite3::test_6",
                            "node_type": "case",
                            "name": "test_6",
                            "doc": "This is a sixth docstring.",
                            "markers": [],
                            "parameters": {},
                            "file": "test_module_2.py",
                            "module": "test_module_2",
                            "parent": "TestSuite3",
                            "function": "test_6",
                        },
                    ],
                },
                {
                    "event": "CollectReport",
                    "node_id": "test_module_2.py::TestSuite4",
                    "items": [
                        {
                            "node_id": "test_module_2.py::TestSuite4::test_7",
                            "node_type": "case",
                            "name": "test_7",
                            "doc": "This is a seventh docstring.",
                            "markers": [],
                            "parameters": {},
                            "file": "test_module_2.py",
                            "module": "test_module_2",
                            "parent": "TestSuite4",
                            "function": "test_7",
                        },
                        {
                            "node_id": "test_module_2.py::TestSuite4::test_8",
                            "node_type": "case",
                            "name": "test_8",
                            "doc": "This is a eighth docstring.",
                            "markers": [],
                            "parameters": {},
                            "file": "test_module_2.py",
                            "module": "test_module_2",
                            "parent": "TestSuite4",
                            "function": "test_8",
                        },
                    ],
                },
            ],
        }

    def test_jsonl(self):
        """Test JSON Lines report for several test suites within several test files."""

        directory = self.make_test_directory()
        result = self.test_dir.runpytest(
            "--collect-only", "--collect-log", self.json_lines_file.as_posix()
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
                "node_id": None,
                "items": [
                    {
                        "node_id": ".",
                        "node_type": "directory",
                        "name": directory.name,
                        "path": directory.as_posix(),
                        "markers": [],
                    }
                ],
            },
            {
                "event": "CollectReport",
                "node_id": "test_module_1.py::TestSuite1",
                "items": [
                    {
                        "node_id": "test_module_1.py::TestSuite1::test_1",
                        "node_type": "case",
                        "name": "test_1",
                        "doc": "This is a first docstring.",
                        "markers": [],
                        "parameters": {},
                        "file": "test_module_1.py",
                        "module": "test_module_1",
                        "parent": "TestSuite1",
                        "function": "test_1",
                    },
                    {
                        "node_id": "test_module_1.py::TestSuite1::test_2",
                        "node_type": "case",
                        "name": "test_2",
                        "doc": "This is a second docstring.",
                        "markers": [],
                        "parameters": {},
                        "file": "test_module_1.py",
                        "module": "test_module_1",
                        "parent": "TestSuite1",
                        "function": "test_2",
                    },
                ],
            },
            {
                "event": "CollectReport",
                "node_id": "test_module_1.py::TestSuite2",
                "items": [
                    {
                        "node_id": "test_module_1.py::TestSuite2::test_3",
                        "node_type": "case",
                        "name": "test_3",
                        "doc": "This is a third docstring.",
                        "markers": [],
                        "parameters": {},
                        "file": "test_module_1.py",
                        "module": "test_module_1",
                        "parent": "TestSuite2",
                        "function": "test_3",
                    },
                    {
                        "node_id": "test_module_1.py::TestSuite2::test_4",
                        "node_type": "case",
                        "name": "test_4",
                        "doc": "This is a fourth docstring.",
                        "markers": [],
                        "parameters": {},
                        "file": "test_module_1.py",
                        "module": "test_module_1",
                        "parent": "TestSuite2",
                        "function": "test_4",
                    },
                ],
            },
            {
                "event": "CollectReport",
                "node_id": "test_module_2.py::TestSuite3",
                "items": [
                    {
                        "node_id": "test_module_2.py::TestSuite3::test_5",
                        "node_type": "case",
                        "name": "test_5",
                        "doc": "This is a fifth docstring.",
                        "markers": [],
                        "parameters": {},
                        "file": "test_module_2.py",
                        "module": "test_module_2",
                        "parent": "TestSuite3",
                        "function": "test_5",
                    },
                    {
                        "node_id": "test_module_2.py::TestSuite3::test_6",
                        "node_type": "case",
                        "name": "test_6",
                        "doc": "This is a sixth docstring.",
                        "markers": [],
                        "parameters": {},
                        "file": "test_module_2.py",
                        "module": "test_module_2",
                        "parent": "TestSuite3",
                        "function": "test_6",
                    },
                ],
            },
            {
                "event": "CollectReport",
                "node_id": "test_module_2.py::TestSuite4",
                "items": [
                    {
                        "node_id": "test_module_2.py::TestSuite4::test_7",
                        "node_type": "case",
                        "name": "test_7",
                        "doc": "This is a seventh docstring.",
                        "markers": [],
                        "parameters": {},
                        "file": "test_module_2.py",
                        "module": "test_module_2",
                        "parent": "TestSuite4",
                        "function": "test_7",
                    },
                    {
                        "node_id": "test_module_2.py::TestSuite4::test_8",
                        "node_type": "case",
                        "name": "test_8",
                        "doc": "This is a eighth docstring.",
                        "markers": [],
                        "parameters": {},
                        "file": "test_module_2.py",
                        "module": "test_module_2",
                        "parent": "TestSuite4",
                        "function": "test_8",
                    },
                ],
            },
            {"exit_status": 0, "event": "SessionFinish"},
        ]

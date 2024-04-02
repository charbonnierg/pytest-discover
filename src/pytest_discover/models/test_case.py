# generated by datamodel-codegen:
#   filename:  test_case.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class TestCase:
    """
    Pytest Test Case
    """

    node_id: str
    """
    Node ID
    """
    name: str
    """
    Test Name
    """
    doc: str
    """
    Test docstring
    """
    markers: List[str]
    """
    Test markers
    """
    parameters: Dict[str, str]
    """
    Test parameters names and types
    """
    node_type: str = "case"
    """
    Node Type
    """
    path: Optional[str] = None
    """
    File path
    """
    module: Optional[str] = None
    """
    Module name
    """
    suite: Optional[str] = None
    """
    Parent suite
    """
    function: Optional[str] = None
    """
    Function name
    """
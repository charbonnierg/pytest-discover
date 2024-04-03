# generated by datamodel-codegen:
#   filename:  test_case_call.json

from __future__ import annotations

from dataclasses import dataclass

from . import outcome


@dataclass
class TestCaseCall:
    """
    Pytest Test Case Call
    """

    node_id: str
    """
    Node ID
    """
    outcome: outcome.Outcome
    event_type: str = "case_call"
    """
    Event Type
    """

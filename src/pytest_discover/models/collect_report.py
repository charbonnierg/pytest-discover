# generated by datamodel-codegen:
#   filename:  collect_report.json

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Union

from . import test_case, test_directory


@dataclass
class CollectReport:
    """
    Pytest Collect Report
    """

    items: List[Union[test_directory.TestDirectory, test_case.TestCase]]
    """
    The collected items
    """
    event: str = "CollectReport"
    """
    The event type
    """
    node_id: Optional[str] = None
    """
    The node id of the collector (if any)
    """

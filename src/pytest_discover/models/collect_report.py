# generated by datamodel-codegen:
#   filename:  collect_report.json

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from . import test_item


@dataclass
class CollectReport:
    """
    Pytest Collect Report
    """

    items: List[test_item.TestItem]
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

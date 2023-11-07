#!/usr/bin/env python
"""
Models the CVSS Confidentiality Requirement metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_NOT_DEFINED = SsvcDecisionPointValue(
    name="Not Defined",
    key="ND",
    description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
)

_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Loss of confidentiality is likely to have a catastrophic adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
)

_MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Loss of confidentiality is likely to have a serious adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Loss of confidentiality is likely to have only a limited adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).",
)

CONFIDENTIALITY_REQUIREMENT_1 = CvssDecisionPoint(
    name="Confidentiality Requirement",
    description="This metric measures the impact to the confidentiality of a successfully exploited vulnerability.",
    key="CR",
    version="1.0.0",
    values=(
        _LOW,
        _MEDIUM,
        _HIGH,
        _NOT_DEFINED,
    ),
)
"""
Defines Low, Medium, High, and Not Defined values for CVSS Confidentiality Requirement.
"""


def main():
    print(CONFIDENTIALITY_REQUIREMENT_1.to_json(indent=2))


if __name__ == "__main__":
    main()

# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from datetime import datetime
from enum import Enum, auto
from typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values
from spdx_tools.spdx3.model import (
    CreationInformation,
    ExternalIdentifier,
    ExternalReference,
    IntegrityMethod,
    LifecycleScopedRelationship,
    LifecycleScopeType,
    RelationshipCompleteness,
    RelationshipType,
)


class SoftwareDependencyLinkType(Enum):
    STATIC = auto()
    DYNAMIC = auto()
    TOOL = auto()
    OTHER = auto()


class DependencyConditionalityType(Enum):
    OPTIONAL = auto()
    REQUIRED = auto()
    PROVIDED = auto()
    PREREQUISITE = auto()
    OTHER = auto()


@dataclass_with_properties
class SoftwareDependencyRelationship(LifecycleScopedRelationship):
    software_linkage: Optional[SoftwareDependencyLinkType] = None
    conditionality: Optional[DependencyConditionalityType] = None

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInformation,
        from_element: str,
        to: List[str],
        relationship_type: RelationshipType,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = None,
        external_references: List[ExternalReference] = None,
        external_identifier: List[ExternalIdentifier] = None,
        extension: None = None,
        completeness: Optional[RelationshipCompleteness] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        scope: Optional[LifecycleScopeType] = None,
        software_linkage: Optional[SoftwareDependencyLinkType] = None,
        conditionality: Optional[DependencyConditionalityType] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_references = [] if external_references is None else external_references
        external_identifier = [] if external_identifier is None else external_identifier
        check_types_and_set_values(self, locals())
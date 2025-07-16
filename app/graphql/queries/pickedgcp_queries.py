import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import PickedGCPType, Connection, Edge, PageInfo
from app.services import PickedGCPService

@strawberry.type
class PickedGCPQuery:
    @strawberry.field
    async def pickedGCP(self, info: Info, calibration_id: int, gcp_id: int) -> Optional[PickedGCPType]:
        """Fetches a single PickedGCP by its composite ID."""
        db = info.context["db"]
        item = await PickedGCPService.get_by_ids(db, calibration_id=calibration_id, gcp_id=gcp_id)
        return PickedGCPType(**item.dict()) if item else None

    @strawberry.field
    async def pickedGCPs(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[PickedGCPType]:
        """Fetches a paginated list of all PickedGCPs."""
        db = info.context["db"]
        items, total = await PickedGCPService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=PickedGCPType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def pickedGCPs_by_calibration(self, info: Info, calibration_id: int, skip: int = 0, limit: int = 10) -> Connection[PickedGCPType]:
        """Fetches PickedGCPs for a specific calibration."""
        db = info.context["db"]
        items, total = await PickedGCPService.get_for_calibration(db, calibration_id, skip, limit)
        edges = [Edge(node=PickedGCPType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def pickedGCPs_by_gcp(self, info: Info, gcp_id: int, skip: int = 0, limit: int = 10) -> Connection[PickedGCPType]:
        """Fetches PickedGCPs for a specific GCP."""
        db = info.context["db"]
        items, total = await PickedGCPService.get_for_gcp(db, gcp_id, skip, limit)
        edges = [Edge(node=PickedGCPType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def pickedGCP_total(self, info: Info) -> int:
        """Returns the total number of PickedGCPs."""
        db = info.context["db"]
        _, total = await PickedGCPService.get_all_paginated(db, 0, 0)
        return total
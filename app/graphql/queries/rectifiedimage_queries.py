import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import RectifiedImageType, Connection, Edge, PageInfo
from app.services import RectifiedImageService, ImageService

@strawberry.type
class RectifiedImageQuery:
    
    @strawberry.field
    async def rectifiedimage(self, info: Info, id: int) -> Optional[RectifiedImageType]:
        db = info.context["db"]
        rectifiedimage = await RectifiedImageService.get_rectifiedimage_by_id(db, rectifiedimage_id=id)
        return RectifiedImageType(**rectifiedimage.dict()) if rectifiedimage else None


    @strawberry.field
    async def rectifiedimage_by_image(
        self, info: Info, image_id: int, skip: int = 0, limit: int = 10
    ) -> Connection[RectifiedImageService]:
        db = info.context["db"]
        if not await ImageService.get_image_by_id(db, image_id):
             raise ValueError(f"Image with ID {image_id} not found.")

        rectifiedimages, total_count = await ImageService.get_image_by_id(db, image_id, skip, limit)
        
        edges = [
            Edge(node=RectifiedImageType(**rectifiedimage.dict()), cursor=str(skip + i))
            for i, rectifiedimage in enumerate(rectifiedimages)
        ]

        page_info = PageInfo(
            has_next_page=skip + limit < total_count,
            has_previous_page=skip > 0,
            start_cursor=edges[0].cursor if edges else None,
            end_cursor=edges[-1].cursor if edges else None,
        )
        
        return Connection(total_count=total_count, edges=edges, page_info=page_info)



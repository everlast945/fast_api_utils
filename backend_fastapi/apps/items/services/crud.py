import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from apps.items.domain.item import ItemDomain
from apps.items.entity.item import ItemEntity


async def items_list(session: AsyncSession, limit: int = 20) -> list[ItemDomain]:
    sql = sa.select(
        ItemEntity
    ).order_by(
        ItemEntity.name.desc()
    ).limit(limit)
    result = await session.execute(sql)

    items = result.scalars().all()

    return [
        ItemDomain(**{field: getattr(item, field) for field in ItemDomain.__fields__})
        for item in items
    ][:10]


def items_create(session: AsyncSession, item: ItemDomain):
    new_item = ItemEntity(**dict(item))
    session.add(new_item)
    return new_item


async def items_read(session: AsyncSession, item_id: int) -> ItemDomain:
    sql = sa.select(ItemEntity).where(
        ItemEntity.id == item_id,
    ).limit(1)
    result = await session.execute(sql)
    item = result.scalars().one()
    return ItemDomain(**{field: getattr(item, field) for field in ItemDomain.__fields__})
# Code generated by op-codegen - DO NO EDIT MANUALLY

from .core import _invoke, _invoke_sync
from json import loads
from .iterator import SDKIterator
from .items_share import ItemsShare
from .types import Item, ItemCreateParams, ItemOverview


class Items:
    """
    The Items API holds all operations the SDK client can perform on 1Password items.
    """

    def __init__(self, client_id):
        self.client_id = client_id
        self.share = ItemsShare(client_id)

    async def create(self, params: ItemCreateParams) -> Item:
        """
        Create a new item
        """
        response = await _invoke(
            {
                "invocation": {
                    "clientId": self.client_id,
                    "parameters": {
                        "name": "ItemsCreate",
                        "parameters": {"params": params.model_dump(by_alias=True)},
                    },
                }
            }
        )
        return Item.model_validate_json(response)

    async def get(self, vault_id: str, item_id: str) -> Item:
        """
        Get an item by vault and item ID
        """
        response = await _invoke(
            {
                "invocation": {
                    "clientId": self.client_id,
                    "parameters": {
                        "name": "ItemsGet",
                        "parameters": {"vault_id": vault_id, "item_id": item_id},
                    },
                }
            }
        )
        return Item.model_validate_json(response)

    async def get_all(self, vault_id: str, item_ids: list[str]) -> list[Item]:
        """
        Get items by vault and their item IDs.
        """
        response = await _invoke(
            {
                "invocation": {
                    "clientId": self.client_id,
                    "parameters": {
                        "name": "ItemsGetAll",
                        "parameters": {"vault_id": vault_id, "item_ids": item_ids},
                    },
                }
            }
        )

        response = loads(response)
        response = [Item.model_validate(data) for data in response]
        return response

    async def put(self, item: Item) -> Item:
        """
        Update an existing item.
        """
        response = await _invoke(
            {
                "invocation": {
                    "clientId": self.client_id,
                    "parameters": {
                        "name": "ItemsPut",
                        "parameters": {"item": item.model_dump(by_alias=True)},
                    },
                }
            }
        )
        return Item.model_validate_json(response)

    async def delete(self, vault_id: str, item_id: str):
        """
        Delete an item.
        """
        await _invoke(
            {
                "invocation": {
                    "clientId": self.client_id,
                    "parameters": {
                        "name": "ItemsDelete",
                        "parameters": {"vault_id": vault_id, "item_id": item_id},
                    },
                }
            }
        )

    async def archive(self, vault_id: str, item_id: str):
        """
        Archive an item.
        """
        await _invoke(
            {
                "invocation": {
                    "clientId": self.client_id,
                    "parameters": {
                        "name": "ItemsArchive",
                        "parameters": {"vault_id": vault_id, "item_id": item_id},
                    },
                }
            }
        )

    async def list_all(self, vault_id: str) -> SDKIterator[ItemOverview]:
        """
        List all items
        """
        response = await _invoke(
            {
                "invocation": {
                    "clientId": self.client_id,
                    "parameters": {
                        "name": "ItemsListAll",
                        "parameters": {"vault_id": vault_id},
                    },
                }
            }
        )

        response = loads(response)
        response = [ItemOverview.model_validate(data) for data in response]
        return SDKIterator(response)

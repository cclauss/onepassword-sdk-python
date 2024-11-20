# Code generated by op-codegen - DO NO EDIT MANUALLY

from .core import _invoke, _invoke_sync
from json import loads
from .iterator import SDKIterator
from .types import Item, ItemOverview


class Items:
    """
    The Items API holds all operations the SDK client can perform on 1Password items.
    """

    def __init__(self, client_id):
        self.client_id = client_id

    async def create(self, params):
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

    async def get(self, vault_id, item_id):
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

    async def put(self, item):
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

    async def delete(self, vault_id, item_id):
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

    async def list_all(self, vault_id):
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

        response_data = loads(response)

        objects = [ItemOverview.model_validate(data) for data in response_data]

        return SDKIterator(objects)

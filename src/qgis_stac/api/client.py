
from .base import BaseClient
from .models import Collection, Item, ResourcePagination


class Client(BaseClient):
    """ API client class that provides implementation of the
    STAC API querying operations.
        """
    def handle_items(
            self,
            items_response
    ):
        """Emits the search results items, so plugin signal observers
        eg. gui can use the data.

        :param items_response: Search results items
        :type items_response: List[models.Items]
        """
        items = []
        pagination = self.get_pagination(items_response.get_item_collections()[0])
        for item_collection in items_response.get_item_collections():
            for item in item_collection:
                item_result = Item(
                    id=item.id
                )
                items.append(item_result)

        self.items_received.emit(items, pagination)

    def handle_collections(
            self,
            collections_response
    ):
        """Emits the search results collections.

        :param collections_response: Search results collections
        :type collections_response: List[models.Collection]
        """
        collections = []
        for collection in collections_response:
            collection_result = Collection(
                id=collection.id,
                title=collection.title
            )
            collections.append(collection_result)

        # TODO query filter pagination results from the
        # response
        pagination = ResourcePagination()

        self.collections_received.emit(collections, pagination)

    def handle_error(
            self,
            message: str
    ):
        """Emits the found error message.

        :param message: Error message
        :type message: str
        """
        self.error_received.emit(message)

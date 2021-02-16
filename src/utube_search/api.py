"""external api for YTSearch."""
import asyncio

import uvloop

from utube_search.exceptions import YtsException
from utube_search.search import YtSearch

uvloop.install()


async def search(query: str, cache: bool = False, kind="json"):
    """external search api."""
    yts = YtSearch(query, cache)
    await yts.search()
    if kind == "list":
        return yts.to_list()
    elif kind == "json":
        return yts.to_json()
    elif kind == "str":
        return yts.to_str()
    else:
        raise YtsException(
            "not a valid kind, valid kind should be one of dict, json, str"
        )


def main(query, cache, kind):
    return asyncio.run(search(query, cache, kind))

"""fetch youtube videos based on search keyword."""

import asyncio
from pathlib import Path

import aiofiles
import aiohttp

import rapidjson as json
import uvloop

from utube_search.config import YOUTUBE_URL

uvloop.install()


class YtSearch:
    """YtSearch - search youtube using a query string.

    if cache is set to true, query results will be stored to disk.
    """

    def __init__(self, query, cache=True):
        self.query = query
        self.cache = cache
        self.fname = Path(f"{query}.json")
        self.query_results = []

    async def _download_page(self):
        """download page with search query."""
        async with aiohttp.ClientSession() as session:
            async with session.get(YOUTUBE_URL.format(self.query)) as response:
                if response.status != 404:
                    self.content = await response.text()

    async def to_disk(self):
        """write query query_results to file."""
        async with aiofiles.open(f"{self.fname}", "w") as fh:
            await fh.write(json.dumps(self.query_results))
        return json.dumps({"fname": str(self.fname)})

    def to_json(self):
        """return query result as json string."""
        return json.dumps({"query_results": self.query_results})

    def to_list(self):
        """return query content list."""
        return self.query_results

    def to_str(self):
        """convert query json to string."""
        return str(self.query_results)

    async def search(self):
        """search for query and update result dictionary."""
        if not self.fname.exists():
            await self._download_page()
            # orignal ref: https://github.com/joetats/youtube_search/blob/cd0596a4830332843ca3c7c3560b360654d2dadc/youtube_search/__init__.py
            from_idx = self.content.index("ytInitialData") + 16
            to_idx = self.content.index("};", from_idx) + 1
            content = json.loads(self.content[from_idx:to_idx])
            video_list = content["contents"]["twoColumnSearchResultsRenderer"][
                "primaryContents"
            ]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]
            for video in video_list:
                query_result = {}
                if "videoRenderer" in video.keys():
                    content = video.get("videoRenderer", {})
                    query_result["title"] = (
                        content.get("title", {})
                        .get("runs", [[{}]])[0]
                        .get("text", None)
                    )
                    query_result["view_count"] = int(
                        "".join(
                            content.get("viewCountText", {})
                            .get("simpleText", 0)
                            .split(" ")[0]
                            .split(",")
                        )
                    )
                    query_result["url"] = "www.youtube.com" + (
                        content.get("navigationEndpoint", {})
                        .get("commandMetadata", {})
                        .get("webCommandMetadata", {})
                        .get("url", None)
                    )
                    query_result["duration"] = content.get("lengthText", {}).get(
                        "simpleText", 0
                    )
                    query_result["publish_time"] = content.get(
                        "publishedTimeText", {}
                    ).get("simpleText", 0)
                    self.query_results.append(query_result)
                    if self.cache:
                        await self.to_disk()
                    elif self.cache:
                        self.fname.unlink()
        elif self.cache:
            async with aiofiles.open(self.fname, "r") as fh:
                self.query_results = json.loads(await fh.read())


async def main(query="electromagnetism"):
    yts = YtSearch(query, cache=True)
    await yts.search()


if __name__ == "__main__":
    asyncio.run(main(query="spacetime"))

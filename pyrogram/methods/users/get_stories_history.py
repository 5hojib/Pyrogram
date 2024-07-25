import logging
from typing import AsyncGenerator, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types

log = logging.getLogger(__name__)


class GetUserStoriesHistory:
    async def get_stories_history(
        self: "pyrogram.Client", chat_id: int = None, limit: int = 0, offset_id: int = 0
    ) -> Optional[AsyncGenerator["types.Story", None]]:
        """Get stories history.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int``, *optional*):
                Unique identifier (int) of the target channel.
                You can also use user profile/channel public link in form of *t.me/<username>* (str).

            limit (``int``, *optional*):
                Limits the number of stories to be retrieved.
                By default, no limit is applied and all stories are returned.

            offset_id (``int``, *optional*):
                Identifier of the first story to be returned.

        Returns:
            ``Generator``: On success, a generator yielding :obj:`~pyrogram.types.Story` objects is returned.

        Example:
            .. code-block:: python

                # Get story history
                async for story in app.get_stories_history():
                    print(story)

        Raises:
            ValueError: In case of invalid arguments.
        """

        if chat_id:
            peer = await self.resolve_peer(chat_id)
        else:
            peer = await self.resolve_peer("me")

        rpc = raw.functions.stories.GetStoriesArchive(
            peer=peer, offset_id=offset_id, limit=limit
        )

        r = await self.invoke(rpc, sleep_threshold=-1)

        for story in r.stories:
            yield await types.Story._parse(self, story, peer)

from __future__ import annotations

import pyrogram
from pyrogram import raw, types
from pyrogram.types.object import Object


class ChatReactions(Object):
    """A chat reactions

    Parameters:
        all_are_enabled (``bool``, *optional*)

        allow_custom_emoji (``bool``, *optional*):
            Whether custom emoji are allowed or not.

        reactions (List of :obj:`~pyrogram.types.Reaction`, *optional*):
            Reactions available.
    """

    def __init__(
        self,
        *,
        client: pyrogram.Client = None,
        all_are_enabled: bool | None = None,
        allow_custom_emoji: bool | None = None,
        reactions: list[types.Reaction] | None = None,
    ) -> None:
        super().__init__(client)

        self.all_are_enabled = all_are_enabled
        self.allow_custom_emoji = allow_custom_emoji
        self.reactions = reactions

    @staticmethod
    def _parse(
        client, chat_reactions: raw.base.ChatReactions
    ) -> ChatReactions | None:
        if isinstance(chat_reactions, raw.types.ChatReactionsAll):
            return ChatReactions(
                client=client,
                all_are_enabled=True,
                allow_custom_emoji=chat_reactions.allow_custom,
            )

        if isinstance(chat_reactions, raw.types.ChatReactionsSome):
            return ChatReactions(
                client=client,
                reactions=[
                    types.ReactionType._parse(reaction)
                    for reaction in chat_reactions.reactions
                ],
            )
        if isinstance(chat_reactions, raw.types.ChatReactionsNone):
            return None

        return None

from __future__ import annotations

from typing import TYPE_CHECKING

from .handler import Handler

if TYPE_CHECKING:
    from collections.abc import Callable


class DisconnectHandler(Handler):
    """The Disconnect handler class. Used to handle disconnections. It is intended to be used with
    :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_disconnect` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a disconnection occurs. It takes *(client)*
            as positional argument (look at the section below for a detailed description).

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself. Useful, for example, when you want to change the proxy before a new connection
            is established.
    """

    def __init__(self, callback: Callable) -> None:
        super().__init__(callback)

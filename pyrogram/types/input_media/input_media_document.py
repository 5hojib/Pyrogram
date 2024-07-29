from __future__ import annotations

from typing import TYPE_CHECKING, BinaryIO, Optional

from pyrogram.types.messages_and_media import MessageEntity

from .input_media import InputMedia

if TYPE_CHECKING:
    from pyrogram import enums


class InputMediaDocument(InputMedia):
    """A generic file to be sent inside an album.

    Parameters:
        media (``str`` | ``BinaryIO``):
            File to send.
            Pass a file_id as string to send a file that exists on the Telegram servers or
            pass a file path as string to upload a new file that exists on your local machine or
            pass a binary file-like object with its attribute “.name” set for in-memory uploads or
            pass an HTTP URL as a string for Telegram to get a file from the Internet.

        thumb (``str``):
            Thumbnail of the file sent.
            The thumbnail should be in JPEG format and less than 200 KB in size.
            A thumbnail's width and height should not exceed 320 pixels.
            Thumbnails can't be reused and can be only uploaded as a new file.

        caption (``str``, *optional*):
            Caption of the document to be sent, 0-1024 characters.
            If not specified, the original caption is kept. Pass "" (empty string) to remove the caption.

        parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
            By default, texts are parsed using both Markdown and HTML styles.
            You can combine both syntaxes together.

        caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
            List of special entities that appear in the caption, which can be specified instead of *parse_mode*.
    """

    def __init__(
        self,
        media: str | BinaryIO,
        thumb: str | None = None,
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: list[MessageEntity] | None = None,
    ) -> None:
        super().__init__(media, caption, parse_mode, caption_entities)

        self.thumb = thumb

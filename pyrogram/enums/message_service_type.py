from enum import auto
from .auto_name import AutoName


class MessageServiceType(AutoName):
    NEW_CHAT_MEMBERS = auto()
    CHAT_JOINED_BY_REQUEST = auto()
    LEFT_CHAT_MEMBERS = auto()
    NEW_CHAT_TITLE = auto()
    NEW_CHAT_PHOTO = auto()
    DELETE_CHAT_PHOTO = auto()
    GROUP_CHAT_CREATED = auto()
    CHANNEL_CHAT_CREATED = auto()
    MIGRATE_TO_CHAT_ID = auto()
    MIGRATE_FROM_CHAT_ID = auto()
    PINNED_MESSAGE = auto()
    GAME_HIGH_SCORE = auto()
    ChannelShared = auto()
    UserShared = auto()
    FORUM_TOPIC_CREATED = auto()
    FORUM_TOPIC_CLOSED = auto()
    FORUM_TOPIC_REOPENED = auto()
    FORUM_TOPIC_EDITED = auto()
    GENERAL_TOPIC_HIDDEN = auto()
    GENERAL_TOPIC_UNHIDDEN = auto()
    VIDEO_CHAT_STARTED = auto()
    VIDEO_CHAT_ENDED = auto()
    VIDEO_CHAT_SCHEDULED = auto()
    VIDEO_CHAT_MEMBERS_INVITED = auto()
    WEB_APP_DATA = auto()
    GIFTED_PREMIUM = auto()
    GIVEAWAY_LAUNCHED = auto()
    GIVEAWAY_RESULT = auto()
    BOOST_APPLY = auto()

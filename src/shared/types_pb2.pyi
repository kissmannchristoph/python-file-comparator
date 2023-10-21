from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SyncFolder(_message.Message):
    __slots__ = ["name", "targetFolder", "originFolder"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGETFOLDER_FIELD_NUMBER: _ClassVar[int]
    ORIGINFOLDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    targetFolder: str
    originFolder: str
    def __init__(self, name: _Optional[str] = ..., targetFolder: _Optional[str] = ..., originFolder: _Optional[str] = ...) -> None: ...

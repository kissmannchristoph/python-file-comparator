import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListSyncFoldersResponse(_message.Message):
    __slots__ = ["syncFolders"]
    SYNCFOLDERS_FIELD_NUMBER: _ClassVar[int]
    syncFolders: _containers.RepeatedCompositeFieldContainer[_types_pb2.SyncFolder]
    def __init__(self, syncFolders: _Optional[_Iterable[_Union[_types_pb2.SyncFolder, _Mapping]]] = ...) -> None: ...

class AddSyncFolderRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveSyncFolderRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartSyncRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

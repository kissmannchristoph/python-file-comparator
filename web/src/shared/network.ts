/* eslint-disable */
import * as _m0 from "protobufjs/minimal";
import { SyncFolder } from "./types";

export const protobufPackage = "network";

export interface ListSyncFoldersResponse {
  syncFolders: SyncFolder[];
}

export interface AddSyncFolderRequest {
}

export interface RemoveSyncFolderRequest {
}

export interface StartSyncRequest {
}

function createBaseListSyncFoldersResponse(): ListSyncFoldersResponse {
  return { syncFolders: [] };
}

export const ListSyncFoldersResponse = {
  encode(message: ListSyncFoldersResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    for (const v of message.syncFolders) {
      SyncFolder.encode(v!, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListSyncFoldersResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseListSyncFoldersResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.syncFolders.push(SyncFolder.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): ListSyncFoldersResponse {
    return {
      syncFolders: globalThis.Array.isArray(object?.syncFolders)
        ? object.syncFolders.map((e: any) => SyncFolder.fromJSON(e))
        : [],
    };
  },

  toJSON(message: ListSyncFoldersResponse): unknown {
    const obj: any = {};
    if (message.syncFolders?.length) {
      obj.syncFolders = message.syncFolders.map((e) => SyncFolder.toJSON(e));
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<ListSyncFoldersResponse>, I>>(base?: I): ListSyncFoldersResponse {
    return ListSyncFoldersResponse.fromPartial(base ?? ({} as any));
  },
  fromPartial<I extends Exact<DeepPartial<ListSyncFoldersResponse>, I>>(object: I): ListSyncFoldersResponse {
    const message = createBaseListSyncFoldersResponse();
    message.syncFolders = object.syncFolders?.map((e) => SyncFolder.fromPartial(e)) || [];
    return message;
  },
};

function createBaseAddSyncFolderRequest(): AddSyncFolderRequest {
  return {};
}

export const AddSyncFolderRequest = {
  encode(_: AddSyncFolderRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): AddSyncFolderRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseAddSyncFolderRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(_: any): AddSyncFolderRequest {
    return {};
  },

  toJSON(_: AddSyncFolderRequest): unknown {
    const obj: any = {};
    return obj;
  },

  create<I extends Exact<DeepPartial<AddSyncFolderRequest>, I>>(base?: I): AddSyncFolderRequest {
    return AddSyncFolderRequest.fromPartial(base ?? ({} as any));
  },
  fromPartial<I extends Exact<DeepPartial<AddSyncFolderRequest>, I>>(_: I): AddSyncFolderRequest {
    const message = createBaseAddSyncFolderRequest();
    return message;
  },
};

function createBaseRemoveSyncFolderRequest(): RemoveSyncFolderRequest {
  return {};
}

export const RemoveSyncFolderRequest = {
  encode(_: RemoveSyncFolderRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): RemoveSyncFolderRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseRemoveSyncFolderRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(_: any): RemoveSyncFolderRequest {
    return {};
  },

  toJSON(_: RemoveSyncFolderRequest): unknown {
    const obj: any = {};
    return obj;
  },

  create<I extends Exact<DeepPartial<RemoveSyncFolderRequest>, I>>(base?: I): RemoveSyncFolderRequest {
    return RemoveSyncFolderRequest.fromPartial(base ?? ({} as any));
  },
  fromPartial<I extends Exact<DeepPartial<RemoveSyncFolderRequest>, I>>(_: I): RemoveSyncFolderRequest {
    const message = createBaseRemoveSyncFolderRequest();
    return message;
  },
};

function createBaseStartSyncRequest(): StartSyncRequest {
  return {};
}

export const StartSyncRequest = {
  encode(_: StartSyncRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): StartSyncRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseStartSyncRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(_: any): StartSyncRequest {
    return {};
  },

  toJSON(_: StartSyncRequest): unknown {
    const obj: any = {};
    return obj;
  },

  create<I extends Exact<DeepPartial<StartSyncRequest>, I>>(base?: I): StartSyncRequest {
    return StartSyncRequest.fromPartial(base ?? ({} as any));
  },
  fromPartial<I extends Exact<DeepPartial<StartSyncRequest>, I>>(_: I): StartSyncRequest {
    const message = createBaseStartSyncRequest();
    return message;
  },
};

type Builtin = Date | Function | Uint8Array | string | number | boolean | undefined;

export type DeepPartial<T> = T extends Builtin ? T
  : T extends globalThis.Array<infer U> ? globalThis.Array<DeepPartial<U>>
  : T extends ReadonlyArray<infer U> ? ReadonlyArray<DeepPartial<U>>
  : T extends {} ? { [K in keyof T]?: DeepPartial<T[K]> }
  : Partial<T>;

type KeysOfUnion<T> = T extends T ? keyof T : never;
export type Exact<P, I extends P> = P extends Builtin ? P
  : P & { [K in keyof P]: Exact<P[K], I[K]> } & { [K in Exclude<keyof I, KeysOfUnion<P>>]: never };

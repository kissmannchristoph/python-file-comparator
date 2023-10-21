/* eslint-disable */
import * as _m0 from "protobufjs/minimal";

export const protobufPackage = "src.shared.types";

export interface SyncFolder {
  name: string;
  targetFolder: string;
  originFolder: string;
}

function createBaseSyncFolder(): SyncFolder {
  return { name: "", targetFolder: "", originFolder: "" };
}

export const SyncFolder = {
  encode(message: SyncFolder, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.name !== "") {
      writer.uint32(10).string(message.name);
    }
    if (message.targetFolder !== "") {
      writer.uint32(18).string(message.targetFolder);
    }
    if (message.originFolder !== "") {
      writer.uint32(26).string(message.originFolder);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SyncFolder {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSyncFolder();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.name = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.targetFolder = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.originFolder = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SyncFolder {
    return {
      name: isSet(object.name) ? globalThis.String(object.name) : "",
      targetFolder: isSet(object.targetFolder) ? globalThis.String(object.targetFolder) : "",
      originFolder: isSet(object.originFolder) ? globalThis.String(object.originFolder) : "",
    };
  },

  toJSON(message: SyncFolder): unknown {
    const obj: any = {};
    if (message.name !== "") {
      obj.name = message.name;
    }
    if (message.targetFolder !== "") {
      obj.targetFolder = message.targetFolder;
    }
    if (message.originFolder !== "") {
      obj.originFolder = message.originFolder;
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<SyncFolder>, I>>(base?: I): SyncFolder {
    return SyncFolder.fromPartial(base ?? ({} as any));
  },
  fromPartial<I extends Exact<DeepPartial<SyncFolder>, I>>(object: I): SyncFolder {
    const message = createBaseSyncFolder();
    message.name = object.name ?? "";
    message.targetFolder = object.targetFolder ?? "";
    message.originFolder = object.originFolder ?? "";
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

function isSet(value: any): boolean {
  return value !== null && value !== undefined;
}

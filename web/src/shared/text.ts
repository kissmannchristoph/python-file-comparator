/* eslint-disable */
import * as _m0 from "protobufjs/minimal";

export const protobufPackage = "";

export interface SearchRequest {
  query?: string | undefined;
  pageNumber: number;
  resultsPerPage: number;
}

function createBaseSearchRequest(): SearchRequest {
  return { query: undefined, pageNumber: 0, resultsPerPage: 0 };
}

export const SearchRequest = {
  encode(message: SearchRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.query !== undefined) {
      writer.uint32(10).string(message.query);
    }
    if (message.pageNumber !== 0) {
      writer.uint32(16).int32(message.pageNumber);
    }
    if (message.resultsPerPage !== 0) {
      writer.uint32(24).int32(message.resultsPerPage);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SearchRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSearchRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.query = reader.string();
          continue;
        case 2:
          if (tag !== 16) {
            break;
          }

          message.pageNumber = reader.int32();
          continue;
        case 3:
          if (tag !== 24) {
            break;
          }

          message.resultsPerPage = reader.int32();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SearchRequest {
    return {
      query: isSet(object.query) ? globalThis.String(object.query) : undefined,
      pageNumber: isSet(object.pageNumber) ? globalThis.Number(object.pageNumber) : 0,
      resultsPerPage: isSet(object.resultsPerPage) ? globalThis.Number(object.resultsPerPage) : 0,
    };
  },

  toJSON(message: SearchRequest): unknown {
    const obj: any = {};
    if (message.query !== undefined) {
      obj.query = message.query;
    }
    if (message.pageNumber !== 0) {
      obj.pageNumber = Math.round(message.pageNumber);
    }
    if (message.resultsPerPage !== 0) {
      obj.resultsPerPage = Math.round(message.resultsPerPage);
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<SearchRequest>, I>>(base?: I): SearchRequest {
    return SearchRequest.fromPartial(base ?? ({} as any));
  },
  fromPartial<I extends Exact<DeepPartial<SearchRequest>, I>>(object: I): SearchRequest {
    const message = createBaseSearchRequest();
    message.query = object.query ?? undefined;
    message.pageNumber = object.pageNumber ?? 0;
    message.resultsPerPage = object.resultsPerPage ?? 0;
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

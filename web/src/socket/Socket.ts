import { io, Socket } from 'socket.io-client';

export let client: Socket | null = null;

// eslint-disable-next-line require-jsdoc
export function connectClient(): Socket {
  console.log('a');
  client = io('ws://localhost:8080', { path: '/socket.io' });
  client.connect();
  return client;
}

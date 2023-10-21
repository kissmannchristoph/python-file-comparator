<script setup lang="ts">
import { version } from 'vuetify';

import Meta from '@/Meta';

const title = import.meta.env.VITE_APP_TITLE;

/** Props */
defineProps({
  msg: {
    type: String,
    default: 'Welcome to Vuetify.',
  },
});
</script>

<template>
  <v-container class="text-center">
    Welcome to Python Folder Sync UI
  </v-container>
</template>

<style scoped>
.logo:hover {
  will-change: filter;
  filter: drop-shadow(0 0 1em #2196f3aa);
}
</style>

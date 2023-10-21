<script setup lang="ts">
import { ref } from 'vue';

const name = ref();
const targetFolder = ref();
const originFolder = ref();

const desserts = [
  {
    name: 'Frozen Yogurt',
    calories: 159,
  },
  {
    name: 'Ice cream sandwich',
    calories: 237,
  },
  {
    name: 'Eclair',
    calories: 262,
  },
  {
    name: 'Cupcake',
    calories: 305,
  },
  {
    name: 'Gingerbread',
    calories: 356,
  },
  {
    name: 'Jelly bean',
    calories: 375,
  },
  {
    name: 'Lollipop',
    calories: 392,
  },
  {
    name: 'Honeycomb',
    calories: 408,
  },
  {
    name: 'Donut',
    calories: 452,
  },
  {
    name: 'KitKat',
    calories: 518,
  },
];
</script>
<template>
  <v-container>
    <v-card>
      <v-card-title>Add Sync Folder</v-card-title>
      <v-card-text>
        <v-text-field v-model="name" label="Name" required />
        <v-text-field v-model="targetFolder" label="Target Folder" required />
        <v-text-field v-model="originFolder" label="Origin Folder" required />
      </v-card-text>
      <v-card-actions>
        <v-btn>save</v-btn>
      </v-card-actions>
    </v-card>
    <br />
    <v-card>
      <v-card-title>Sync Folders</v-card-title>
      <v-card-text>
        <v-table>
          <thead>
            <tr>
              <th class="text-left">Name</th>
              <th class="text-center">Calories</th>
              <th class="text-right">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in desserts" :key="item.name">
              <td>{{ item.name }}</td>
              <td class="text-center">{{ item.calories }}</td>
              <td class="text-right">
                <v-btn>Sync</v-btn>
                &nbsp;
                <v-btn>Details</v-btn>
                &nbsp;
                <v-btn>Remove</v-btn>
              </td>
            </tr>
          </tbody>
        </v-table>
      </v-card-text>
    </v-card>
  </v-container>
</template>

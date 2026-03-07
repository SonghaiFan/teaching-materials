<script setup lang="ts">
import MonashDefault from './monash-default.vue'
</script>

<template>
  <MonashDefault v-bind="$attrs">
    <slot />
  </MonashDefault>
</template>

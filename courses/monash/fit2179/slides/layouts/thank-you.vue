<script setup lang="ts">
import MonashEnd from './monash-end.vue'
</script>

<template>
  <MonashEnd v-bind="$attrs">
    <slot />
  </MonashEnd>
</template>

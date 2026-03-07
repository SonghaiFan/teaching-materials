<script setup lang="ts">
import MonashCover from './monash-cover.vue'
</script>

<template>
  <MonashCover v-bind="$attrs">
    <slot />
  </MonashCover>
</template>

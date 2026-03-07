<script setup lang="ts">
import MonashVertical from './monash-vertical.vue'
</script>

<template>
  <MonashVertical v-bind="$attrs">
    <slot />
  </MonashVertical>
</template>

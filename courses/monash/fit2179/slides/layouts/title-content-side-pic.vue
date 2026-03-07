<script setup lang="ts">
import MonashSplit from './monash-split.vue'
</script>

<template>
  <MonashSplit v-bind="$attrs">
    <slot />
    <template v-if="$slots.right" #right>
      <slot name="right" />
    </template>
  </MonashSplit>
</template>

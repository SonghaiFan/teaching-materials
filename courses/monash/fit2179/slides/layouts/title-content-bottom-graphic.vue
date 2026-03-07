<script setup lang="ts">
import MonashBottomGraphic from './monash-bottom-graphic.vue'
</script>

<template>
  <MonashBottomGraphic v-bind="$attrs">
    <slot />
  </MonashBottomGraphic>
</template>

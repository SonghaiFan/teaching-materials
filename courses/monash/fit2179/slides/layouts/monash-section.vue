<script setup lang="ts">
import SectionHeader from './section-header.vue'
</script>

<template>
  <SectionHeader v-bind="$attrs">
    <slot />
  </SectionHeader>
</template>

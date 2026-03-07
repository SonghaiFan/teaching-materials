<script setup lang="ts">
import MonashDefault from './monash-default.vue'

defineProps<{
  eyebrow?: string
}>()
</script>

<template>
  <MonashDefault v-bind="$attrs">
    <div v-if="eyebrow" class="monash-eyebrow">{{ eyebrow }}</div>
    <slot />
  </MonashDefault>
</template>

<style scoped>
.monash-eyebrow {
  font-size: 0.9rem;
  color: var(--slidev-theme-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 1rem;
}
</style>

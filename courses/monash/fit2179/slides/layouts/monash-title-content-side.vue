<script setup lang="ts">
import MonashFrame from '../components/MonashFrame.vue'

defineProps<{
  eyebrow?: string
  image?: string
  imageAlt?: string
  imageFit?: 'cover' | 'contain'
}>()
</script>

<template>
  <MonashFrame
    tone="light"
    show-header-logo
    show-footer-monash
    show-page-number
  >
    <div class="monash-split">
      <div class="monash-split__content">
        <div v-if="eyebrow" class="monash-eyebrow">{{ eyebrow }}</div>
        <slot />
      </div>
      <div v-if="image" class="monash-split__image">
        <img :src="image" :alt="imageAlt || ''" :style="{ objectFit: imageFit || 'cover' }" />
      </div>
    </div>
  </MonashFrame>
</template>

<style scoped>
.monash-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  height: 100%;
  align-items: center;
}

.monash-split__content {
  padding-right: 1rem;
}

.monash-split__image {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.monash-split__image img {
  max-width: 100%;
  max-height: 100%;
  border-radius: 4px;
}

.monash-eyebrow {
  font-size: 0.9rem;
  color: var(--slidev-theme-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 1rem;
}
</style>

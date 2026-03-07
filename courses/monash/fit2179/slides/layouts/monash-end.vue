<script setup lang="ts">
import MonashFrame from '../components/MonashFrame.vue'

const props = withDefaults(defineProps<{
  speaker?: string
  contact?: string
  logoSrc?: string
}>(), {
  speaker: '',
  contact: '',
  logoSrc: '/images/pptx/image1.png',
})
</script>

<template>
  <MonashFrame
    tone="dark"
    :logo-src="props.logoSrc"
    :show-header-logo="false"
    :show-footer-monash="true"
    :show-page-number="true"
    :show-right-rail="true"
  >
    <section class="monash-end">
      <div class="monash-end__content">
        <slot />
        <p v-if="props.speaker" class="monash-end__speaker">{{ props.speaker }}</p>
        <p v-if="props.contact" class="monash-end__contact">{{ props.contact }}</p>
      </div>
    </section>
  </MonashFrame>
</template>

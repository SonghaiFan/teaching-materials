<script setup lang="ts">
import MonashFrame from '../components/MonashFrame.vue'

const props = withDefaults(defineProps<{
  eyebrow?: string
  logoSrc?: string
  footerLogoSrc?: string
  footerLogoAlt?: string
}>(), {
  eyebrow: '',
  logoSrc: '/images/pptx/image1.png',
  footerLogoSrc: '',
  footerLogoAlt: 'Partner logo',
})
</script>

<template>
  <MonashFrame
    tone="light"
    :logo-src="props.logoSrc"
    :footer-logo-src="props.footerLogoSrc"
    :footer-logo-alt="props.footerLogoAlt"
    :show-header-logo="false"
    :show-footer-monash="true"
    :show-page-number="true"
  >
    <section class="monash-page monash-page--bottom-graphic">
      <p v-if="props.eyebrow" class="monash-page__eyebrow">{{ props.eyebrow }}</p>
      <div class="monash-page__body">
        <slot />
      </div>
    </section>
  </MonashFrame>
</template>

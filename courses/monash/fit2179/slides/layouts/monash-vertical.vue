<script setup lang="ts">
import MonashFrame from '../components/MonashFrame.vue'

const props = withDefaults(defineProps<{
  eyebrow?: string
  verticalTitle?: string
  logoSrc?: string
  footerLogoSrc?: string
  footerLogoAlt?: string
}>(), {
  eyebrow: '',
  verticalTitle: '',
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
    <section class="monash-page monash-vertical">
      <p v-if="props.eyebrow" class="monash-page__eyebrow">{{ props.eyebrow }}</p>

      <div class="monash-vertical__body">
        <div class="monash-vertical__content">
          <slot />
        </div>

        <div v-if="props.verticalTitle" class="monash-vertical__title-wrap" aria-hidden="true">
          <h1 class="monash-vertical__title">{{ props.verticalTitle }}</h1>
        </div>
      </div>
    </section>
  </MonashFrame>
</template>

<script setup lang="ts">
import MonashDefault from './monash-default.vue'

const props = withDefaults(defineProps<{
  eyebrow?: string
  section?: string
  lead?: string
  logoSrc?: string
  footerLogoSrc?: string
  footerLogoAlt?: string
}>(), {
  eyebrow: '',
  section: '',
  lead: '',
  logoSrc: '/images/pptx/image1.png',
  footerLogoSrc: '',
  footerLogoAlt: 'Partner logo',
})
</script>

<template>
  <MonashDefault
    :eyebrow="props.eyebrow"
    :logo-src="props.logoSrc"
    :footer-logo-src="props.footerLogoSrc"
    :footer-logo-alt="props.footerLogoAlt"
  >
    <section class="monash-section-header">
      <h1 v-if="props.section">{{ props.section }}</h1>
      <p v-if="props.lead" class="monash-section-header__lead">{{ props.lead }}</p>
      <slot />
    </section>
  </MonashDefault>
</template>

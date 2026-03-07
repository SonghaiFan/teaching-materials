<script setup lang="ts">
import MonashFrame from '../components/MonashFrame.vue'

const props = withDefaults(defineProps<{
  eyebrow?: string
  image?: string
  imageAlt?: string
  imageFit?: 'contain' | 'cover'
  imagePosition?: 'left' | 'right'
  logoSrc?: string
  footerLogoSrc?: string
  footerLogoAlt?: string
}>(), {
  eyebrow: '',
  image: '',
  imageAlt: '',
  imageFit: 'contain',
  imagePosition: 'right',
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
    <section class="monash-page">
      <p v-if="props.eyebrow" class="monash-page__eyebrow">{{ props.eyebrow }}</p>
      <div class="monash-split" :class="`monash-split--${props.imagePosition}`">
        <div class="monash-split__content">
          <slot />
          <slot name="left" />
        </div>

        <div class="monash-split__media">
          <slot name="right">
            <div class="monash-split__media-card">
              <img
                v-if="props.image"
                class="monash-split__image"
                :class="`monash-split__image--${props.imageFit}`"
                :src="props.image"
                :alt="props.imageAlt"
              >
            </div>
          </slot>
        </div>
      </div>
    </section>
  </MonashFrame>
</template>

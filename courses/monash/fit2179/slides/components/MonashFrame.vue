<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = withDefaults(defineProps<{
  tone?: 'light' | 'dark'
  logoSrc?: string
  footerLogoSrc?: string
  footerLogoAlt?: string
  backgroundSrc?: string
  showHeaderLogo?: boolean
  showFooterMonash?: boolean
  showPageNumber?: boolean
  showRightRail?: boolean
}>(), {
  tone: 'light',
  logoSrc: '/images/pptx/image1.png',
  footerLogoSrc: '',
  footerLogoAlt: 'Partner logo',
  backgroundSrc: '',
  showHeaderLogo: false,
  showFooterMonash: true,
  showPageNumber: true,
  showRightRail: false,
})

const { $page } = useSlideContext()
const pageNumber = computed(() => `${$page.value}`)
</script>

<template>
  <div
    class="slidev-layout monash-shell"
    :class="[
      `monash-shell--${props.tone}`,
      {
        'monash-shell--rail': props.showRightRail,
        'monash-shell--header-logo': props.showHeaderLogo,
        'monash-shell--footer': props.showFooterMonash || props.footerLogoSrc || props.showPageNumber,
      },
    ]"
  >
    <img
      v-if="props.backgroundSrc"
      class="monash-shell__background"
      :src="props.backgroundSrc"
      alt=""
      aria-hidden="true"
    >

    <div v-if="props.showRightRail" class="monash-shell__rail" aria-hidden="true">
      <div class="monash-shell__pattern" />
      <div class="monash-shell__bands">
        <span class="monash-shell__band monash-shell__band--blue-top" />
        <span class="monash-shell__band monash-shell__band--violet-mid" />
        <span class="monash-shell__band monash-shell__band--blue-mid" />
        <span class="monash-shell__band monash-shell__band--violet-low" />
        <span class="monash-shell__band monash-shell__band--blue-low" />
      </div>
    </div>

    <img
      v-if="props.showHeaderLogo"
      class="monash-shell__logo"
      :src="props.logoSrc"
      alt="Monash University"
    >

    <div class="monash-shell__body">
      <slot />
    </div>

    <div
      v-if="props.showFooterMonash || props.footerLogoSrc || props.showPageNumber"
      class="monash-shell__footer"
    >
      <div class="monash-shell__footer-block monash-shell__footer-block--left">
        <img
          v-if="props.showFooterMonash"
          class="monash-shell__footer-logo"
          :src="props.logoSrc"
          alt="Monash University"
        >
      </div>

      <div class="monash-shell__footer-block monash-shell__footer-block--center">
        <img
          v-if="props.footerLogoSrc"
          class="monash-shell__partner-logo"
          :src="props.footerLogoSrc"
          :alt="props.footerLogoAlt"
        >
      </div>

      <div class="monash-shell__footer-block monash-shell__footer-block--right">
        <span v-if="props.showPageNumber" class="monash-shell__page-number">{{ pageNumber }}</span>
      </div>
    </div>
  </div>
</template>

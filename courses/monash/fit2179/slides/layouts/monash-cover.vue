<script setup lang="ts">
import MonashFrame from '../components/MonashFrame.vue'

const props = withDefaults(defineProps<{
  subtitle?: string
  date?: string
  presenter?: string
  logoSrc?: string
}>(), {
  subtitle: '',
  date: '',
  presenter: '',
  logoSrc: '/images/pptx/image1.png',
})
</script>

<template>
  <MonashFrame
    tone="dark"
    :logo-src="props.logoSrc"
    :show-header-logo="true"
    :show-footer-monash="false"
    :show-page-number="false"
    :show-right-rail="true"
  >
    <section class="monash-cover">
      <div class="monash-cover__content">
        <slot />
        <p v-if="props.subtitle" class="monash-cover__subtitle">{{ props.subtitle }}</p>
        <p v-if="props.date || props.presenter" class="monash-cover__meta">
          <span v-if="props.date">Date: {{ props.date }}</span>
          <span v-if="props.date && props.presenter" class="monash-cover__meta-sep">|</span>
          <span v-if="props.presenter">Presenter: {{ props.presenter }}</span>
        </p>
      </div>
    </section>
  </MonashFrame>
</template>

<script setup lang="ts">
import { nextTick, onMounted, ref } from 'vue'

declare global {
  interface Window {
    vegaEmbed?: (el: string | HTMLElement, spec: object, options?: object) => Promise<unknown>
  }
}

const props = defineProps({
  title: {
    type: String,
    default: 'Vega-Lite Playground',
  },
  initialSpec: {
    type: Object as () => Record<string, unknown>,
    required: true,
  },
  height: {
    type: Number,
    default: 320,
  },
})

function stringifySpec() {
  return JSON.stringify(props.initialSpec, null, 2)
}

const specText = ref(stringifySpec())
const errorText = ref('')
const previewId = `vega-preview-${Math.random().toString(36).slice(2)}`

let loaderPromise: Promise<void> | null = null

function loadScript(src: string) {
  return new Promise<void>((resolve, reject) => {
    const existing = document.querySelector(`script[data-vega-src="${src}"]`) as HTMLScriptElement | null
    if (existing) {
      if (existing.dataset.loaded === 'true') {
        resolve()
        return
      }
      existing.addEventListener('load', () => resolve(), { once: true })
      existing.addEventListener('error', () => reject(new Error(`Failed to load ${src}`)), { once: true })
      return
    }

    const script = document.createElement('script')
    script.src = src
    script.async = true
    script.dataset.vegaSrc = src
    script.addEventListener('load', () => {
      script.dataset.loaded = 'true'
      resolve()
    }, { once: true })
    script.addEventListener('error', () => reject(new Error(`Failed to load ${src}`)), { once: true })
    document.head.appendChild(script)
  })
}

async function ensureVegaRuntime() {
  if (!loaderPromise) {
    loaderPromise = (async () => {
      await loadScript('https://cdn.jsdelivr.net/npm/vega@6.2.0')
      await loadScript('https://cdn.jsdelivr.net/npm/vega-lite@6.4.1')
      await loadScript('https://cdn.jsdelivr.net/npm/vega-embed@7.1.0')
    })()
  }
  return loaderPromise
}

async function renderSpec() {
  errorText.value = ''

  try {
    await ensureVegaRuntime()
    await nextTick()

    const parsed = JSON.parse(specText.value)
    const target = document.getElementById(previewId)

    if (!target || !window.vegaEmbed)
      throw new Error('Vega runtime is not available yet.')

    target.innerHTML = ''
    await window.vegaEmbed(target, parsed, {
      // actions: false,
      renderer: 'svg',
    })
  }
  catch (error) {
    errorText.value = error instanceof Error ? error.message : 'Unknown error'
  }
}

function resetSpec() {
  specText.value = stringifySpec()
  renderSpec()
}

onMounted(() => {
  renderSpec()
})
</script>

<template>
  <div class="playground">
    <div class="header">
      <p class="eyebrow">{{ title }}</p>
      <div class="actions">
        <button type="button" class="btn" @click="renderSpec">
          Render
        </button>
        <button type="button" class="btn" @click="resetSpec">
          Reset
        </button>
      </div>
    </div>

    <div class="grid">
      <div class="panel">
        <p class="panel-title">Spec</p>
        <textarea v-model="specText" class="editor" :style="{ height: `${height}px` }" spellcheck="false" />
      </div>

      <div class="panel">
        <p class="panel-title">Preview</p>
        <div :id="previewId" class="preview" :style="{ height: `${height}px` }" />
        <div v-if="errorText" class="error">
          {{ errorText }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.playground {
  border: 1px solid rgba(15, 23, 42, 0.14);
  background: rgba(255, 255, 255, 0.7);
  padding: 0.9rem;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 0.7rem;
}

.eyebrow {
  margin: 0;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: #64748b;
}

.actions {
  display: flex;
  gap: 0.5rem;
}

.btn {
  border: 1px solid rgba(15, 23, 42, 0.16);
  background: white;
  color: #111827;
  padding: 0.28rem 0.6rem;
  font-size: 0.82rem;
  cursor: pointer;
}

.btn:hover {
  background: rgba(241, 245, 249, 0.9);
}

.grid {
  display: grid;
  grid-template-columns: 1.05fr 1fr;
  gap: 0.8rem;
  align-items: start;
}

.panel {
  min-width: 0;
}

.panel-title {
  margin: 0 0 0.35rem;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #64748b;
}

.editor {
  width: 100%;
  box-sizing: border-box;
  border: 1px solid rgba(15, 23, 42, 0.16);
  background: #f8fafc;
  padding: 0.7rem;
  font: 0.78rem/1.45 ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  resize: none;
}

.preview {
  border: 1px solid rgba(15, 23, 42, 0.16);
  background: white;
  overflow: hidden;
  padding: 0.35rem;
  box-sizing: border-box;
}

.preview :deep(.vega-embed) {
  max-width: 100%;
  max-height: 100%;
  overflow: hidden;
}

.preview :deep(svg) {
  display: block;
  max-width: 100%;
  max-height: 100%;
}

.preview :deep(.vega-bindings) {
  font-size: 0.68rem;
  line-height: 1.2;
}

.preview :deep(.vega-bind) {
  margin-bottom: 0.12rem;
}

.preview :deep(input[type="range"]) {
  width: 7rem;
  max-width: 45%;
}

.preview :deep(select) {
  max-width: 9rem;
}

.error {
  margin-top: 0.55rem;
  color: #b91c1c;
  font-size: 0.82rem;
  line-height: 1.4;
}
</style>

<script setup lang="ts">
import { computed, onBeforeUnmount, ref } from 'vue'

const props = defineProps({
  title: {
    type: String,
    default: 'Countdown Timer',
  },
  minutes: {
    type: Number,
    default: 10,
  },
})

const remainingSeconds = ref(Math.max(0, Math.round(props.minutes * 60)))
const initialSeconds = Math.max(0, Math.round(props.minutes * 60))
const isRunning = ref(false)
let intervalId: ReturnType<typeof setInterval> | null = null

function clearTimer() {
  if (intervalId) {
    clearInterval(intervalId)
    intervalId = null
  }
}

function startTimer() {
  if (isRunning.value || remainingSeconds.value <= 0)
    return
  isRunning.value = true
  intervalId = setInterval(() => {
    if (remainingSeconds.value > 0) {
      remainingSeconds.value -= 1
      return
    }
    pauseTimer()
  }, 1000)
}

function pauseTimer() {
  isRunning.value = false
  clearTimer()
}

function resetTimer() {
  pauseTimer()
  remainingSeconds.value = initialSeconds
}

const formattedTime = computed(() => {
  const minutes = Math.floor(remainingSeconds.value / 60)
  const seconds = remainingSeconds.value % 60
  return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`
})

const progress = computed(() => {
  if (initialSeconds === 0)
    return 0
  return (remainingSeconds.value / initialSeconds) * 100
})

onBeforeUnmount(() => {
  clearTimer()
})
</script>

<template>
  <div class="timer-panel">
    <p class="eyebrow">{{ title }}</p>
    <div class="time">{{ formattedTime }}</div>
    <div class="track" aria-hidden="true">
      <div class="fill" :style="{ width: `${progress}%` }" />
    </div>
    <div class="actions">
      <button type="button" class="btn" @click="startTimer">
        Start
      </button>
      <button type="button" class="btn" @click="pauseTimer">
        Pause
      </button>
      <button type="button" class="btn" @click="resetTimer">
        Reset
      </button>
    </div>
  </div>
</template>

<style scoped>
.timer-panel {
  border: 1px solid rgba(15, 23, 42, 0.14);
  background: rgba(255, 255, 255, 0.68);
  padding: 1rem;
}

.eyebrow {
  margin: 0;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: #64748b;
}

.time {
  margin-top: 0.55rem;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 2.2rem;
  font-weight: 700;
  color: #111827;
}

.track {
  margin-top: 0.9rem;
  height: 0.45rem;
  background: rgba(148, 163, 184, 0.22);
  overflow: hidden;
}

.fill {
  height: 100%;
  background: #006dae;
  transition: width 0.3s ease;
}

.actions {
  display: flex;
  gap: 0.6rem;
  margin-top: 1rem;
  flex-wrap: wrap;
}

.btn {
  border: 1px solid rgba(15, 23, 42, 0.16);
  background: white;
  color: #111827;
  padding: 0.4rem 0.75rem;
  font-size: 0.9rem;
  cursor: pointer;
}

.btn:hover {
  background: rgba(241, 245, 249, 0.9);
}
</style>

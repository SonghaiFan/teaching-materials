<script setup lang="ts">
import {
  buildPairs,
  clearAll,
  initializeNames,
  namesText,
  pairs,
  participantCount,
  showEditor,
} from './pairingStore'

const props = defineProps({
  initialNames: {
    type: Array as () => string[],
    default: () => [],
  },
})

initializeNames(props.initialNames)
</script>

<template>
  <div class="pairing-board">
    <p class="eyebrow">Random student pairing</p>

    <div class="meta">
      <span>{{ participantCount }} students</span>
    </div>

    <div class="actions">
      <button type="button" class="btn" @click="buildPairs">
        Shuffle pairs
      </button>
      <button type="button" class="btn" @click="clearAll">
        Clear
      </button>
      <button type="button" class="btn" @click="showEditor = !showEditor">
        {{ showEditor ? 'Hide names' : 'Edit names' }}
      </button>
    </div>

    <textarea
      v-if="showEditor"
      v-model="namesText"
      class="textarea"
      rows="5"
      placeholder="Paste one student name per line"
    />

    <div v-if="pairs.length" class="pairs">
      <div v-for="(pair, index) in pairs" :key="`${pair.members.join('-')}-${index}`" class="pair-card">
        <p class="pair-title">
          {{ pair.members.length === 3 ? `Group ${index + 1}` : `Pair ${index + 1}` }}
        </p>
        <p v-for="member in pair.members" :key="member" class="pair-name">
          {{ member }}
        </p>
        <p v-if="pair.members.length === 3" class="pair-wait">Three-person critique group</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pairing-board {
  border: 1px solid rgba(15, 23, 42, 0.14);
  background: rgba(255, 255, 255, 0.68);
  padding: 0.85rem;
}

.eyebrow {
  margin: 0 0 0.55rem;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: #64748b;
}

.textarea {
  width: 100%;
  border: 1px solid rgba(15, 23, 42, 0.16);
  background: white;
  padding: 0.55rem;
  font: inherit;
  resize: vertical;
  box-sizing: border-box;
  line-height: 1.35;
}

.meta {
  margin-top: 0.2rem;
  font-size: 0.8rem;
  color: #64748b;
}

.actions {
  display: flex;
  gap: 0.6rem;
  margin-top: 0.6rem;
  flex-wrap: wrap;
}

.textarea {
  margin-top: 0.7rem;
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

.pairs {
  margin-top: 0.8rem;
  display: grid;
  gap: 0.45rem;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  max-height: 13.2rem;
  overflow: auto;
  padding-right: 0.2rem;
}

.pair-card {
  border: 1px solid rgba(15, 23, 42, 0.12);
  background: rgba(248, 250, 252, 0.95);
  padding: 0.5rem;
}

.pair-title {
  margin: 0 0 0.22rem;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #64748b;
}

.pair-name {
  margin: 0.05rem 0;
  color: #111827;
  font-size: 0.8rem;
  line-height: 1.3;
}

.pair-wait {
  margin: 0.15rem 0 0;
  color: #b45309;
  font-size: 0.74rem;
}
</style>

<script setup lang="ts">
import { computed } from 'vue'
import { pairs } from './pairingStore'

const props = defineProps({
  minutesPerStudent: {
    type: Number,
    default: 2,
  },
})

const scheduledGroups = computed(() => {
  return pairs.value.map((pair, index) => ({
    index: index + 1,
    members: pair.members,
    minutes: pair.members.length * props.minutesPerStudent,
  }))
})
</script>

<template>
  <div class="timing-board">
    <p class="eyebrow">Presentation order</p>

    <div v-if="scheduledGroups.length" class="groups">
      <div v-for="group in scheduledGroups" :key="`${group.index}-${group.members.join('-')}`" class="group-card">
        <div class="group-header">
          <p class="group-title">{{ group.members.length === 3 ? `Group ${group.index}` : `Pair ${group.index}` }}</p>
          <p class="group-time">{{ group.minutes }} min</p>
        </div>
        <p v-for="member in group.members" :key="member" class="group-name">{{ member }}</p>
      </div>
    </div>

    <div v-else class="empty">
      Shuffle the pairs on the previous slide first.
    </div>
  </div>
</template>

<style scoped>
.timing-board {
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

.groups {
  display: grid;
  gap: 0.45rem;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  max-height: 15rem;
  overflow: auto;
  padding-right: 0.2rem;
}

.group-card {
  border: 1px solid rgba(15, 23, 42, 0.12);
  background: rgba(248, 250, 252, 0.95);
  padding: 0.55rem;
}

.group-header {
  display: flex;
  justify-content: space-between;
  gap: 0.6rem;
  align-items: baseline;
  margin-bottom: 0.2rem;
}

.group-title,
.group-time {
  margin: 0;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #64748b;
}

.group-name {
  margin: 0.05rem 0;
  color: #111827;
  font-size: 0.82rem;
  line-height: 1.3;
}

.empty {
  color: #64748b;
  font-size: 0.92rem;
}
</style>

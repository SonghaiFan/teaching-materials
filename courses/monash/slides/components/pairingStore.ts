import { computed, ref } from 'vue'

export type PairGroup = {
  members: string[]
}

export const namesText = ref('')
export const pairs = ref<PairGroup[]>([])
export const showEditor = ref(false)

export function initializeNames(initialNames: string[]) {
  if (!namesText.value.trim() && initialNames.length > 0)
    namesText.value = initialNames.join('\n')
}

function shuffleArray<T>(items: T[]) {
  const copy = [...items]
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[copy[i], copy[j]] = [copy[j], copy[i]]
  }
  return copy
}

export function buildPairs() {
  const names = namesText.value
    .split('\n')
    .map(name => name.trim())
    .filter(Boolean)

  const shuffled = shuffleArray(names)
  const nextPairs: PairGroup[] = []

  for (let i = 0; i < shuffled.length;) {
    const remaining = shuffled.length - i

    if (remaining === 3) {
      nextPairs.push({
        members: [shuffled[i], shuffled[i + 1], shuffled[i + 2]],
      })
      i += 3
      continue
    }

    nextPairs.push({
      members: [shuffled[i], shuffled[i + 1]].filter(Boolean),
    })
    i += 2
  }

  pairs.value = nextPairs
}

export function clearAll() {
  namesText.value = ''
  pairs.value = []
}

export const participantCount = computed(() => {
  return namesText.value
    .split('\n')
    .map(name => name.trim())
    .filter(Boolean).length
})

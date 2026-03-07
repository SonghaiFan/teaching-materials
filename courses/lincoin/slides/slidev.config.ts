import { defineConfig } from '@slidev/cli'

export default defineConfig({
  // Base path for GitHub Pages deployment
  base: '/fit5196-slides/',
  
  // Theme configuration
  theme: 'default',
  
  // Slidev features
  highlighter: 'shiki',
  
  // Export configuration
  export: {
    format: 'pdf',
    timeout: 30000,
  },
  
  // Development server
  server: {
    port: 3030,
  },
})

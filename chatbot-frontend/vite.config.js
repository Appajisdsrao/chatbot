import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Export Vite configuration with polyfills
export default defineConfig({
  plugins: [react()],
  define: {
    'process.env': {},
  },
  optimizeDeps: {
    include: ['crypto-browserify', 'stream-browserify', 'assert'],
  },
  build: {
    rollupOptions: {
      external: ['crypto', 'stream', 'assert'], // Exclude node modules
    },
  },
});

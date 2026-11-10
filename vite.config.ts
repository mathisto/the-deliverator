import { defineConfig } from 'vite';
export default defineConfig({ build: { lib: { entry: 'ui/index.ts', formats: ['es'], fileName: () => 'deliverator.js' } } });

import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig(async ({ command, mode }) => {
  return {
    build: {
      rollupOptions: {
        input: {
          main: 'ventes-par-region.html'
        },
      },
      outDir: "docs"
    }
  }
});
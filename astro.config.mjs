// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://legal.sheernox.com',
  trailingSlash: 'ignore',
  build: {
    format: 'file',
  },
  integrations: [sitemap()],
  server: {
    host: true,
    port: 4321,
  },
});

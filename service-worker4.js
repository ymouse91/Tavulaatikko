const CACHE_NAME = 'tavupeli-v1';
const FILES_TO_CACHE = [
  '/',
  '/index4.html',
  '/sallitut_sanat.txt',
  '/manifest4.json',
  '/icon-192.png',
  '/icon-512.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(FILES_TO_CACHE))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
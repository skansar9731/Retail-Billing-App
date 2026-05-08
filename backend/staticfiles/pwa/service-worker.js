const CACHE_NAME = "retail-billing-cache-v1";

const urlsToCache = [

    "/",

    "/login/",

    "/dashboard/",

    "/static/js/dashboard.js",

];


self.addEventListener("install", (event) => {

    event.waitUntil(

        caches.open(CACHE_NAME).then((cache) => {

            return cache.addAll(urlsToCache);

        })

    );

});


self.addEventListener("fetch", (event) => {

    event.respondWith(

        caches.match(event.request).then((response) => {

            return response || fetch(event.request);

        })

    );

});
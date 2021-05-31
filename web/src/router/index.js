import { createRouter, createWebHistory } from "vue-router";
import App from "../App.vue";
import NotFound from "../pages/404.vue";

const routes = [
  {
    path: "/",
    name: "App",
    component: App,
  },
  {
    path: "/:catchAll(.*)",
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

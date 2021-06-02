import { createRouter, createWebHistory } from "vue-router";
import Main from "../pages/Main.vue";
import NotFound from "../pages/404.vue";

const routes = [
  {
    path: "/",
    name: "Main",
    component: Main,
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

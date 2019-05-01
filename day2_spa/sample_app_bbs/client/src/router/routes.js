const routes = [
  {
    path: "/",
    component: () => import("layouts/MyLayout.vue"),
    children: [
      {
        path: "",
        redirect: 'bbs/entries'
      },
      {
        path: "bbs/entries",
        component: () => import("pages/bbs/Entries.vue")
      },
      {
        path: "bbs/new-entry",
        component: () => import("pages/bbs/NewEntry.vue")
      }
    ]
  }
];

// Always leave this as last one
if (process.env.MODE !== "ssr") {
  routes.push({
    path: "*",
    component: () => import("pages/Error404.vue")
  });
}

export default routes;

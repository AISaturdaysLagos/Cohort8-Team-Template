import "@/assets/main.css";

import App from "./App.vue";
import camelCase from "lodash/camelCase";
import { createApp } from "vue";
import router from "./router";
import store from "./store";
import upperFirst from "lodash/upperFirst";

import VueSweetalert from "vue-sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";

const requireComponent = require.context(
  "./components/reusable",
  true,
  /Base[A-Z]\w+\.(vue|js)$/
);

const app = createApp(App);

requireComponent.keys().forEach((fileName) => {
  const componentConfig = requireComponent(fileName);

  const componentName = upperFirst(
    camelCase(fileName.replace(/^\.\/(.*)\.\w+$/, "$1"))
  );

  app.component(componentName, componentConfig.default || componentConfig);
});

app.use(store).use(router).use(VueSweetalert).mount("#app");

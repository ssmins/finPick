import { createRouter, createWebHistory } from "vue-router";

import HomeView from "@/views/HomeView.vue";
import LoginView from "@/views/LoginView.vue";
import SignUpView from "@/views/SignUpView.vue";
import MyPageView from "@/views/MyPageView.vue";
import ArticleView from "@/views/ArticleView.vue";
import BankMapView from "@/views/BankMapView.vue";
import ExchangeView from "@/views/ExchangeView.vue";
import CompareBaseLayout from "@/components/layouts/CompareBaseLayout.vue";
import CompareDepositView from "@/views/CompareDepositView.vue";
import CompareSavingsView from "@/views/CompareSavingsView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomeView",
      component: HomeView,
    },
    {
      path: "/login",
      name: "LoginView",
      component: LoginView,
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/mypage",
      name: "MyPageView",
      component: MyPageView,
    },
    {
      path: "/articles",
      name: "ArticleView",
      component: ArticleView,
    },
    {
      path: "/bankmap",
      name: "BankMapView",
      component: BankMapView,
    },
    {
      path: "/exchange",
      name: "ExchangeView",
      component: ExchangeView,
    },
    {
      path: "/compare",
      component: CompareBaseLayout,
      children: [
        {
          path: "deposit",
          name: "CompareDepositView",
          component: CompareDepositView,
        },
        {
          path: "savings",
          name: "CompareSavingsView",
          component: CompareSavingsView,
        },
      ],
    },
  ],
});

export default router;

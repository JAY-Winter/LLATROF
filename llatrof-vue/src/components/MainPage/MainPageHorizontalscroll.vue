<template>
  <div class="container pt-4">
    <MainPageCategoryButton />
  </div>
</template>

<script>
// import MainPageCartegotyCard from '@/components/MainPage/MainPageCartegotyCard.vue'
// https://github.com/ilyashubin/scrollbooster
// import ScrollBooster from 'scrollbooster';
import MainPageCategoryButton from "@/components/MainPage/MainPageCategoryButton";

export default {
  name: "MainPageHorizontalscroll",
  components: {
    // MainPageCartegotyCard,
    MainPageCategoryButton,
  },
  data() {
    return {
      cartegory: ["데님", "코튼", "숏", "점프", "슈트", "트레이닝", "기타"],
      scrollB: null,
    };
  },
};
</script>

<style>
#horizontalScroll::-webkit-scrollbar {
  display: none;
}
</style>

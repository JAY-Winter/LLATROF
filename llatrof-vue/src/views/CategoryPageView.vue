<template>
  <div style="text-align: center; font-size: 1.5rem" class="container">
    {{ $route.params.categoryName }}
    <hr style="margin-top: 5px" />
    <div class="container">
      <div class="row">
        <MainPageGoodsCard
          v-for="good in goods.slice(0, presentPage * 14)"
          :key="good.id"
          :good="good"
        />
      </div>
      <infinite-loading @infinite="infiniteHandler"></infinite-loading>
      <div class="row d-flex justify-content-center pb-4">
        <span
          @click="morePage"
          style="font-size: 14px; border: 1px solid black; padding: 0px 10px"
          >More Item {{ presentPage }}/{{ maxPage }}</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import MainPageGoodsCard from "@/components/MainPage/MainPageGoodsCard";
import axios from "axios";
import InfiniteLoading from "vue-infinite-loading";

export default {
  name: "CategoryPageView",
  components: {
    MainPageGoodsCard,
    InfiniteLoading,
  },
  data() {
    return {
      goods: [],
      presentPage: 1,
      categoryN: this.$route.params.categoryName,
    };
  },
  computed: {
    maxPage() {
      return Math.ceil(this.goods?.length / 14);
    },
  },
  methods: {
    morePage() {
      if (this.presentPage < this.maxPage) {
        this.presentPage += 1;
      } else {
        alert("페이지 끝!");
      }
    },
    getCategory() {
      axios({
        method: "get",
        url: `https://whatyoulookingat.club/articles/category/${this.categoryN}`,
      })
        .then((res) => {
          this.goods = res.data;
        })
        .catch((err) => console.log(err));
    },
    async infiniteHandler($state) {
      if (this.presentPage !== this.maxPage) {
        await setTimeout(() => {
          this.presentPage += 1;
          $state.loaded();
        }, 1000);
      } else {
        $state.complete();
      }
    },
  },
  created() {
    this.getCategory();
  },
  watch: {
    categoryN() {
      this.presentPage = 1;
      this.getCategory();
    },
  },
  beforeRouteUpdate(to, from, next) {
    this.categoryN = to.params.categoryName;
    next();
  },
};
</script>

<style scoped></style>
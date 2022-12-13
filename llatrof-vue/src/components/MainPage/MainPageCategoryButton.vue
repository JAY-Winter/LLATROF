<template>
  <div class="row row-cols-5">
    <div class="col">
      <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '데님' } }"
        ><div id="div_size">데님</div></router-link
      >
    </div>
    <div class="col">
      <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '코튼' } }"
        ><div id="div_size">코튼</div></router-link
      >
    </div>
    <div class="col">
      <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '슈트' } }"
        ><div id="div_size">슈트</div></router-link
      >
    </div>
    <div class="col">
      <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '트레이닝' } }"
        ><div id="div_size">트레이닝</div></router-link
      >
    </div>
    <div class="col">
      <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '기타' } }"
        ><div id="div_size">기타</div></router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "MainPageCategorydiv",
  props: {
    categoryInfo: Object,
  },
};
</script>

<style>
#div_size {
  color: black;
  border-radius: 10%;
  text-align: center;
  border: 1px black solid;
  margin: 3 0 0 0;
}
</style>

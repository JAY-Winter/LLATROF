<template>
  <div class="row row-cols-3">
    <div>
      <router-link
      @click.native="closeAside"
      :to="{ name: 'category', params: { categoryName: '데님' } }"
      ><div id="inner_div">DENIM</div></router-link
      >
      </div>
      <div>
        <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '코튼' } }"
        ><div id="inner_div">COTTON</div></router-link
      >
      </div>
      <div>
        <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '슬랙스' } }"
        ><div id="inner_div">SLACKS</div></router-link
        >
        </div>
      <div>
        <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '트레이닝' } }"
        ><div id="inner_div">TRAINING</div></router-link
        >
      </div>
      <div>
        <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '쇼츠' } }"
        ><div id="inner_div">SHORTS</div></router-link
        >
      </div>
      <div>
        <router-link
        @click.native="closeAside"
        :to="{ name: 'category', params: { categoryName: '기타' } }"
        ><div id="inner_div">ETC</div></router-link
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
  #inner_div{
  color: black;
  font-size: 3rem;
  border-radius: 10%;
  text-align: center;
  border: 1px black solid;
  margin: 3 0 0 0;
}
</style>
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
        :to="{ name: 'category', params: { categoryName: '슈트' } }"
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
        :to="{ name: 'category', params: { categoryName: '숏' } }"
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
  background-color: rgba(169, 165, 165, 0.2);
  margin: 5px;
  height: 50px;
  display: flex;
  align-items: center;
  border-radius: 5px;
  justify-content: center;
  font-size: 1.1rem;
  }
  </style>
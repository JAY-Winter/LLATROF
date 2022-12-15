<template>
    <div>
      <MainPageCarousel />
      <MainPageHorizontalscroll />
       <div style="font-size: 1.5rem;" class="container">
          <h4 class="pb-1 pt-4">LLATROF's PICK</h4>
          <div class="container" style="text-align: center;">
              <div class="row">
                  <MainPageGoodsCard 
                      v-for="good in liamspick"
                      :key="good.id"
                      :good=good.goods
                  />
              </div>
          </div>
      </div>
    </div>
  </template>
  
  <script>
  import MainPageCarousel from '@/components/MainPage/MainPageCarousel'
  import MainPageHorizontalscroll from '@/components/MainPage/MainPageHorizontalscroll'
  import MainPageGoodsCard from '@/components/MainPage/MainPageGoodsCard'
  import axios from 'axios'
  
  export default {
      name: 'MainPageView',
      components: {
          MainPageCarousel,
          MainPageHorizontalscroll,
          MainPageGoodsCard,
      },
      data() {
          return {
              cartegory: this.$store.state.cartegory,
              liamspick: []
          }
      },
      computed: {
          goods() {
              return this.$store.state.articles
          }
      },
      methods: {
          getLiamsPick() {
              axios({
              method: 'get',
              url: `https://whatyoulookingat.club/articles/liamspick`
              })
              .then(res => {
                  this.liamspick = res.data
              })
              .catch(err => console.log(err))
          }
      },
      created() {
          this.getLiamsPick()
      },
  }
  </script>
  
  <style>
  </style>
<template>
  <div>
    <MainPageCarousel />
    <MainPageHorizontalscroll />
    <MainPageGoodsCard 
        v-for="good in goods"
        :key = good.id
        :good = good
    />
  </div>
</template>

<script>
import MainPageCarousel from '@/components/MainPage/MainPageCarousel'
import MainPageHorizontalscroll from '@/components/MainPage/MainPageHorizontalscroll'
import MainPageGoodsCard from '@/components/MainPage/MainPageGoodsCard'

export default {
    name: 'MainPageView',
    components: {
        MainPageCarousel,
        MainPageHorizontalscroll,
        MainPageGoodsCard,
    },
    data() {
        return {
            cartegory: this.$store.state.cartegory
        }
    },
    computed: {
        goods() {
            return this.$store.state.articles
        }
    }
}
</script>

<style>
</style>
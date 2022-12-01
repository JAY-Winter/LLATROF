<template>
  <div>
    <MainPageCarousel />
    <MainPageHorizontalscroll />
  </div>
</template>

<script>
import MainPageCarousel from '@/components/MainPage/MainPageCarousel'
import MainPageHorizontalscroll from '@/components/MainPage/MainPageHorizontalscroll'

export default {
    name: 'MainPageView',
    components: {
        MainPageCarousel,
        MainPageHorizontalscroll,
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
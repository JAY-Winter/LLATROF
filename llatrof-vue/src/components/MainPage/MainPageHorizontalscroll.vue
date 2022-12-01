<template>
  <div class="container d-flex overflow-hidden" ref="viewport">
    <div class="row d-flex flex-nowrap " id="horizontalScroll" ref="content">
        <!-- <MainPageCartegotyCard 
            v-for="sub in cartegory"
            :key="sub.title"
            :cartegoryInfo = sub
            class="m-2"
        /> -->
        <MainPageCategoryButton />
    </div>
  </div>
</template>

<script>
// import MainPageCartegotyCard from '@/components/MainPage/MainPageCartegotyCard.vue'
// https://github.com/ilyashubin/scrollbooster
import ScrollBooster from 'scrollbooster';
import MainPageCategoryButton from '@/components/MainPage/MainPageCategoryButton'

export default {
    name: 'MainPageHorizontalscroll',
    components: {
        // MainPageCartegotyCard,
        MainPageCategoryButton
    },
    data() {
        return {
            cartegory: ['데님', '코튼', '숏', '점프', '슈트', '트레이닝', '기타'],
            scrollB: null,
        }
    },
    computed: {
    },
    methods: {
        // 스크롤 부스터
        sb() {
            // refs를 통해서 html요소 정보를 불러올 수 있습니다.
            const viewport = this.$refs.viewport
            const content = this.$refs.content
            new ScrollBooster({
                viewport,
                content,
                direction: "horizontal",
                scrollMode: "transform"
            })
        }
    },
    mounted() {
        // 마운트 될 때 스크롤 함수 동작하게 설정
        this.sb()
    }
}
</script>

<style>
    #horizontalScroll::-webkit-scrollbar {
        display: none;
    }
</style>
<template>
    <div style="text-align: center; font-size: 1.5rem;" class="container">
        {{ $route.params.brandName }}
        <hr style="margin-top: 5px">
        <div class="container">
            <div class="row">
                <MainPageGoodsCard 
                    v-for="good in goods.slice(0, presentPage * 14)"
                    :key="good.id"
                    :good=good
                />
            </div>
            <div class="row d-flex justify-content-center pb-4">
                <span @click="morePage" style=" font-size: 14px; border: 1px solid black; padding: 0px 10px;">More Item {{ presentPage }}/{{ maxPage }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import MainPageGoodsCard from '@/components/MainPage/MainPageGoodsCard'
import axios from 'axios'

export default {
    name: 'BrandPageView',
    components: {
        MainPageGoodsCard
    },
    data() {
        return {
            goods: [],
            presentPage: 1,
            brandN: this.$route.params.brandName
        }
    },
    computed: {
        maxPage() {
            return Math.ceil(this.goods?.length / 14)
        }
    },
    methods: {
        morePage() {
            if (this.presentPage < this.maxPage) {
                this.presentPage += 1
            }
            else {
                alert('페이지 끝!')
            }
        },
        getCategory() {
            axios({
            method: 'get',
            url: `https://whatyoulookingat.club/articles/brand/${this.brandN}`
            })
            .then(res => {
                this.goods = res.data
            })
            .catch(err => console.log(err))
        }
    },
    created() {
        this.getCategory()
    },
    watch: {
      brandN () {
        this.presentPage = 1
        this.getCategory()
      }
    },
    beforeRouteUpdate(to, from, next) {
      console.log(to.params.brandName)
      this.brandN = to.params.brandName
      next()
    }
}
</script>

<style scoped>

</style>
<template>
  <!-- <div class="card border-0" style="width: 200px;">
    <img :src="cartegoryInfo.imgUrl" class="card-img-top mt-2" alt="테스트" style="height: 100%; width: 100%;">
    <div class="card-body">
      <h5 class="card-title">{{ cartegoryInfo.title }}</h5>
    </div>
  </div> -->
  <div>
    <b-card
      style="width: 20rem;"
      class="mb-2"
    >
      <b-card-img 
      :src="cartegoryInfo.imgUrl" 
      height = 300rem
      width = 100%
      style="object-fit: cover;"
      tag="article" />
      <b-card-title>
        {{ cartegoryInfo.title }}
      </b-card-title>
    </b-card>
</div>
</template>


<script>
export default {
    name: 'MainPageCard',
    props: {
        cartegoryInfo: Object,
    }
}
</script>

<style>

</style>
<template>
  <!-- <div class="card border-0" style="width: 200px;">
    <img :src="cartegoryInfo.imgUrl" class="card-img-top mt-2" alt="테스트" style="height: 100%; width: 100%;">
    <div class="card-body">
      <h5 class="card-title">{{ cartegoryInfo.title }}</h5>
    </div>
  </div> -->
  <!-- <div>
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
</div> -->
<div id="card">
  <router-link @click.native="closeAside" :to="{ name: 'category', params: {categoryName: cartegoryInfo.categoryName} }">
  <div class="card-img">
    <img :src="cartegoryInfo.imgUrl" :alt="cartegoryInfo.title" class="img-in-card">
  </div>
  <div class="p-2">
    <p><small>{{ cartegoryInfo.title }}</small></p>
    <!-- ㄴ 장고로 브랜드 이름 받아서 써야함 -->
    <h4><strong>{{ cartegoryInfo.title }}</strong></h4>
    <!-- <h4>여기는 가격 써야하는 자리</h4> -->
    <h5>100,000 won</h5>
  </div></router-link>
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
#card {
  width: 300px;
}

.card-img {
  width: 100%;
  height: 400px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.img-in-card {
  object-fit: cover;
  width: 100%;
}
</style>
<template>
  <div id="card" class="col-6">
    
      <a :href="good.goods_url" target="_blank"><img :src="good.goods_img_url" :alt="good.title" class="img-in-card"></a>
    
    <div class="p-2">
      <!-- 주석 처리한 바로 밑에 거랑 router-link 중에 하나 골라서 쓰면 될듯... 브랜드 누르면 브랜드로 넘어가는 게 맞는 거 같긴 한데 싶어서 생각중 -->
      <!-- <p><small>{{ good.goods_brand }}</small></p> -->
      <router-link :to="{ name: 'brand', params: { brandName: good.goods_brand } }" class="router-brand"><p><small>{{ good.goods_brand }}</small></p></router-link>
      <a :href="good.goods_url" target="_blank" class="router-brand"><strong>{{ good.goods_title }}</strong></a>
      <p>{{ good.goods_price }}원</p>
    </div>
  </div>
</template>

<script>
export default {
    name: 'MainPageGoodsCard',
    props: {
        good: Object,
    }
}
</script>


<style scoped>
#card {
  width: 300px;
  color: black;
  text-align: initial;
  font-size: 17px;
  padding: 0;
}

.card-img {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.img-in-card {
  object-fit: cover;
  width: 100%;
  height: 200px;
}

.router-brand {
  text-decoration-line: none;
  color: black;
}

.router-brand:hover {
  text-decoration-line: none;
  color: black;
}
</style>
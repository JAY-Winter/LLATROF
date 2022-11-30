<template>
  <div>
    <b-card
      style="width: 20rem;"
      class="mb-2"
    >
      <b-card-img 
      :src="Good?.goods_img_url" 
      height = 300rem
      width = 100%
      style="object-fit: cover;"
      tag="article" />
      <b-card-title>
        {{ Good?.goods_brand }}
      </b-card-title>
      <b-card-body>
        {{ Good?.goods_url}}
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
export default {
    name: 'MainPageGoodsCard',
    props: {
        Good: Object,
    }
}
</script>

<style>

</style>
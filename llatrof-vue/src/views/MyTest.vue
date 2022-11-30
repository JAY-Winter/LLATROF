-<template>
  <div>
    <!-- bootstrap vue 형식 -->
    <!-- style 임의 지정, 이미지 src에는 한 상품의 여러 이미지 중 제일 앞에 있는 것 수정필요 -->
    <img v-b-modal.modal-scrollable style="width: 200px;" src="https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20201124_244%2F1606197919745TUI2N_PNG%2F9a077c9a40a95078b912f155eb00e1a1.jpg&type=sc960_832">

    <b-modal id="modal-scrollable" scrollable title="Scrollable Content">
      <p class="my-4" v-for="i in 20" :key="i">
        상품 이미지들, 상세정보, 링크 넣는 공간
      </p>
    </b-modal>
  </div>
</template>

<script>

export default {
    name: 'MyTest',
}
</script>

<style>

</style>
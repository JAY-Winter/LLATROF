<template>
  <div>
    <!-- <div class="dropdown" id="dropdown-dropup">
      <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        Dropdown button
      </button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Another action</a></li>
        <li><a class="dropdown-item" href="#">Something else here</a></li>
      </ul>
    </div> -->

    <b-dropdown id="dropdown-dropup" dropup text="MENU" variant="outline-dark" class="m-1" :class="{ 'navbar--hidden': !showNavbar }">
      <b-dropdown-item href="#">Action</b-dropdown-item>
      <b-dropdown-item href="#">Another action</b-dropdown-item>
      <b-dropdown-item href="#">Something else here</b-dropdown-item>
      <b-dropdown-item href="#">Another action</b-dropdown-item>
      <b-dropdown-item href="#">Something else here</b-dropdown-item>
    </b-dropdown>
    <!-- onScorll함수는 어디에...? -->
    <svg id="svg" xmlns="http://www.w3.org/2000/svg" width="25" height="26" fill="currentColor" class="bi bi-chevron-up mb-3" viewBox="0 0 16 16" @click="scrollToTop">
      <path fill-rule="evenodd" d="M7.646 4.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 5.707l-5.646 5.647a.5.5 0 0 1-.708-.708l6-6z"/>
    </svg>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      showNavbar: null
    }
  },
  props: {
    msg: String
  },
  
  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
      })
    }
  },
}

</script>

<!-- 스코프를 사용하면 전역이 아니라 현재vue만 적용 -->
<style scoped>

svg {
  position:fixed;
  right: 1rem;
  bottom:1px;
  background-color: white;
  border-radius: 100%;
  transition:top 0.3s;
}
#dropdown-dropup {
  position:fixed;
  left:2px;
  bottom:1px;
  display:block;
  transition:top 0.3s;
}

</style>
<template>
  <div id="app" ref="app">
    <OpeningAnimation v-if="animationPlay"/>
    <!-- 최상단에 고정하기 위해서 fixed-top -->
    <NavBar class="fixed-top"/>
    <router-view style="margin-top: 60px" />
    <Footer/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar/NavBar.vue'
import Footer from '@/components/Footer/Footer.vue'
import OpeningAnimation from '@/components/Open/OpeningAnimation'

export default ({
  name: 'App',
  data() {
    return {
      animationPlay: true
    }
  },
  components: {
    NavBar,
    Footer,
    OpeningAnimation,
  },
})
// 네브바와 푸터 두군데서 코드 중복이 이루어져서
// 간섭이 있었기에 두군데의 공통된 부모인 app에 통합
// 스크롤링은 최상단에서 이루어지도록 만들었음
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        // document.getElementById("navbar").style.top = "0";
        // document.getElementById("dropdown-dropup").style.bottom = "0";
        document.getElementById("svg").style.bottom = "0";
    } else {
        // document.getElementById("navbar").style.top = "-100px";
        // document.getElementById("dropdown-dropup").style.bottom = "-100px";
        document.getElementById("svg").style.bottom = "-100px";
    }
    prevScrollpos = currentScrollPos;
}
</script>

<!-- 스코프를 사용하면 전역이 아니라 현재vue만 적용 -->
<style>
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* 스크롤바 숨김 */
body::-webkit-scrollbar{
  display: none;
}
</style>

<template>
  <div>
    <div id="mySidenav" class="sidenav" ref="mySidenav">
      <a href="javascript:void(0)" class="closebtn" @click="closeAside">
        &times;
      </a>
      <a><b>CATEGORY</b></a>
      <br />
      <div style="">
        <router-link
          @click.native="closeAside"
          :to="{ name: 'category', params: { categoryName: '데님' } }"
          >데님</router-link
        >
        <router-link
          @click.native="closeAside"
          :to="{ name: 'category', params: { categoryName: '코튼' } }"
          >코튼</router-link
        >
        <router-link
          @click.native="closeAside"
          :to="{ name: 'category', params: { categoryName: '슈트' } }"
          >슬랙스</router-link
        >
        <router-link
          @click.native="closeAside"
          :to="{ name: 'category', params: { categoryName: '트레이닝' } }"
          >트레이닝</router-link
        >
        <router-link
          @click.native="closeAside"
          :to="{ name: 'category', params: { categoryName: '기타' } }"
          >기타</router-link
        >
      </div>
      <br />
      <a><b>BRAND</b></a>
      <br />
      <div >
        <div class="brand-nav">
          <p>황</p>
          <p>규</p>
          <p>형</p>
          <p>이</p>
          <p>만</p>
          <p>드</p>
          <p>는</p>
          <p>제</p>
          <p>품</p>
          <p>페</p>
          <p>이</p>
          <p>지</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
          <p>데님</p>
        </div>
      </div>
    </div>
    <!-- 오버레이 -->
    <div class="overlay" v-show="btnClicked" @click="closeAside"></div>
    <!-- 아이콘 -->
    <a href="#" @click.prevent>
      <i
        class="bi bi-list"
        style="font-size: 1.5rem; color: white"
        id="sideMain"
        ref="sideMain"
        @click="openAside"
      ></i
    ></a>
    <!-- <button class="btn btn-dark" id="sideMain" ref="sideMain" @click="openAside" >
Menu
</button> -->
  </div>
</template>

<script>
export default {
  name: "NavBarAside",
  data() {
    return {
      btnClicked: false,
    };
  },
  methods: {
    openAside() {
      this.btnClicked = true;
      this.$refs.mySidenav.style.width = "250px";
      document.documentElement.style.overflow = 'hidden'
      // this.$refs.sideMain.style.marginLeft = '250px'
    },

    closeAside() {
      this.btnClicked = false;
      this.$refs.mySidenav.style.width = "0";
      document.documentElement.style.overflow = ''
      // this.$refs.sideMain.style.marginLeft = '0'
    },
  },
};
</script>

<style>
.sidenav {
  height: 100%;
  width: 0;
  position: fixed;
  display: flex;
  flex-direction: column;
  align-items: start;
  z-index: 99;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
}

.sidenav a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  color: #818181;
  display: flex;
  transition: 0.3s;
  z-index: 1;
}

.sidenav a:hover {
  color: #f1f1f1;
}

.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

#sideMain {
  transition: margin-left 0.5s;

  z-index: -1;
}

@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
  .sidenav a {
    font-size: 18px;
  }
}

.overlay {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
}
.overlay {
  opacity: 0.5;
  background-color: black;
}
.brand-nav {
  display: flex;
  flex-direction: column;
  align-items: start;
  height: 50vh;
  width: 250px;
  flex-wrap: nowrap;
  overflow: auto;
  color: white;
  padding-left: 35px;
  background-color: #111;
}
.brand-nav::-webkit-scrollbar {
  display: block;
  width: 0.5em;
  overflow: auto;
  height: 2em;
  background-color: #111;
}
.brand-nav::-webkit-scrollbar-thumb {
  background: #aaa;
  border-radius: 10px;
}
</style>

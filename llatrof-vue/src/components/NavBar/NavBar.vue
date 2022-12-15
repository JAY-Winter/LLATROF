<template>
    <nav id="navbar" class="navbar navbar-default" role="navigation">
        <div id="navbar_left" class="nav navbar-nav navbar-left">
            <NavBarAside/>
        </div>
        <router-link :to="{ name: 'mainpage' }" class="navbar-brnad">LLATROF</router-link>
        <div id="navbar_right" class="nav navbar-nav navbar-right">
        <li><a href='#' @click.prevent><i class="bi bi-search" style="font-size: 1.2rem; color: black;"></i></a></li>
        </div>
    </nav>
</template>

<script>
import NavBarAside from '@/components/NavBar/NavBarAside.vue'
export default {
    name: 'NavBar',
    components: {
        NavBarAside,
    },
}

// 아래로 스크롤시 숨기기

</script>

<style>

#navbar {
  background-color: black; 
  position: fixed; 
  display: flex;
  top: 0; 
  width: 100%;
  height: 50px; 
  transition: top 0.3s; /* Transition effect when sliding down (and up) */
}

#navbar a {
  float: left;
  display: block;
  color: white;
  text-align: center;
  /* padding: 15px; */
  text-decoration: none;
}

.navbar-brnad {
  font-size: 1.4rem;
}

/* #navbar a:hover {
  background-color: #ddd;
  color: black;
} */

.navbar {
    background-color: lightgray;
}

#navbar_left {
}

#navbar_right {
    
}

.navbar-brand {
    position: absolute;
    width: 100%;
    /* left: 25%; */
    text-align: center;
    margin:0 auto;
}
.navbar-toggle {
    z-index:3;
}

</style>
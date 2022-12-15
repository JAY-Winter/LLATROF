<template>
  <div class="logo">
    <div class="logoin">
      <div id="F1">F</div>
      <div id="O1">O</div>
      <div id="R1">R</div>
      <div id="T1">T</div>
      <div id="A1">A</div>
      <div id="L1">L</div>
      <div id="L2">L</div>
    </div>
    <!-- <div class="logoin">
      <div style="margin: 5px">L</div>
      <div style="margin: 5px">L</div>
      <div style="margin: 5px">A</div>
      <div style="margin: 5px">T</div>
      <div style="margin: 5px">R</div>
      <div style="margin: 5px">O</div>
      <div style="margin: 5px">F</div>
    </div> -->
  </div>
</template>

<script>
export default {
  name: "OpeningAnimation",
  methods: {},
};
</script>

<style scoped>
.logo {
  position: fixed;
  top: 0;
  font-family: "Helvetica", serif;
  color: white;
  background-color: black;
  display: flex;
  flex-direction: column;
  font-size: 3rem;
  height: 100vh;
  width: 100vw;
  align-items: center;
  justify-content: center;
  animation: uppp 0.5s;
  animation-delay: 4s;
  animation-fill-mode: forwards;
  -webkit-animation: uppp 0.5s;
  -webkit-animation-delay: 4s;
  -webkit-animation-fill-mode: forwards;
  z-index: 2000;
}
@keyframes uppp {
  100% {
    transform: translateY(-100vh);
    visibility: hidden;
    -webkit-transform: translateY(-100vh);
    -webkit-visibility: hidden;
  }
}
.logoin {
  display: flex;
  flex-direction: row;
}
#F1 {
  animation: f1 4s;
  animation-fill-mode: forwards;
  margin-right: 10px;
  -webkit-animation: f1 4s;
  -webkit-animation-fill-mode: forwards;
  -webkit-margin-right: 10px;
}
@-webkit-keyframes f1 {
  0% {
    -webkit-scale: 0;
  }
  10% {
    -webkit-scale: 1;
  }
  30% {
    -webkit-scale: 1;
    -webkit-transform: translate(0, 0);
  }
  60% {
    -webkit-transform: translate(50vw, 30vh) rotate(540deg);
  }
  80% {
    -webkit-transform: translateX(15.6rem);
  }
  100% {
    -webkit-transform: translateX(15.6rem);
  }
}
@keyframes f1 {
  0% {
    scale: 0;
  }
  10% {
    scale: 1;
  }
  30% {
    scale: 1;
    transform: translate(0, 0);
  }
  60% {
    transform: translate(50vw, 30vh) rotate(540deg);
  }
  80% {
    transform: translateX(15.6rem);
  }
  100% {
    transform: translateX(15.6rem);
  }
}
#O1 {
  animation: o1 4s;
  animation-fill-mode: forwards;
  margin-right: 10px;
  -webkit-animation: o1 4s;
  -webkit-animation-fill-mode: forwards;
  -webkit-margin-right: 10px;
}
@-webkit-keyframes o1 {
  0% {
    -webkit-scale: 0;
  }
  10% {
    -webkit-scale: 1;
  }
  30% {
    -webkit-scale: 1;
    -webkit-transform: translate(0, 0);
  }
  60% {
    -webkit-transform: translate(-10vw, -40vh) rotate(-600deg);
  }
  80% {
    -webkit-transform: translateX(10.5rem);
  }
  100% {
    -webkit-transform: translateX(10.5rem);
  }
}
@keyframes o1 {
  0% {
    scale: 0;
  }
  10% {
    scale: 1;
  }
  30% {
    scale: 1;
    transform: translate(0, 0);
  }
  60% {
    transform: translate(-10vw, -40vh) rotate(-600deg);
  }
  80% {
    transform: translateX(10.5rem);
  }
  100% {
    transform: translateX(10.5rem);
  }
}
#R1 {
  animation: r1 4s;
  animation-fill-mode: forwards;
  margin-right: 30px;
  -webkit-animation: r1 4s;
  -webkit-animation-fill-mode: forwards;
  -webkit-margin-right: 30px;
}
@-webkit-keyframes r1 {
  0% {
    -webkit-scale: 0;
  }
  10% {
    -webkit-scale: 1;
  }
  30% {
    -webkit-scale: 1;
    -webkit-transform: translate(0, 0);
  }
  60% {
    -webkit-transform: translate(10vw, -30vh) rotate(450deg);
  }
  80% {
    -webkit-transform: translateX(5.2rem);
  }
  100% {
    -webkit-transform: translateX(5.2rem);
  }
}
@keyframes r1 {
  0% {
    scale: 0;
  }
  10% {
    scale: 1;
  }
  30% {
    scale: 1;
    transform: translate(0, 0);
  }
  60% {
    transform: translate(10vw, -30vh) rotate(450deg);
  }
  80% {
    transform: translateX(5.2rem);
  }
  100% {
    transform: translateX(5.2rem);
  }
}
#T1 {
  animation: t1 4s;
  animation-fill-mode: forwards;
  margin-right: 10px;
  -webkit-animation: t1 4s;
  -webkit-animation-fill-mode: forwards;
  -webkit-margin-right: 10px;
}
@-webkit-keyframes t1 {
  0% {
    -webkit-scale: 0;
  }
  10% {
    -webkit-scale: 1;
  }
  30% {
    -webkit-scale: 1;
    -webkit-transform: translate(0, 0);
  }
  60% {
    -webkit-transform: translate(-10vw, 40vh) rotate(-530deg);
  }
  80% {
    -webkit-transform: translateX(-1.2rem);
  }
  100% {
    -webkit-transform: translateX(-1.2rem);
  }
}
@keyframes t1 {
  0% {
    scale: 0;
  }
  10% {
    scale: 1;
  }
  30% {
    scale: 1;
    transform: translate(0, 0);
  }
  60% {
    transform: translate(-10vw, 40vh) rotate(-530deg);
  }
  80% {
    transform: translateX(-1.2rem);
  }
  100% {
    transform: translateX(-1.2rem);
  }
}
#A1 {
  animation: a1 4s;
  animation-fill-mode: forwards;
  margin-right: 10px;
  -webkit-animation: a1 4s;
  -webkit-animation-fill-mode: forwards;
  -webkit-margin-right: 10px;
}
@-webkit-keyframes a1 {
  0% {
    -webkit-scale: 0;
  }
  10% {
    -webkit-scale: 1;
  }
  30% {
    -webkit-scale: 1;
    -webkit-transform: translate(0, 0);
  }
  60% {
    -webkit-transform: translate(-20vw, -10vh) rotate(-480deg);
  }
  80% {
    -webkit-transform: translateX(-6.3rem);
  }
  100% {
    -webkit-transform: translateX(-6.3rem);
  }
}
@keyframes a1 {
  0% {
    scale: 0;
  }
  10% {
    scale: 1;
  }
  30% {
    scale: 1;
    transform: translate(0, 0);
  }
  60% {
    transform: translate(-20vw, -10vh) rotate(-480deg);
  }
  80% {
    transform: translateX(-6.3rem);
  }
  100% {
    transform: translateX(-6.3rem);
  }
}
#L1 {
  animation: l1 4s;
  animation-fill-mode: forwards;
  margin-right: 10px;
  -webkit-animation: l1 4s;
  -webkit-animation-fill-mode: forwards;
  -webkit-margin-right: 10px;
}
@-webkit-keyframes l1 {
  0% {
    -webkit-scale: 0;
  }
  10% {
    -webkit-scale: 1;
  }
  30% {
    -webkit-scale: 1;
    -webkit-transform: translate(0, 0);
  }
  60% {
    -webkit-transform: translate(-50vw, 20vh) rotate(-610deg);
  }
  80% {
    -webkit-transform: translateX(-11.4rem);
  }
  100% {
    -webkit-transform: translateX(-11.4rem);
  }
}
@keyframes l1 {
  0% {
    scale: 0;
  }
  10% {
    scale: 1;
  }
  30% {
    scale: 1;
    transform: translate(0, 0);
  }
  60% {
    transform: translate(-50vw, 20vh) rotate(-610deg);
  }
  80% {
    transform: translateX(-11.4rem);
  }
  100% {
    transform: translateX(-11.4rem);
  }
}
#L2 {
  animation: l2 4s;
  animation-fill-mode: forwards;
  margin-right: 10px;
  -webkit-animation: l2 4s;
  -webkit-animation-fill-mode: forwards;
  -webkit-margin-right: 10px;
}
@-webkit-keyframes l2 {
  0% {
    -webkit-scale: 0;
  }
  10% {
    -webkit-scale: 1;
  }
  30% {
    -webkit-scale: 1;
    -webkit-transform: translate(0, 0);
  }
  60% {
    -webkit-transform: translate(-10vw, -30vh) rotate(492deg);
  }
  80% {
    -webkit-transform: translateX(-15.9rem);
  }
  100% {
    -webkit-transform: translateX(-15.9rem);
  }
}
@keyframes l2 {
  0% {
    scale: 0;
  }
  10% {
    scale: 1;
  }
  30% {
    scale: 1;
    transform: translate(0, 0);
  }
  60% {
    transform: translate(-10vw, -30vh) rotate(492deg);
  }
  80% {
    transform: translateX(-15.9rem);
  }
  100% {
    transform: translateX(-15.9rem);
  }
}
</style>

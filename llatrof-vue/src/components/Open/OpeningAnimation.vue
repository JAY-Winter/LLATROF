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
    </div>
</template>

<script>
export default {
    name: 'OpeningAnimation',
    methods: {

    }
}
</script>

<style scoped>
    .logo {
        position: fixed;
        top: 0;
        font-family: 'Hahmlet', serif;
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
        z-index: 2000;
    }
    @keyframes uppp {
        to {
            transform: translateY(-100vh);
            visibility: hidden;
        }
    }
    .logoin {
        display: flex;
        flex-direction: row;
    }
    #F1 {
        animation: f1 4S;
        animation-fill-mode: forwards;
        margin-right: 10px;
    }
    @keyframes f1 {
        from {
            scale: 0;
        }
        10% {
            scale: 1;
        }
        30% {
            scale: 1;
            transform: translate(0, 0);
        }
        60%{
            transform: translate(50vw, 30vh) rotate(540deg);
        }
        80% {
            transform: translateX(17.5rem);
        }
        to {
            transform: translateX(17.5rem);
        }
    }
    #O1 {
        animation: o1 4S;
        animation-fill-mode: forwards;
        margin-right: 10px;
    }
    @keyframes o1 {
        from {
            scale: 0;
        }
        10% {
            scale: 1;
        }
        30% {
            scale: 1;
            transform: translate(0, 0);
        }
        60%{
            transform: translate(-10vw, -40vh) rotate(-600deg);
        }
        80% {
            transform: translateX(11.8rem);
        }
        to {
            transform: translateX(11.8rem);
        }
    }
    #R1 {
        animation: r1 4S;
        animation-fill-mode: forwards;
        margin-right: 30px
    }
    @keyframes r1 {
        from {
            scale: 0;
        }
        10% {
            scale: 1;
        }
        30% {
            scale: 1;
            transform: translate(0, 0);
        }
        60%{
            transform: translate(10vw, -30vh) rotate(450deg);
        }
        80% {
            transform: translateX(5.7rem);
        }
        to {
            transform: translateX(5.7rem);
        }
    }
    #T1 {
        animation: t1 4S;
        animation-fill-mode: forwards;
        margin-right: 10px;
    }
    @keyframes t1 {
        from {
            scale: 0;
        }
        10% {
            scale: 1;
        }
        30% {
            scale: 1;
            transform: translate(0, 0);
        }
        60%{
            transform: translate(-10vw, 40vh) rotate(-530deg);
        }
        80% {
            transform: translateX(-1.8rem);
        }
        to {
            transform: translateX(-1.8rem);
        }
    }
    #A1 {
        animation: a1 4S;
        animation-fill-mode: forwards;
        margin-right: 10px;
    }
    @keyframes a1 {
        from {
            scale: 0;
        }
        10% {
            scale: 1;
        }
        30% {
            scale: 1;
            transform: translate(0, 0);
        }
        60%{
            transform: translate(-20vw, -10vh) rotate(-480deg);;
        }
        80% {
            transform: translateX(-7.2rem);
        }
        to {
            transform: translateX(-7.2rem);
        }
    }
    #L1 {
        animation: l1 4S;
        animation-fill-mode: forwards;
        margin-right: 10px;
    }
    @keyframes l1 {
        from {
            scale: 0;
        }
        10% {
            scale: 1;
        }
        30% {
            scale: 1;
            transform: translate(0, 0);
        }
        60%{
            transform: translate(-50vw, 20vh) rotate(-610deg);;
        }
        80% {
            transform: translateX(-12.5rem);
        }
        to {
            transform: translateX(-12.5rem);
        }
    }
    #L2 {
        animation: l2 4S;
        animation-fill-mode: forwards;
        margin-right: 10px;
    }
    @keyframes l2 {
        from {
            scale: 0;
        }
        10% {
            scale: 1;
        }
        30% {
            scale: 1;
            transform: translate(0, 0);
        }
        60%{
            transform: translate(-10vw, -30vh) rotate(492deg);;
        }
        80% {
            transform: translateX(-17.2rem);
        }
        to {
            transform: translateX(-17.2rem);
        }
    }
</style>
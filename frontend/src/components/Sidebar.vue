<template>
    <div class="sidebar">
        <img id="keller" src="@/assets/kellerwill.png" alt="">
        <i id="sink" class="fas fa-sink fa-3x"></i>
        <i id="house" class="fas fa-home fa-3x"></i>
        <i id="key" class="fas fa-key fa-3x"></i>
        <i id="door" class="fas fa-door-closed fa-3x"></i>
        <i id="bighouse" class="fas fa-home fa-5x"></i>
        <i id="bigkey" class="fas fa-key fa-7x"></i>
    </div>
</template>

<script>
export default {    
    name: 'Sidebar'
}
</script>

<style scoped>
    .sidebar{
        position: relative;
        float: left;
        width: 350px;
        height: 100vh;
        background: linear-gradient(rgb(70, 63, 133),rgb(37, 33, 85));
        overflow: hidden;
        border-right: 2px solid white;
    }
    #keller{
        margin-top: 200px;
        width: 150px;
        border-radius: 10px;
    }
    #contact{
        display: block;
        font-size: 21px;
        color: #e00404;
        font-family:'Lato', sans-serif;
        width: 120px;
        height: 50px;
        margin: 20px 0px 0px 115px;
        background-color: white;
        border-radius: 10px;
        transition: all .2s ease-in-out;
    }
    #contact:hover{
        cursor: pointer;
        background-color:#9cc7e6 ;
    }
    #sink{
        position: absolute;
        opacity: .7;
        top: -50px;
        color: rgb(75, 195, 59);
        transform: rotate(49deg);
    }
    .sink_ate {
        animation: float 100s ease-in-out;
        animation-iteration-count: infinite;
    }
    #house{
        left: 700px;
        top: 200px;
        position: absolute;
        opacity: .7;
        color: rgb(68, 59, 195);
    }
    .house_ate{
        animation: house 10s ease-in-out;
        animation-iteration-count: infinite;
        animation-delay: 15s;
    }
    #key {
        left: 100px;
        top: 600px;
        position: absolute;
        opacity: .7;
        color: rgb(68, 59, 195);
        transform: rotate(80deg);
    }
    .key_ate{
        animation: key 110s ease-in-out;
        animation-iteration-count: infinite;
        animation-delay: 5s;
    }
    #door {
        left: 150px;
        top: 450px;
        position: absolute;
        opacity: .7;
        color: rgb(197, 46, 46);
    }
    .door_ate{
        animation: door 40s ease-in-out;
        animation-iteration-count: infinite;
    }
    #bighouse{
        left: -90px;
        top: 400px;
        position: absolute;
        opacity: 40%;
        color: rgb(68, 59, 195);
        transform: rotate(49deg);
    }
    .bighouse_ate{
        animation: bighouse 80s ease-in-out;
        animation-iteration-count: infinite;
    }
    #bigkey {
        left: 600px;
        top: 700px;
        position: absolute;
        opacity: 40%;
        color: rgb(255, 252, 90);
        transform: rotate(49deg);
    }
    .bigkey_ate{
        animation: bigkey 100s ease-in-out;
        animation-iteration-count: infinite;
    }

    @keyframes house {
        50%{
            transform: translate(-1000px, 100px) rotate(360deg);      
        }
    }
    @keyframes float {
        50%{
            transform: translate(300px, 700px) rotate(180deg);
        }
    }
    @keyframes key {
        50%{
            transform: translate(0px, -850px);
        }
    }
    @keyframes door {
        50% {
            transform: translate(-450px, -700px) rotate(360deg)
        }
    }
    @keyframes bighouse {
        50%{
            transform: translate(500px, -700px) rotate(700deg);
        }
    }
    @keyframes bigkey {
        50%{
            transform: translate(-750px, -400px) rotate(180deg);
        }
    }
</style>

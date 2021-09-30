<template>
    <div class="mainpic">
        <div class="zach-pic" id="zach-pic"></div>
        <img @click="chaos()" class="zachface_ate" id="zachface" src="../assets/zachface.png" alt="zachface">
        <h3 id="clickme">Click Me</h3>
        <div class="about_zach">
            <h1 id="greeting">Hi, I'm Zach!</h1>
            <p id="about_text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit cumque quia voluptates aliquam perspiciatis eum quidem perferendis in rem! Ratione, voluptas?Eum delectus expedita totam quae hic distinctio ullam nisi?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit magni exercitationem maiores. Dolore facilis excepturi veritatis sit tenetur error, harum at eaque atque! Magni cumque, velit sunt possimus illo quae? Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde voluptatum debitis quo enim eos dolores, impedit sint nemo quas praesentium maxime, vero beatae. Repellendus facere esse, nesciunt sequi mollitia officiis.</p>
            <button @click="displayContact()" id="contact">Contact Me</button>
        </div>
        <Sidebar hidden/>
    </div>
</template>

<script>
import store from '@/store.js'
import Sidebar from '../components/Sidebar.vue'
export default {
    name: 'ZachPic',
    components: {
        Sidebar,
    },
    data(){
        return store.state
    },
    methods: {
        chaos(){
            var zachface = document.getElementById("zachface")
            var sink = document.getElementById("sink");
            var house = document.getElementById("house")
            var key = document.getElementById("key")
            var door = document.getElementById("door")
            var bighouse = document.getElementById("bighouse")
            var bigkey = document.getElementById("bigkey")
            var contact = document.getElementById("contact")
            zachface.classList.remove("zachface_ate")
            sink.classList.add("sink_ate")
            house.classList.add("house_ate")
            key.classList.add("key_ate")
            door.classList.add("door_ate")
            bighouse.classList.add("bighouse_ate")
            bigkey.classList.add("bigkey_ate")
            contact.classList.add("contact_ate")
        },
        displayContact(){
            store.ContactForm()
        }
    },
    mounted(){
        var zachface = document.getElementById("zachface")
        var zachpic = document.getElementById("zach-pic")
        zachface.addEventListener("mouseover", mOver, false)
        zachface.addEventListener("mouseout", mOut, false)
        
        function mOver(){
            zachpic.setAttribute("style", "width:450px; height:450px; top:120px; left:380px;")
        }
        function mOut(){
            zachpic.setAttribute("style", "left: 401px; top: 150px; width: 400px; height: 400px;")
        }
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@1,900&display=swap');
    .mainpic{
        display: flex;
        justify-content: space-around;
        height: 100vh;
        background: radial-gradient(#9cc7e6 100%, #ffffff  50%);
    }
    .zach-pic{
        position: absolute;
        left: 401px;
        top: 150px;
        width: 400px;
        height: 400px;
        border-radius: 100%;
        border: 5px dashed rgb(37, 33, 85);
        animation: rotation 30s infinite linear;
        transition: all .5s ease-in-out;
    }
    #clickme {
        position:absolute;
        top: 170px;
        left: 575px;
    }
    #zachface{
        width: 420px;
        height: 370px;
        margin: 80px 0px 0px 50px;
        transition: all .5s ease-in-out;
    }
    .zachface_ate{
        animation: pulse 2s infinite ease-in-out;
        cursor: pointer;
    }
    .about_zach{
        padding: 0px 50px;
        margin: 50px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }
    #greeting{
        font-size: 55px;
        font-family:'Lato', sans-serif;
    }
    #contact{
        position: absolute;
        left: 0px;
        top: 425px;
        font-size: 21px;
        color: #e00404;
        font-family:'Lato', sans-serif;
        width: 120px;
        height: 50px;
        margin: 20px 0px 0px 115px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgb(8, 8, 8);
        transition: all .2s ease-in-out;
    }
    .contact_ate{
        animation: contact 25s ease-in-out;
        animation-fill-mode: forwards;
        animation-delay: 5s;
    }
    #contact:hover{
        cursor: pointer;
        background-color:#d4d4d4 ;
    }

@keyframes rotation {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}
@keyframes contact {
    100%{
        transform: translate(900px, -330px) rotate(720deg)
    }
}
@keyframes pulse {
    50%{
        filter: brightness(150%);
    }
    100%{
        filter: brightness(100%);
    }
}
</style>

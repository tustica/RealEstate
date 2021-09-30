<template>
    <div class="contact">
        <img @click="killContact()" id="xicon" src="../assets/xicon.png" alt="xicon">
        <form id="form">
                <input class="content" type="text" name="name" v-model="name" placeholder="Name">
                <input class="content" type="text" name="email" v-model="email" placeholder="Email">
                <textarea class="content" cols="30" rows="5" name="message" v-model="message" placeholder="Message"></textarea>
                <input @click="sendEmail()" id="send" class="content" type="submit" value="Send">
        </form>
    </div> 
</template>

<script>
import emailjs from 'emailjs-com';
import store from '@/store.js'
export default {
    name: 'Contact',
    data(){
        return {
            store: store.state,
            name: '',
            email: '',
            message: ''
        }
    },
    methods: {
        killContact(){
            store.killContactForm()
        },
        sendEmail(e){
            try {
                emailjs.sendForm('service_ygpj0kd', 'template_hreugpi', e.target,
                'user_3gqTY4G8Rbn56e3Gd2uBT', {
                    name: this.name,
                    email: this.email,
                    message: this.message
                })
            } catch(error) {
                console.log({error})
            }
            this.name = ''
            this.email = ''
            this.message = ''
        }
    }   
}
</script>

<style scoped>
    .contact{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100vw;
        height: 100vh;
        position: absolute;
        background: rgba(0, 0, 0,0.7);
        top:0;
        left:0;
    }
    #form{
        display: flex;
        flex-direction: column;
        width: 300px;
    }
    .content{
        font-family:'Lato', sans-serif;
        font-size: 20px;
        padding: 10px;
        margin: 20px;
    }
    #send{
        cursor: pointer;
        align-self: center;
        font-size: 21px;
        color: #e00404;
        font-family:'Lato', sans-serif;
        width: 120px;
        height: 50px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgb(8, 8, 8);
    }
    #xicon{
        cursor: pointer;
        position: absolute;
        width: 50px;
        top:60px;
        left: 850px;
    }
</style>

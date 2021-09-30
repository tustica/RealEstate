<template>
  <div id="app">
    <Header msg="Welcome to Your Vue.js App"/>
    <Sidebar/>
    <ZachPic/>
    <Contact v-if="contact"/>

  </div>
</template>

<script>
import store from '@/store.js'
import Header from './components/Header.vue'
import Sidebar from './components/Sidebar.vue'
import ZachPic from './components/ZachPic.vue'
import Contact from './components/Contact.vue'

export default {
  name: 'App',
  components: {
    Header,
    Sidebar,
    ZachPic,
    Contact
  },
  data(){
    return store.state
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  transition: all 1s ease-in-out 0s;
}
html, body {
  margin: 0px;
}
</style>

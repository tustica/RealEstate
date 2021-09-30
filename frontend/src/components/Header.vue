<template>
  <div id="nav" class="header">
    <div class="leftside">
      <img id="doormat" src="../assets/doormat.png" alt="doormat">
      <!-- <i id="home_icon" class="fas fa-home fa-2x"></i> -->
      <h1 id="title">Zach Menezes</h1>
    </div>
    <ul class="nav-links">
      <li>About</li>
      <li>Homes</li>
      <li>Extra</li>
    </ul>
    <div class="social-links">
      <i class="fab fa-twitter"></i>
      <i class="fab fa-instagram"></i>
      <i class="fab fa-facebook"></i>
    </div>
  </div>
  
</template>

<script>

export default {
  name: 'Header',
  props: {
    msg: String
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@1,900&display=swap');
body, html{
  margin: 0px;
}
.header{
  width: 100%;
  height: 85px;
  background: linear-gradient(rgb(70, 63, 133),rgb(37, 33, 85));
  box-shadow: 0px 3px 5px rgb(179, 179, 179);
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0px;
  border-bottom: 2px solid white;
  
}
.nav-links {
  list-style: none;
}

.nav-links li{
  display: inline-block;
  padding: 0px 15px;
}
.nav-links li{
  text-decoration: none;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 20px;
  color: rgb(255, 255, 255);
  transition: all 0.5s ease 0s ;
  
}
.nav-links li:hover{
  color: rgb(255, 15, 15);
  cursor: pointer;
  text-decoration: underline;

}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#title{
  color: white;
  font-size: 35px;
  font-family:'Lato', sans-serif;
  margin-left: 15px;
  align-self: center;
}
#home_icon{
  margin-left: 30px;
  margin-top: 20px;
  color: white;

}
.leftside{
  display: flex;
  text-align: center;
}
.social-links{
  font-size: 25px;
  display: flex;
  width: 200px;
  justify-content: space-around;
  color: white;
}
.social-links i:hover{
  color: rgb(255, 15, 15);
  cursor: pointer;
  transition: all 0.5s ease 0s ;
}
#doormat{
  margin-left: 10px;
  width: 100px;
  animation: doormat 70s ease-in-out;
  animation-delay: 5s;
}

/* @keyframes doormat {
  50%{
    transform: translate(1000px, 300px) rotate(280deg);
  }
} */
</style>

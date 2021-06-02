<template>
  <div class="space">
    <div class="text">
      <div class="align-middle">
        <h1>404</h1>
      </div>
    </div>
    <div class="orbit-1"></div>
    <div class="moon-1 sm"></div>
    <div class="orbit-2"></div>
    <div class="moon-2 sm"></div>
    <div class="orbit-3"></div>
    <div class="moon-3"></div>
  </div>
</template>

<style>
html,
body {
  background: #0d1117;
  width: 100%;
  height: 100%;
  overflow: hidden;
  font-family: "Varela Round", sans-serif;
  letter-spacing: 0.1em;
  font-smooth: antialiased;
}

.space {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 50%;
  left: 50%;
}
.space > div {
  position: absolute;
}
.space .text {
  display: table;
  z-index: 100;
  margin-top: -250px;
  margin-left: -250px;
  width: 500px;
  height: 500px;
  color: #fff;
}
.space .text .align-middle {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}
.space .text h1 {
  font-size: 140px;
  line-height: 0.01em;
}
.space .text p {
  font-size: 18px;
  color: #687c8f;
}
.space div[class^="moon"] {
  background: url("https://i.imgur.com/0i18KL5.png");
  background-size: 60px;
  width: 60px;
  height: 60px;
  z-index: 10;
}
.space div[class^="moon"].sm {
  background-size: 30px;
  width: 30px;
  height: 30px;
}
.space .moon-1 {
  margin-top: -15px;
  margin-left: -15px;
  background-size: 50% auto;
  animation: orbit1 15s linear infinite;
}
.space .moon-2 {
  margin-top: -15px;
  margin-left: -15px;
  animation: orbit2 -6s 18s linear infinite;
}
.space .moon-3 {
  margin-top: -30px;
  margin-left: -30px;
  animation: orbit3 -12s 22s linear infinite;
}
.space .orbit-1 {
  margin-top: -250px;
  margin-left: -250px;
  width: 500px;
  height: 500px;
  border-radius: 250px;
  background: #3f5468;
  z-index: 8;
}
.space .orbit-2 {
  margin-top: -340px;
  margin-left: -340px;
  width: 680px;
  height: 680px;
  border-radius: 340px;
  background: #3a4f64;
  z-index: 7;
}
.space .orbit-3 {
  margin-top: -395px;
  margin-left: -395px;
  width: 790px;
  height: 790px;
  border-radius: 395px;
  background: #374c61;
  z-index: 6;
}
@keyframes orbit1 {
  from {
    transform: rotate(0deg) translateX(250px);
  }
  to {
    transform: rotate(360deg) translateX(250px);
  }
}
@keyframes orbit2 {
  from {
    transform: rotate(0deg) translateX(340px);
  }
  to {
    transform: rotate(360deg) translateX(340px);
  }
}
@keyframes orbit3 {
  from {
    transform: rotate(0deg) translateX(395px);
  }
  to {
    transform: rotate(360deg) translateX(395px);
  }
}
</style>

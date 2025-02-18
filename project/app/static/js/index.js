"use strict";

function toggleModal() {
  // mainタグのhidden切り替え
  const homeMain = document.getElementsByClassName("home-main")[0];
  homeMain.classList.toggle("hidden");
  // modalのhidden切り替え
  const modal = document.getElementsByClassName("modal")[0];
  modal.classList.toggle("hidden");
}
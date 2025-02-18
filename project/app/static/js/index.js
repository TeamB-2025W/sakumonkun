"use strict";

function toggleModal(testTitle) {
  // mainタグのhidden切り替え
  const homeMain = document.getElementsByClassName("home-main")[0];
  homeMain.classList.toggle("hidden");
  // modalのhidden切り替え
  const modal = document.getElementsByClassName("modal")[0];
  modal.classList.toggle("hidden");

  if (testTitle) {
    document.getElementById("test-title-viewer").textContent = testTitle;
  }
}
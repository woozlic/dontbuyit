function copyPhone() {
  let copyText = document.getElementById("phoneInput");
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */
  document.execCommand("copy");
  let tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Скопировано: " + copyText.value;
}

function outPhone() {
  let tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Скопировать";
}
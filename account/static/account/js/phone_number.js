function copyPhone() {
  /* Get the text field */
  let copyText = document.getElementById("phoneInput");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  document.execCommand("copy");

  let tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Скопировано: " + copyText.value;

}

function outPhone() {
  let tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Скопировать";
}
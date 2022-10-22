let plusClick = document.getElementById('plusClick');
let btnClear = document.getElementById('btnClear');
let minClick = document.getElementById('minClick');
let pWait = document.getElementById('waiting');
let plus = 0;

plusClick.onclick = function () {
  plus++;
  pWait.textContent = plus;
}
minClick.onclick = function () {
  plus--;
  pWait.textContent = plus;
}
btnClear.onclick = function () {
  pWait.textContent = "";
  plus = 0;
}
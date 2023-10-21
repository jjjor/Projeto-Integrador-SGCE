console.log("Ola mundo");
const input = document.querySelector("#data_nascimento");

input.addEventListener("input", (e) => {
  if (e.target.value.length > 10) {
    e.target.value = e.target.value.substring(0, 10);
  }
});
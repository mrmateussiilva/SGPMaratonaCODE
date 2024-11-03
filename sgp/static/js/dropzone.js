

const dropzone = document.getElementById("dropzone");

// Para colar a imagem
document.addEventListener("paste", (event) => {
  const items = event.clipboardData.items;
  for (const item of items) {
    if (item.type.indexOf("image") !== -1) {
      const file = item.getAsFile();
      const reader = new FileReader();
      reader.onload = (event) => {
        const img = document.createElement("img");
        img.setAttribute("id", "imagemFicha");
        img.src = event.target.result;
        dropzone.innerHTML = ""; // Limpa a área para a nova imagem
        dropzone.appendChild(img); // Mostra a imagem
      };
      reader.readAsDataURL(file);
    }
  }
});

// Para arrastar e soltar a imagem
dropzone.addEventListener("dragover", (event) => {
  event.preventDefault(); // Necessário para permitir o "drop"
  dropzone.style.borderColor = "#00cc00"; // Mudar a cor da borda ao arrastar
});

dropzone.addEventListener("dragleave", () => {
  dropzone.style.borderColor = "#cccccc"; // Voltar à cor original
});

dropzone.addEventListener("drop", (event) => {
  event.preventDefault();
  const file = event.dataTransfer.files[0];
  if (file && file.type.startsWith("image/")) {
    const reader = new FileReader();
    reader.onload = (event) => {
      const img = document.createElement("img");
      img.src = event.target.result;
      dropzone.innerHTML = ""; // Limpa a área para a nova imagem
      dropzone.appendChild(img); // Mostra a imagem
    };
    reader.readAsDataURL(file);
  }
});

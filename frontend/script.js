
async function upload() {
  const file = document.getElementById('fileInput').files[0];
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch('https://<your-backend-url>.onrender.com/analyze', {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById('output').textContent = data.analysis;
}

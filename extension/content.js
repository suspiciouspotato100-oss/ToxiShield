async function analyzeComment(text, element) {
  try {
    const response = await fetch("https://toxishield.onrender.com/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await response.json();
    if (data.label === "TOXIC") {
      element.style.filter = "blur(6px)";
      element.title = "⚠ Toxic comment detected";
    }
  } catch (error) {
    console.error("Error analyzing comment:", error);
  }
}

function scanInstagramComments() {
  const comments = document.querySelectorAll("ul._a9ym span");
  comments.forEach(comment => {
    const text = comment.innerText.trim();
    if (text && !comment.classList.contains("checked")) {
      comment.classList.add("checked");
      analyzeComment(text, comment);
    }
  });
}

setInterval(scanInstagramComments, 3000);
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fun Facts Generator</title>
  <style>
    /* General Styling */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background-color: #f0f8ff;
      margin: 0;
      padding: 0;
    }

    h1 {
      color: #2c3e50;
      margin-top: 20px;
    }

    /* Button Styling */
    button {
      padding: 10px 20px;
      font-size: 16px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    button:hover {
      background-color: #1abc9c;
      transform: scale(1.1);
      transition: all 0.3s;
    }

    /* Dropdown Styling */
    select {
      padding: 10px;
      margin: 10px;
      font-size: 16px;
      border-radius: 5px;
      border: 1px solid #ccc;
    }

    /* Fact Text Styling */
    p {
      margin-top: 20px;
      font-size: 18px;
      color: #34495e;
      animation: fadeIn 1.5s;
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
  </style>
</head>
<body>
  <h1>Fun Facts About Earth</h1>
  <select id="category">
    <option value="science">Science</option>
    <option value="history">History</option>
    <option value="nature">Nature</option>
  </select>
  <button id="generate-btn">Generate Another Fun Fact</button>
  <button id="share-btn">Share Fun Fact</button>
  <p id="fun-fact"></p>

  <script>
    const facts = {
      science: [
        "Earth’s atmosphere is 78% nitrogen and 21% oxygen.",
        "Earth is about 4.5 billion years old."
      ],
      history: [
        "Earth is the only planet known to support life.",
        "The Moon influences ocean tides."
      ],
      nature: [
        "71% of Earth's surface is water.",
        "Earth has diverse ecosystems like rainforests and deserts."
      ]
    };

    document.getElementById("generate-btn").addEventListener("click", () => {
      const selectedCategory = document.getElementById("category").value;
      const randomFact = facts[selectedCategory][Math.floor(Math.random() * facts[selectedCategory].length)];
      document.getElementById("fun-fact").innerText = randomFact;
    });

    document.getElementById("share-btn").addEventListener("click", () => {
      const fact = document.getElementById("fun-fact").innerText;
      const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(fact)} - Generated in GenAl workshop!`;
      window.open(twitterUrl, "_blank");
    });
  </script>
</body>
</html>

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    your_name = "Abi"
    his_name = "Rei"

    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Birthday</title>

<style>
body {
    margin: 0;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(to right, #ff758c, #ff7eb3);
    overflow-x: hidden;
    color: white;
}

/* Header */
h1 {
    margin-top: 30px;
    font-size: 35px;
}

.names {
    font-size: 18px;
    margin-bottom: 15px;
}

/* Photo */
img {
    width: 220px;
    max-width: 80%;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
}

/* Message */
.message {
    width: 85%;
    margin: 20px auto;
    font-size: 18px;
    min-height: 120px;
}

/* Cake */
.cake {
    font-size: 70px;
    cursor: pointer;
    margin-top: 15px;
}

/* Love letter popup */
.popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0);
    background: white;
    color: #333;
    padding: 20px;
    border-radius: 15px;
    width: 80%;
    max-width: 300px;
    z-index: 10;
    transition: 0.3s;
}

.popup.active {
    transform: translate(-50%, -50%) scale(1);
}

/* Hearts */
.heart {
    position: fixed;
    color: pink;
    font-size: 20px;
    animation: floatHeart 5s linear infinite;
}

@keyframes floatHeart {
    0% { transform: translateY(0); opacity:1;}
    100% { transform: translateY(-100vh); opacity:0;}
}

/* Firework */
.firework {
    position: fixed;
    width: 10px;
    height: 10px;
    background: yellow;
    border-radius: 50%;
    animation: explode 1s ease-out forwards;
}

@keyframes explode {
    to {
        transform: scale(10);
        opacity: 0;
    }
}

</style>
</head>

<body>

<h1>🎉 Happy Birthday, {{his_name}}! 🎉</h1>
<div class="names">From {{your_name}} 💖</div>

<img src="https://drive.google.com/file/d/1gIawnqRKwrt9Ci6EPlW6aBhvmfAzbXIN/view?usp=sharing">

<div class="message" id="message"></div>

<div class="cake" onclick="cakeClick()">🎂</div>

<!-- Love Letter -->
<div class="popup" id="popup">
    <h3>💌 For You</h3>
    <p>I just want you to know that you mean everything to me. I miss you.💖</p>
</div>

<audio autoplay loop>
<source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3">
</audio>

<script>
// Typing message
const text = "Happiest birthday to the greatest man I know.💖\\n\\n" +
"May your year ahead be filled with love, laughter, unforgettable adventures, and endless opportunities.\\n\\n" +
"Thank you for being such an amazing man. I am forever grateful to have you in my life.\\n\\n" +
"I am always here for you. Enjoy your day! I love you. God bless you, my bebi.💕";

let i = 0;
function typeWriter() {
    if (i < text.length) {
        document.getElementById("message").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, 35);
    }
}
typeWriter();

// Popup auto show
setTimeout(() => {
    document.getElementById("popup").classList.add("active");
}, 2000);

// Cake click fireworks
function cakeClick() {
    for (let i = 0; i < 20; i++) {
        let f = document.createElement("div");
        f.className = "firework";
        f.style.left = Math.random() * 100 + "vw";
        f.style.top = Math.random() * 100 + "vh";
        document.body.appendChild(f);
        setTimeout(() => f.remove(), 1000);
    }
}

// Floating hearts
setInterval(() => {
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "💖";
    heart.style.left = Math.random() * 100 + "vw";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 5000);
}, 300);

</script>

</body>
</html>
""", your_name=your_name, his_name=his_name)

if __name__ == "__main__":
    app.run(debug=True)
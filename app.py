from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    name = "My Rei"  

    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Happy Birthday</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            overflow: hidden;
            color: white;
        }

        h1 {
            font-size: 50px;
            margin-top: 60px;
            animation: fadeIn 2s ease-in-out;
        }

        .message {
            width: 70%;
            margin: 30px auto;
            font-size: 20px;
            line-height: 1.6;
            background: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            animation: fadeIn 3s ease-in-out;
        }

        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        /* Balloons */
        .balloon {
            width: 60px;
            height: 80px;
            border-radius: 50%;
            position: absolute;
            bottom: -120px;
            animation: floatUp linear infinite;
        }

        @keyframes floatUp {
            0% { transform: translateY(0); }
            100% { transform: translateY(-120vh); }
        }

        /* Confetti */
        .confetti {
            position: fixed;
            width: 10px;
            height: 10px;
            top: 0;
            animation: fall linear infinite;
        }

        @keyframes fall {
            0% { transform: translateY(0); }
            100% { transform: translateY(100vh); }
        }

    </style>
</head>

<body>

    <h1>🎉 Happy Birthday {{name}}! 🎉</h1>

    <div class="message">
        Happiest birthday to the greatest man I know. 💖<br><br>
        May your year ahead be filled with love, laughter, unforgettable adventures, 
        and endless opportunities.<br><br>
        Thank you for being such an amazing man—I’m forever grateful to have you in my life.<br><br>
        I love you, always. 💕<br>
        God bless you, bebi.
    </div>

    <!-- Music -->
    <audio autoplay loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>

    <script>
        // Balloons
        for (let i = 0; i < 15; i++) {
            let b = document.createElement("div");
            b.className = "balloon";
            b.style.left = Math.random() * 100 + "vw";
            b.style.backgroundColor = "hsl(" + Math.random()*360 + ",100%,60%)";
            b.style.animationDuration = (5 + Math.random()*5) + "s";
            document.body.appendChild(b);
        }

        // Confetti
        for (let i = 0; i < 80; i++) {
            let c = document.createElement("div");
            c.className = "confetti";
            c.style.left = Math.random() * 100 + "vw";
            c.style.backgroundColor = "hsl(" + Math.random()*360 + ",100%,50%)";
            c.style.animationDuration = (3 + Math.random()*4) + "s";
            document.body.appendChild(c);
        }
    </script>

</body>
</html>
""", name=name)

if __name__ == "__main__":
    app.run(debug=True)
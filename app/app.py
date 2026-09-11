from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>BMW Convertible</title>
        <style>
        * { box-sizing: border-box; }
        html, body {
            margin: 0;
            width: 100%;
            height: 100%;
            font-family: Arial, Helvetica, sans-serif;
            background:
                linear-gradient(rgba(0,0,0,0.10), rgba(0,0,0,0.18)),
                url("https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=1600&q=80") center/cover no-repeat fixed;
        }

        body {
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .wallpaper {
            width: 100vw;
            height: 100vh;
        }
        </style>
    </head>
    <body>
        <div class="wallpaper"></div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

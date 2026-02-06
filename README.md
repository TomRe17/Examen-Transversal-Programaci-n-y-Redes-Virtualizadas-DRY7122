<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reloj Digital</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
        }

        .reloj {
            width: 250px;
            height: 250px;
            background-color: #bdbdbd;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 36px;
            font-weight: bold;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #555;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #333;
        }
    </style>
</head>
<body>

    <div class="reloj" id="reloj">00:00:00</div>

    <button onclick="volver()">Volver al inicio</button>

    <script>
        function actualizarReloj() {
            const ahora = new Date();
            let h = ahora.getHours();
            let m = ahora.getMinutes();
            let s = ahora.getSeconds();

            h = h < 10 ? "0" + h : h;
            m = m < 10 ? "0" + m : m;
            s = s < 10 ? "0" + s : s;

            document.getElementById("reloj").textContent = `${h}:${m}:${s}`;
        }

        function volver() {
            window.location.href = "index.html";
        }

        setInterval(actualizarReloj, 1000);
        actualizarReloj();
    </script>

</body>
</html>

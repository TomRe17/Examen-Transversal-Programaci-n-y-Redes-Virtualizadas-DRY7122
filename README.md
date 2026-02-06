<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reloj Digital</title>
    <style>
        body {
            display: flex;
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
            color: #000;
            border-radius: 8px; /* opcional */
        }
    </style>
</head>
<body>

    <div class="reloj" id="reloj">
        00:00:00
    </div>

    <script>
        function actualizarReloj() {
            const ahora = new Date();
            let horas = ahora.getHours();
            let minutos = ahora.getMinutes();
            let segundos = ahora.getSeconds();

            // Agregar cero si es menor a 10
            horas = horas < 10 ? "0" + horas : horas;
            minutos = minutos < 10 ? "0" + minutos : minutos;
            segundos = segundos < 10 ? "0" + segundos : segundos;

            document.getElementById("reloj").textContent =
                horas + ":" + minutos + ":" + segundos;
        }

        setInterval(actualizarReloj, 1000);
        actualizarReloj();
    </script>

</body>
</html>

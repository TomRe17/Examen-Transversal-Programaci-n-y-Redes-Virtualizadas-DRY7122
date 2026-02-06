<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Calculadora</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        background: linear-gradient(to bottom right, #eff6ff, #e0f2fe);
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 2rem;
      }

      .greeting-section {
        margin-bottom: 3rem;
        text-align: center;
      }

      .greeting-btn {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        padding: 1rem 2rem;
        border: none;
        border-radius: 0.5rem;
        font-size: 1rem;
        cursor: pointer;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transition: all 0.2s;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin: 0 auto;
      }

      .greeting-btn:hover {
        background-color: #1d4ed8;
        transform: scale(1.05);
      }

      .greeting-btn:active {
        transform: scale(0.98);
      }

      .greeting-message {
        margin-top: 1rem;
        font-size: 1.125rem;
        font-weight: 500;
        color: #1e40af;
        animation: pulse 2s infinite;
      }

      @keyframes pulse {
        0%, 100% {
          opacity: 1;
        }
        50% {
          opacity: 0.5;
        }
      }

      .calculator-container {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
      }

      .calculator {
        background: white;
        border-radius: 1rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        padding: 1.5rem;
        width: 320px;
      }

      .display {
        background-color: #1f2937;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
      }

      .display-value {
        text-align: right;
        color: white;
        font-size: 2rem;
        font-family: 'Courier New', monospace;
        word-wrap: break-word;
        word-break: break-all;
      }

      .buttons-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.5rem;
      }

      button {
        padding: 1rem;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        border-radius: 0.5rem;
        cursor: pointer;
        transition: all 0.2s;
      }

      button:active {
        transform: scale(0.95);
      }

      .btn-number {
        background-color: #e5e7eb;
        color: #1f2937;
      }

      .btn-number:hover {
        background-color: #d1d5db;
      }

      .btn-operator {
        background-color: #f97316;
        color: white;
      }

      .btn-operator:hover {
        background-color: #ea580c;
      }

      .btn-clear {
        background-color: #ef4444;
        color: white;
        grid-column: span 2;
      }

      .btn-clear:hover {
        background-color: #dc2626;
      }

      .btn-equals {
        background-color: #22c55e;
        color: white;
        grid-row: span 2;
      }

      .btn-equals:hover {
        background-color: #16a34a;
      }

      .clock-btn {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        padding: 1rem 2rem;
        width: 320px;
        border: none;
        border-radius: 0.5rem;
        font-size: 1rem;
        cursor: pointer;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transition: all 0.2s;
      }

      .clock-btn:hover {
        background-color: #1d4ed8;
        transform: scale(1.02);
      }

      .clock-btn:active {
        transform: scale(0.98);
      }
    </style>
  </head>
  <body>
    <div class="greeting-section">
      <button class="greeting-btn" onclick="showGreeting()">
        <span>😊</span>
        Saludar
      </button>
      <div id="greeting-message" class="greeting-message"></div>
    </div>

    <div class="calculator-container">
      <div class="calculator">
        <div class="display">
          <div class="display-value" id="display">0</div>
        </div>

        <div class="buttons-grid">
          <button class="btn-clear" onclick="clearDisplay()">C</button>
          <button class="btn-operator" onclick="setOperation('÷')">÷</button>
          <button class="btn-operator" onclick="setOperation('×')">×</button>

          <button class="btn-number" onclick="appendNumber('7')">7</button>
          <button class="btn-number" onclick="appendNumber('8')">8</button>
          <button class="btn-number" onclick="appendNumber('9')">9</button>
          <button class="btn-operator" onclick="setOperation('-')">-</button>

          <button class="btn-number" onclick="appendNumber('4')">4</button>
          <button class="btn-number" onclick="appendNumber('5')">5</button>
          <button class="btn-number" onclick="appendNumber('6')">6</button>
          <button class="btn-operator" onclick="setOperation('+')">+</button>

          <button class="btn-number" onclick="appendNumber('1')">1</button>
          <button class="btn-number" onclick="appendNumber('2')">2</button>
          <button class="btn-number" onclick="appendNumber('3')">3</button>
          <button class="btn-equals" onclick="calculate()">=</button>

          <button class="btn-number" style="grid-column: span 2;" onclick="appendNumber('0')">0</button>
          <button class="btn-number" onclick="appendDecimal()">.</button>
        </div>
      </div>

      <a href="clock.html">
        <button class="clock-btn">Ver Reloj</button>
      </a>
    </div>

    <script>
      let display = '0';
      let previousValue = null;
      let operation = null;
      let shouldResetDisplay = false;

      function updateDisplay() {
        document.getElementById('display').textContent = display;
      }

      function appendNumber(num) {
        if (shouldResetDisplay) {
          display = num;
          shouldResetDisplay = false;
        } else {
          if (display === '0') {
            display = num;
          } else {
            display += num;
          }
        }
        updateDisplay();
      }

      function appendDecimal() {
        if (shouldResetDisplay) {
          display = '0.';
          shouldResetDisplay = false;
        } else if (!display.includes('.')) {
          display += '.';
        }
        updateDisplay();
      }

      function setOperation(op) {
        const currentValue = parseFloat(display);

        if (previousValue !== null && operation && !shouldResetDisplay) {
          const result = calculateResult(previousValue, currentValue, operation);
          display = String(result);
          previousValue = result;
        } else {
          previousValue = currentValue;
        }

        operation = op;
        shouldResetDisplay = true;
        updateDisplay();
      }

      function calculateResult(prev, current, op) {
        switch (op) {
          case '+':
            return prev + current;
          case '-':
            return prev - current;
          case '×':
            return prev * current;
          case '÷':
            return prev / current;
          default:
            return current;
        }
      }

      function calculate() {
        if (previousValue !== null && operation) {
          const currentValue = parseFloat(display);
          const result = calculateResult(previousValue, currentValue, operation);
          display = String(result);
          previousValue = null;
          operation = null;
          shouldResetDisplay = true;
          updateDisplay();
        }
      }

      function clearDisplay() {
        display = '0';
        previousValue = null;
        operation = null;
        shouldResetDisplay = false;
        updateDisplay();
      }

      function showGreeting() {
        const messageEl = document.getElementById('greeting-message');
        messageEl.textContent = '¡Hola! ¡Que tengas un excelente día!';
        setTimeout(() => {
          messageEl.textContent = '';
        }, 3000);
      }
    </script>
  </body>
</html>

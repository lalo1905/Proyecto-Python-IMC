Calculadora de Índice de Masa Corporal (IMC) 

Proyecto desarrollado en Python para calcular el Índice de Masa Corporal de un usuario desde la consola.

Características Principales
 **Validación robusta de datos de texto**: 
   Los campos de nombre y apellidos verifican obligatoriamente que no estén vacíos y que contengan **estrictamente letras** (utilizando `.isalpha()` y omitiendo espacios en nombres compuestos).

 **Validación estricta de datos numéricos**:
   Obliga al usuario a ingresar números válidos mayores a cero para la edad, el peso y la estatura.

   **Estatura con formato decimal**: Requiere obligatoriamente el uso de punto decimal (ej. `1.75`) para asegurar la precisión del cálculo.

 **Manejo de Excepciones (`try-except`)**: Evita que el programa colapse o se cierre de golpe si el usuario introduce letras o caracteres no válidos donde se esperan números.
 
 **Formato y Presentación (`f-strings`)**:
   Capitaliza automáticamente los nombres y apellidos (`.capitalize()`).
   Muestra un resumen detallado y simétrico en la consola.
   Redondea el resultado final del IMC a exactamente dos decimales (`:.2f`).

Tecnologías y Herramientas Utilizadas
 **Python** (Lógica de programación, bucles `while`, condicionales, manejo de excepciones).
 **Git y GitHub** (Control de versiones y almacenamiento del repositorio).
 **Visual Studio Code (VS Code)** (Entorno de desarrollo).

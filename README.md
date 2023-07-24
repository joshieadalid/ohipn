# ohipn
Optimizador de Horarios IPN (OHIPN)
# Descripción

Este proyecto, "Optimizador de Horarios IPN" (OHIPN), es una solución diseñada para ayudar a los estudiantes del Instituto Politécnico Nacional (IPN) en México a optimizar sus horarios de clases. Mediante la utilización de algoritmos eficientes, este proyecto proporciona una selección de horarios optimizados basados en la oferta de clases disponibles.
# Instalación

Para instalar y ejecutar este proyecto, sigue los siguientes pasos:

## Clona el repositorio a tu local:

bash
`git clone https://github.com/username/OHIPN.git`

    Navega al directorio clonado:

bash
`cd OHIPN`

    Asegúrate de tener instaladas todas las dependencias necesarias. Este proyecto utiliza la biblioteca NetworkX para manejo de grafos y pandas para manejo de datos:

bash
`pip install networkx pandas`

    Ejecuta el script principal:

bash
`python main.py`

# Uso

El script principal (main.py) cargará los datos de las materias disponibles desde un archivo JSON (horarios.json). Luego, utilizará estos datos para generar una serie de horarios posibles, optimizando para minimizar el tiempo libre entre clases y maximizar la cantidad de materias diferentes.

Los horarios optimizados se imprimirán en la consola. Cada horario incluirá una lista de clases con los respectivos horarios y la "fragmentación" del horario, que es una medida de cuánto tiempo libre hay entre clases.

Además, se proporciona un script (create.py) para convertir los datos de las materias disponibles de un formato CSV a un formato JSON.
# Contribución

Si deseas contribuir a este proyecto, puedes hacerlo de las siguientes formas:

* Reportando errores.
* Sugiriendo nuevas características.
* Mejorando el código o la documentación.
* Compartiendo el proyecto con otros.

Para contribuir, por favor primero crea un issue en el repositorio para discutir lo que te gustaría cambiar.
# Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
# Contacto

Si tienes alguna pregunta o comentario, por favor crea un issue en el repositorio y estaremos encantados de ayudarte.
# Autores

* Josué Adalid Juárez Botello

Este proyecto es mantenido por estudiantes del Instituto Politécnico Nacional. Agradecemos a todos los que han contribuido a su desarrollo.

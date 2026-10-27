# cars-sales-app
Nueva app para explorar, visualizar y comparar los datos de los diversos anuncios de carros en venta.

## Funcionalidades
- Puedes ver un histograma de la venta de los diversos carros.
- También se despliega un gráfico de dispersión con los carros que se encuentran en venta.

## Estructura del repositorio
- app.py: tiene el código de la aplicación Streamlit.
- requirements.txt: contiene la lista de las librerías necesarias. 
- notebooks/: aquí se guarda el análisis exploratorio.
- vehicles_us.csv: contiene la información del dataset.

## Tecnologías utilizadas
Para esta aplicación utilice Python, Streamlite, Pandas, Plotly Express.

## Breve descripción de visualizaciones
- El histograma nos muestra la distribución del kilometraje de los vehículos.
- El gráfico de dispersión nos presenta la relación precio y kilometraje.

## Principales hallazgos del EDA
- Histograma: El resultado más alto que tenemos son 661 carros que cuentan con un kilometraje dentro de 98k a 99.999k. Entre mayor es el kilometraje, menor es la cantidad de carros que hay a la venta.
-Gráfico dispersión: Los carros con menor kilometraje son los que tienen un precio considerablemente alto, esto también depende del modelo del carro, ya que veo que hay uno que tiene 115km y su precio es de 375k.

## Aplicación desplegada

Puedes consultar la aplicación aquí:

[Ver aplicación en Render](https://cars-sales-app.onrender.com) 
# 📌 API Endpoints

Esta API permite gestionar productos e ingredientes, incluyendo su consulta, actualización y venta.

## 🍨🥤 Productos

### 🔹 Obtener todos los productos
**GET** `/productos`

### 🔹 Obtener un producto por ID
**GET** `/producto_id?id={id}`

### 🔹 Obtener un producto por nombre
**GET** `/producto_nombre?nombre={nombre}`

### 🔹 Obtener las calorías de un producto
**GET** `/producto_calorias?id={id}`

### 🔹 Obtener la rentabilidad de un producto
**GET** `/producto_rentabilidad?id={id}`

### 🔹 Obtener el costo de un producto
**GET** `/producto_costo?id={id}`

### 🔹 Vender un producto
**POST** `/vender_producto?id={id}`

## 🍓 Ingredientes

### 🔹 Obtener todos los ingredientes
**GET** `/ingredientes`

### 🔹 Obtener un ingrediente por ID
**GET** `/ingrediente_id?id={id}`

### 🔹 Obtener un ingrediente por nombre
**GET** `/ingrediente_nombre?nombre={nombre}`

### 🔹 Verificar si un ingrediente es sano
**GET** `/ingrediente_es_sano?id={id}`

### 🔹 Reabastecer un ingrediente
**POST** `/ingrediente_reabastecer?id={id}`

### 🔹 Renovar un ingrediente
**POST** `/ingrediente_renovar?id={id}`


Aquí tienes la documentación completa lista para ser agregada a un archivo global como `graphql_api_reference.md`, en un **solo bloque de código `.md`**:

````md
## 📡 Horus API (GraphQL)

Este documento describe cómo interactuar con los recursos en la API GraphQL mediante queries y mutations.

---

### 🔍 Consultas (Queries)

#### 🔹 Obtener todos los sensores

```graphql
query {
  sensors {
    id
    name
    x
    y
    z
    isvirtual
    description
    station_id
  }
}
````

##### 📝 Respuesta esperada:

```json
{
  "data": {
    "sensors": [
      {
        "id": 1,
        "name": "Sensor 1",
        "x": 10.5,
        "y": 5.0,
        "z": 3.2,
        "isvirtual": false,
        "description": "Sensor principal",
        "station_id": 1
      }
    ]
  }
}
```

---

#### 🔹 Obtener un sensor por ID

```graphql
query {
  sensor(id: 1) {
    id
    name
    x
    y
    z
    isvirtual
    description
    station_id
  }
}
```

---

### ✏️ Mutaciones (Mutations)

#### 🔹 Crear un sensor

```graphql
mutation {
  createSensor(input: {
    name: "Sensor X",
    x: 1.0,
    y: 2.0,
    z: 3.0,
    isvirtual: true,
    description: "Sensor virtual de prueba",
    station_id: 1
  }) {
    id
    name
  }
}
```

---

#### 🔹 Actualizar un sensor

```graphql
mutation {
  updateSensor(id: 1, input: {
    x: 11.0,
    y: 5.5
  }) {
    id
    name
    x
    y
  }
}
```

---

#### 🔹 Eliminar un sensor

```graphql
mutation {
  deleteSensor(id: 1)
}
```

##### 📝 Respuesta esperada:

```json
{
  "data": {
    "deleteSensor": true
  }
}
```

```


<?php
$nombreServidor = "localhost";
$nombreUsuario = "root"; 
$contrasena = ""; 
$nombreBaseDatos = "cuidado_gatos_db";

// Crear conexión
$conn = new mysqli($nombreServidor, $nombreUsuario, $contrasena, $nombreBaseDatos);

// Verificar la conexión
if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

$nombreGato = $_POST['nombre_gato'];
$responsable = $_POST['responsable'];

$sql = "INSERT INTO gatos (nombre_gato, responsable) VALUES ('$nombreGato', '$responsable')";

if ($conn->query($sql) === TRUE) {
    echo "Registro exitoso";
} else {
    echo "Error al registrar: " . $conn->error;
}

// Cerrar la conexión
$conn->close();
?>

<?php
error_reporting(0);
$nombre = $_POST['nombre1'];
$apellido =  $_POST['apellido1'];
$correo_electronico= $_POST['email1'];
$obra =  $_POST['obra1'];
$texto =  $_POST['texto11'];
$header = "Compra";

$mensaje = "Este mensaje fue enviado por " . $nombre . " " . $apellido . "\r\n";
$mensaje .= "Su e-mail es: " . $mail . " \r\n";
$mensaje .= "Obra" . $obra . " \r\n";
$mensaje .= "Comentario " . $texto . " \r\n";
$mensaje .= "Enviado el " . date('d/m/Y', time());

$para = gustitelez@hotmail.com;
$asunto = 'Compra';

mail($para, $asunto, utf8_decode($mensaje), $header);

echo 'mensaje enviado correctamente';

?>

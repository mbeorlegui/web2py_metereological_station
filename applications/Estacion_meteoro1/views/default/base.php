<?php
$con = mysqli_connect("localhost","", "", "");

if (mysqli_connect_errno()) { 
 echo "Error de MySQL: " . mysqli_connect_error(); 
 }

 $sql_func = ("Select* from t_registro_clima WHERE humedad");

 $res = mysqli_query($con, $sql_func)or die(mysql_error());
 $fila = mysqli_fetch_array($res); 

?>
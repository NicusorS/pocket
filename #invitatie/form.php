<html>
    <head>
    <title>Confirm</title>
    <style>
        
        a{color:#ffffff;
            text-decoration: none;
            
        }
        a:visited{
            color:#ffffff;
            
        }
        
        </style>
    </head>
<?php

$nume = $pers = "";

if(isset($_POST['submit']))
{

	$con = mysqli_connect("mysql.hostinger.ro","u831870946_costi","Vacanta-16","u831870946_nunta");
		
	if (!$con){
		die('Could not connect: ' . mysql_error());
	}
		else
		
		echo ('');

	mysqli_select_db( $con,"u136997149_nunta");
	
	$sqlCmd = sprintf("INSERT INTO nunta (Nume, Persoane) VALUES ('%s','%s')", 
		mysqli_real_escape_string($con, $_POST["nume"]),
		mysqli_real_escape_string($con, $_POST["pers"]));
	
	
	mysqli_query($con,$sqlCmd);
	
	$nume = $pers = "";

	mysqli_close($con);
}


     ?>
    
    <body style="background-color:pink">
        
        <div style="padding-top:65px; color:#ffffff; font-family:'Gill Sans', 'Gill Sans MT', 'Myriad Pro', 'DejaVu Sans Condensed', Helvetica, Arial, sans-serif; font-size:60px; font-weight:bold;">FANTASTIC!<br>NE VEDEM ACOLO :)</div>
        
    </body>
</html>
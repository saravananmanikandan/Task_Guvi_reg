
<?php
   // connect to mongodb
   $m = new MongoClient();
	
   echo "Connection to database successfully";
   // select a database
   $db = $m->Reg_guvi;
	
   echo "Database mydb selected";
?>

mongodb+srv://saravanan:<password>@cluster0.uasf7s8.mongodb.net/?retryWrites=true&w=majority
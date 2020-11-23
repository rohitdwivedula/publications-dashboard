<?php
	//PHP code to generate the verify button on the marks page. 
	echo"<form method='post' action='/verify.php'>
		<input type='submit' name='action' value='Verify'>
		<input type='hidden' name='eval_id' value='$eval_id'>
	</form>";
?>
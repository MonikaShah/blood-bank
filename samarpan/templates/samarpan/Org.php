<?php
/*
 *  CONFIGURE EVERYTHING HERE
 */

// an email address that will be in the From field of the email.

$from = 'rameshwar.g@stridessoftware.com';

// an email address that will receive the email with the output of the form

$sendTo = 'bo@samarpanbloodcentre.org';

//$sendTo = 'bo@samarpanbloodcentre.org';

// subject of the email
$subject = 'From :Samarpan website Organizer Reg.';

// form field names and their translations.
// array variable name => Text to appear in the email
$fields = array('txtCompany' => 'Organizer Name', 'txtLocation' => 'Contact Person Name', 'phone' => 'Phone', 'email' => 'Email', 'txtAddres' => 'Addres' ); 


// message that will be displayed when everything is OK :)

//$okMessage = 'Contact form successfully submitted. Thank you, I will get back to you soon!';
 
$okMessage = header("Location:http://www.stridessoftware.com/email_for_Partner_with_us_sent.html");

// If something goes wrong, we will display this message.
$errorMessage = 'There was an error while submitting the form. Please try again later';

/*
 *  LET'S DO THE SENDING
 */

// if you are not debugging and don't need error reporting, turn this off by error_reporting(0);
error_reporting(E_ALL & ~E_NOTICE);

try
{

    if(count($_POST) == 0) throw new \Exception('Form is empty');
            
    $emailText = "Mail From Samarpan Blood bank website in Organizer page \n\n\n";

    foreach ($_POST as $key => $value) {
        // If the field exists in the $fields array, include it in the email 
        if (isset($fields[$key])) {
            $emailText .= "$fields[$key]: $value \n\n";
        }
    }

    // All the neccessary headers for the email.
    $headers = array('Content-Type: text/plain; charset="UTF-8";',
        'From: ' . $from,
        'Reply-To: ' . $from,
        'Return-Path: ' . $from,
    );
    
    // Send email
    mail($sendTo, $subject, $emailText, implode("\n", $headers));

    $responseArray = array('type' => 'success', 'message' => $okMessage);
}
catch (\Exception $e)
{
    $responseArray = array('type' => 'danger', 'message' => $errorMessage);
}


// if requested by AJAX request return JSON response
if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
    $encoded = json_encode($responseArray);
	
    header('Content-Type: application/json');

    echo $encoded;
}

// else just display the message
else {
    echo $responseArray['message'];
	
}

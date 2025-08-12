<?php

$calculus = "pipi";
	
   preg_match_all("/([a-z_]+)/", strtolower($calculus), $words);
   $words = $words[0];
 
   $accepted_words = ['base_convert', 'pi'];
   $alphabet = str_split('_abcdefghijklmnopqrstuvwxyz0123456789.+-*/%()[],');
 
//    var_dump($calculus);
    print_r($words);
 
   $safe = true;
   for ($i = 0; $i < count($words); $i++) {
       if (strlen($words[$i]) && (array_search($words[$i], $accepted_words) === false)) {
           $safe = false;
           echo $words[$i]."\n";
           die("Failed here\n");
       }
   }

 
   for ($i = 0; $i < strlen($calculus); $i++) {
       if (array_search($calculus[$i], $alphabet) === false) {
           $safe = false;
           echo $calculus[$i]."is not in alphabet\n";
           die("Failed in advanced\n");
       }
   }
 
   if (strlen($calculus) > 256) return "Expression too long.";
   $ans = '';
   if (($safe) === false) $ans = "This calculus is not safe.";
   else eval('$ans=' . $calculus . ";");
?>
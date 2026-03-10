---
layout: default
title: Perl-Command-Injection
---
In this challenge we get this `perl` source code. The challenge is very similar to [natas19](../../overthewire/natas/natas19.md).

```perl
#!/usr/bin/perl

delete @ENV{qw(IFS CDPATH ENV BASH_ENV)};
$ENV{'PATH'}='/bin:/usr/bin';

use strict;
use warnings;

main();

sub main {
    my ($file, $line) = @_;

    menu();
    prompt();

    while((my $file = <STDIN>)) {
        chomp $file;

        process_file($file);

        prompt();
    }
}

sub prompt {
    local $| = 1;
    print ">>> ";
}
sub menu {
    print "*************************\n";
    print "* Stat File Service    *\n";
    print "*************************\n";
}

sub check_read_access {
    my $f = shift;

    if(-f $f) {
        my $filemode = (stat($f))[2];

        return ($filemode & 4);
    }

    return 0;
}

sub process_file {
    my $file = shift;
    my $line;
    my ($line_count, $char_count, $word_count) = (0,0,0);

    $file =~ /(.+)/;
    $file = $1;
    if(!open(F, $file)) {
        die "[-] Can't open $file: $!\n";
    }


    while(($line = <F>)) {
        $line_count++;
        $char_count += length $line;
        $word_count += scalar(split/\W+/, $line);
    }

    print "~~~ Statistics for \"$file\" ~~~\n";
    print "Lines: $line_count\n";
    print "Words: $word_count\n";
    print "Chars: $char_count\n";

    close F;
}
```

We can see it uses the function `open(F, $file)` on the input we give.
This can be vulnerable, if we give `|` and then some command, it executes the command and pipe the output to the stdout.

![[Pasted image 20260310172223.png]]

We can simply give the input `|cat .passwd`, and grab the password, in our case **PerlCanDoBetterThanYouThink**


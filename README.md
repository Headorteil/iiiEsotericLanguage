# iii Esoteric Language

I made this python esoteric language interpreter for my esoteric language : iii which have the particularity to have his programms only composed by the character i.

This interpreter use a BrainFuck python interpreter and the synthax of iii and BrainFuck are in bijection, so whatewer can do BrainFuck, iii cans also do.

Also to note : BrainFuck is turing complete, so iii is. That means, with an infinite amount of ressources, any computable programe can be written in iii.

PS : Maybe the programms files of iii are a little bit heavy ^^ (A programm which print "Hello World!" is written with a file that contains 11394260736961616017478696325142642241587016089942641935756584435039981423330228839638374655156139739 i), but i implemented that a way you can play with the number of i and not necessarly the file itself.

```
usage: iiiEsotericHeadorteil.py [-h] [-a A] [-n N] [-p P] [-o O] [-e] [-d]
                                [-c]

iii Encoder/Decoder/Executer (deals with BrainFuck)

optional arguments:
  -h, --help  show this help message and exit
  -a A        Specify/Print the string of your BrainFuck program (input or
              output) give this option "yes" if it is use for an output
  -n N        Specify/Print the number of i your programm would contain (if
              you don'precise this option in -c mode, be careful, iii
              programms can be really huge and you may have an overflow error)
              (input or output) give this option "yes" if it is use for an
              output
  -p P        Specify the path of your iii file (input or output)
  -o O        Specify the path of your BrainFuck file(input or output)
  -e          Execute your programm
  -d          Convert your iii program to BrainFuck
  -c          Convert your BrainFuck program to iii

Examples :
$ ./iiiEsotericHeadorteil.py -c -a"++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>." -n"yes"
$ ./iiiEsotericHeadorteil.py -d -n11394260736961616017478696325142642241587016089942641935756584435039981423330228839638374655156139739 -o"yes"
$ ./iiiEsotericHeadorteil.py -e -n11394260736961616017478696325142642241587016089942641935756584435039981423330228839638374655156139739
```

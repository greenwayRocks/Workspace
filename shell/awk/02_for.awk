#!/usr/bin/awk -f

BEGIN { print "Here's your for loop!" }

{
  for (i=1; i<= 10; i++) {
    printf("Counter is now: %d\n", i);
  }
  exit
}

END { print "The loop ends here and now ..." }

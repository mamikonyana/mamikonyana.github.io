#!/bin/bash

for file in `find templates/ml_afternoon -type f`; do
  if ! grep '{% raw %}' $file &> /dev/null ; then
    perl -pi -e 'print "{% raw %}\n\n" if $. == 1' $file
    echo '{% endraw %}' >> $file
  fi
done

for file in `find templates/ml_evening -type f`; do
  if ! grep '{% raw %}' $file &> /dev/null ; then
    perl -pi -e 'print "{% raw %}\n\n" if $. == 1' $file
    echo '{% endraw %}' >> $file
  fi
done

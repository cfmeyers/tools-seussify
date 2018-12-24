

[Silly words](https://github.com/veltman/gobblefunk/blob/master/lib/words.json) taken from https://github.com/veltman/gobblefunk.


# Usage

```bash
echo "SELECT * FROM etl.raw_pixel" | python seussify.py
>> SELECT * FROM swogswallowed.skritz
```

If the path to your repo is `/Users/me/dev/tools/seussify`, then adding this to your .vimrc:

```
fun! Seussify() range
  :'<,'>: !/Users/me/dev/tools/seussify/env/bin/python /Users/me/dev/tools/seussify/seussify.py
endfun
vnoremap ,s :call Seussify()<cr>
```
gives you the ability to transform visually-selected SQL.

let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd /var/shared/Projects/tinyhouse/server
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 src/index.ts
badd +7 src/database/index.ts
badd +12 src/lib/types.ts
badd +1 temp/seed.ts
badd +34 src/graphql/resolvers.ts
badd +1 .env
badd +35 term:///var/shared/Projects/tinyhouse/server//2639:npm\ run\ start
badd +1 /var/shared/Projects/tinyhouse/server/
argglobal
%argdel
$argadd /var/shared/Projects/tinyhouse/server/
argglobal
if bufexists("term:///var/shared/Projects/tinyhouse/server//2639:npm\ run\ start") | buffer term:///var/shared/Projects/tinyhouse/server//2639:npm\ run\ start | else | edit term:///var/shared/Projects/tinyhouse/server//2639:npm\ run\ start | endif
if &buftype ==# 'terminal'
  silent file term:///var/shared/Projects/tinyhouse/server//2639:npm\ run\ start
endif
balt src/index.ts
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 16) / 33)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0&& getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOFc
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
let g:this_session = v:this_session
let g:this_obsession = v:this_session
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :

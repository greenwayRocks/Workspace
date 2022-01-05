let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Workspace/react/02_fullstack-react/02_time_tracking_app
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 public/index.html
badd +1 data.json
badd +33 term://~/Workspace/react/02_fullstack-react/02_time_tracking_app//4756:npm\ run\ start
argglobal
%argdel
$argadd ./
argglobal
if bufexists("term://~/Workspace/react/02_fullstack-react/02_time_tracking_app//4756:npm\ run\ start") | buffer term://~/Workspace/react/02_fullstack-react/02_time_tracking_app//4756:npm\ run\ start | else | edit term://~/Workspace/react/02_fullstack-react/02_time_tracking_app//4756:npm\ run\ start | endif
if &buftype ==# 'terminal'
  silent file term://~/Workspace/react/02_fullstack-react/02_time_tracking_app//4756:npm\ run\ start
endif
balt data.json
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 33 - ((25 * winheight(0) + 13) / 26)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 33
normal! 018|
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

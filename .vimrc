" ── General ──────────────────────────────────────────────
set nocompatible              " ditch Vi compatibility
set encoding=utf-8
set history=500

" ── UI ───────────────────────────────────────────────────
set number                    " line numbers
set relativenumber            " relative numbers (great for motions)
set cursorline                " highlight current line
set signcolumn=yes            " always show sign column (no layout shift)
set scrolloff=8               " keep 8 lines above/below cursor
set sidescrolloff=8
set nowrap                    " no line wrapping
set showmatch                 " briefly jump to matching bracket
set wildmenu                  " enhanced tab completion in command mode
set laststatus=2              " always show status line
set ruler                     " show cursor position
set showcmd                   " show partial command in status line

" ── Search ───────────────────────────────────────────────
set hlsearch                  " highlight search results
set incsearch                 " search as you type
set ignorecase                " case insensitive...
set smartcase                 " ...unless you type a capital

" ── Indentation ──────────────────────────────────────────
set expandtab                 " spaces not tabs
set tabstop=2
set shiftwidth=2
set softtabstop=2
set autoindent
set smartindent

" ── Behavior ─────────────────────────────────────────────
set hidden                    " switch buffers without saving
set updatetime=300            " faster CursorHold events
set timeoutlen=500            " snappier key sequence timeout
set backspace=indent,eol,start
set clipboard=unnamed         " yank to system clipboard (macOS)
set mouse=a                   " mouse support
set autoread                  " reload files changed outside vim

" ── Swap / backup ────────────────────────────────────────
set noswapfile
set nobackup
set nowritebackup

" ── Clear search highlight with Escape ───────────────────
nnoremap <Esc> :nohlsearch<CR>

" ── Better split navigation ──────────────────────────────
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

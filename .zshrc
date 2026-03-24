

# quickly edit+resource this
zconf() {
  vim ~/.zshrc
  source ~/.zshrc
  echo "🔄 .zshrc refreshed"
}


tcuts() {
  vim ~/.talon/user/nick/shortcuts.talon
}
tsettings() {
  vim ~/.talon/user/nick/settings.talon
}
tconf() {
  vim ~/.talon/user/nick/shortcuts.talon
}
tcorrections() {
  vim ~/.talon/user/nick/corrections.py
}
tvocab() {
  vim ~/.talon/user/nick/vocabulary.py
}

alias ex=exit
mcd() {
  mkdir "$1" && cd "$1"
}
alias grba='git rebase --abort'
alias grbc='git rebase --continue'

alias gcm='git commit -m'
alias gc='git commit'
Ml() {
  git checkout main
  git pull
}
alias gca='git commit --amend'
alias gs='git status'
alias gd='git diff'
alias gds='git diff --staged'

gpr() {
  local BRANCH="$(git branch --show-current)"
  echo "Pushing to [$BRANCH]"
  sleep 1
  git push origin $BRANCH $@
}

gprf() {
  echo 'WARNING!! Force-pushing'
  sleep 1
  gpr --force
}

fpath+=("$(brew --prefix)/share/zsh/site-functions")
autoload -U promptinit; promptinit
prompt pure

# modern shell replacements
alias cat=bat
alias ls=lsd

# mcfly https://github.com/cantino/mcfly
eval "$(mcfly init zsh)"

export PATH="$PATH:$HOME/.local/bin"

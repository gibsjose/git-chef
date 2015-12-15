# Git Chef

`git chef` is a helpful, searchable collection of common `git` questions, incorporated right into your existing `git` workflow.

To use `git chef`, simply feed it a description of what you want to do. For example:
```bash
git chef 'squash last n commits'
```

or

```bash
git chef 'reword last commit message'
```

If more than one recipe is found that matches your description, you will be prompted to choose from the matching recipes.

## Cookbooks
`git chef` comes with a set of recipes all contained in the master 'cookbook'. These recipes are indexed and searched by description when you need help executing a `git` command.

You can also add your own cookbooks with your own commands, or replace the master cookbook recipes with your own.

## Recipes
Recipes are simply a `<recipe_name>.chef` file that lives in your cookbook directory. The recipes follow a simple standard format with four types of instructions.

```bash
# <description>

> <examples>

! <caveats> # (optional)

@ <tags> # (optional)
```

The examples are usually just a single command, but can also include multiple commands and bash-style comments (starting with `#`).

So a pretty simple recipe for rewording the last commit message might look like this:
```bash
# reword last commit message

> git commit --amend -m '<new message>'

@ reword, commit, amend, last commit
```

And a more complicated example for squashing the last N commits might look like this:
```bash
# squash last n commits

> git rebase -i HEAD ~<N> #Where <N> is number of commits to be squashed
> # 1) Leave latest commit as `pick`
> # 2) Change all others to `squash`
> # 3) Save and edit commit message

! If already pushed, push changes with:
! git push origin +master

@ squash, n, rebase
```

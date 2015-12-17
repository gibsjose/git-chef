# Git Chef

`git chef` is a helpful, searchable collection of answers to common `git` questions, incorporated right into your existing `git` workflow. It was inspired by the frustration of constantly forgetting some of those pesky complicated `git` commands.

## Using `git chef`
To use `git chef`, simply feed it a description of what you want to do. For example:
```bash
git chef 'squash last n commits'
```

or

```bash
git chef 'reword last commit message'
```

`git chef` will then find a matching recipe and tell you which `git` commands you will need!

## Searching
You can use natural language when searching for a matching recipe, like this:
```bash
git chef 'squash last 2 commits'
```

or

```bash
git chef 'combine last n commits'
```

or

```bash
git chef 'merge a bunch of commits together'
```

When you use `git chef` for the first time it will first index all the cookbooks/recipes, which may take some time. If you add cookbooks or recipes, run `git chef index` to re-run the indexing to search the new recipes.

That's all you need to know, unless you would like to [Contribute](#contributing), in which case you will need to read up on cookbooks and recipes.

## Contributing
Want to contribute a useful recipe or cookbook? Great! Just fork this repo, add your changes and submit a pull request.

Before contributing, please read the sections below on [Cookbooks](#cookbooks) and creating [Recipes](#recipes). There is also a section on [Example Recipes](#example-recipes) to get you started.

Also see the note above about running `git chef index` after making additions locally.

## Cookbooks
`git chef` comes with a set of base *recipes* contained in the master *cookbook*. These recipes are indexed and searched by their description when you need help executing a `git` command.

You can also add your own cookbooks or edit/replace the master cookbook recipes with your own.

`git-chef` will first search the master cookbook and will then search subsequent cookbooks in alphabetic order.

## Recipes
Recipes are simply a `<recipe_name>.chef` file that lives in your cookbook directory. You can name a new recipe whatever you want, as long as it is not already taken within the same cookbook.

The recipes follow a simple format with six types of instructions:

```bash
# description       # (REQUIRED)

> commands          # (REQUIRED)
~ examples          # (optional)
* comments          # (optional)

! caveats           # (optional)

@ tags              # (optional)
```

### Description
A concise description of the command. This should be as descriptive as possible while remaining brief.

Some good description examples:
```bash
# Merge two branches

# Create a new branch

# Change remote url
```

You can have as many description lines as you would like, but only the first line will be indexed. Subsequent lines will be treated as comments.

> Descriptions are prefixed with a `#` character.

### Commands
Many `git` actions are solved by a single command. For example, to create a new branch from the current one, use the syntax:
```bash
> git checkout -b <new_branch>
```

However, this could also be written more verbosely as two commands:
```bash
> git checkout <existing_branch>
> git checkout -b <new_branch>
```

The `>` character denotes the *syntax* of a command, while the `~` character is an example of the command. Command examples are often helpful, but are completely optional. A command may have as many examples as desired. Examples are considered to be associated with the command most-directly above them.

So the previous example could be expanded with example commands like this:
```bash
> git checkout <existing_branch>
~ git checkout master
> git checkout -b <new_branch>
~ git checkout -b develop
```

You may also add extra information to the commands by adding a comment beneath the command, prefixed by `*`:
```
> git checkout <existing_branch>
~ git checkout master
* Skip if you are already on the desired existing branch
> git checkout -b <new_branch>
~ git checkout -b develop
* Will create a new branch called <new_branch> from <existing_branch>
```

You may have comments without preceding commands, or commands without a subsequent comment. If a command has more than one comment, all subsequent comments (until the next command) are associated with it.

It is often necessary to provide a variable argument to one or more commands. To keep things consistent, these should be surrounded in brackets `<...>`.

For example, to rebase the last `N` commits, the command should look like:
```bash
> git rebase -i HEAD~<N>
```

Or when a branch name is required as part of the command:
```bash
> git branch -d <branch>
```

In these cases, adding an example command can be very helpful. The syntax-example-comment (`>` - `~` - `*`) flow is a great way of defining a command clearly, although you may describe the command any way you would like, as long as the **syntax** element is present.

In the event the `git` action requires multiple commands, the commands (and optional comments) should be listed in the order they are meant to be executed in. Non-command actions (e.g. 'modify the commit message') should be listed as a series of comments.

> Commands are prefixed with a `>` character.

> Examples are prefixed with a `~` character.

> Comments are prefixed with a `*` character.

### Caveats
Caveats are an **optional** (but often helpful) component to a recipe. They can be used in addition to command comments to define actions or commands someone may need to do perform under certain conditions, or give warnings/information about how the command works.

For example, when squashing commits, if the commits have already been pushed, you have to push them again after squashing using a special syntax (a `+`, to force the branch refspec). This could be listed as a caveat as follows:
```bash
! If already pushed, push changes with:
!   git push <remote> +<branch>
! ex:
!   git push origin +master
```

Of course, this could also have been included as a comment in the command section, but it is up to the chef to decide whether it is a *comment* or a *caveat*. To help with that decision, the chef should know that caveats are displayed to the user in a more warning-like fashion.

> Caveats are prefixed with a `!` character.

### Tags
Tags are also an **optional** component to a recipe. They are used as helpful indicators in addition to the description when searching for `git` actions.

You may define individual tags on each line:
```bash
@ remote
@ url
@ ...
```

or as a comma-separated list on one line:
```bash
@ remote, url, ...
```

> Tags are prefixed with a `@` character.

### Recipe Examples
A pretty simple recipe for rewording the last commit message might look like this:
```bash
# reword last commit message

> git commit --amend -m '<new message>'

@ reword, commit, amend, message
```

And a more complicated example for squashing the last N commits might look like this:
```bash
# squash last n commits

> git rebase -i HEAD~<N>
* <N> is number of commits to be squashed

* 1) Leave latest commit as `pick`
* 2) Change all others to `squash`
* 3) Save and edit commit message

! If already pushed, push changes with:
!   git push <remote> +<branch>
! ex:
!   git push origin +master

@ squash, n, rebase, commits, merge, combine
```

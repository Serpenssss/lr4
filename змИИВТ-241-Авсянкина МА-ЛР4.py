yuliy@Asus_TUF MINGW64 ~
$ ssh-keygen -t ed25519 -C "lr4 <aowbdj@gmail.com>"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/c/Users/yuliy/.ssh/id_ed25519):
/c/Users/yuliy/.ssh/id_ed25519 already exists.
Overwrite (y/n)? y
Enter passphrase for "/c/Users/yuliy/.ssh/id_ed25519" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/yuliy/.ssh/id_ed25519
Your public key has been saved in /c/Users/yuliy/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:RNEgFflklk89UWCsXnHm5EI9Rs8oU1jX9NObnosJiKs lr4 <aowbdj@gmail.com>
The key's randomart image is:
+--[ED25519 256]--+
|      ..** . =BB=|
|       o. * oo**X|
|        .= ooooX*|
|       .  . ooo *|
|        S  . . + |
|        . . . . .|
|       . . .   o |
|        .   . o .|
|     E..     o . |
+----[SHA256]-----+

yuliy@Asus_TUF MINGW64 ~
$ ^C

yuliy@Asus_TUF MINGW64 ~
$ eval "$(ssh-agent -s)"
Agent pid 797

yuliy@Asus_TUF MINGW64 ~
$ ssh-add ~/.ssh/id_ed25519
Identity added: /c/Users/yuliy/.ssh/id_ed25519 (lr4 <aowbdj@gmail.com>)

yuliy@Asus_TUF MINGW64 ~
$ cd "C:\Users\yuliy\Documents\LR4"

yuliy@Asus_TUF MINGW64 ~/Documents/LR4
$ git init
Initialized empty Git repository in C:/Users/yuliy/Documents/LR4/.git/

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (master)
$ git config --global --add safe.directory "C:\Users\yuliy\Documents\LR4"

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (master)
$ git checkout -b LR4-AMA
Switched to a new branch 'LR4-AMA'

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git status
On branch LR4-AMA

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        AMA.txt

nothing added to commit but untracked files present (use "git add" to track)

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git add AMA.txt

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git status
On branch LR4-AMA

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   AMA.txt


yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git add .

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git commit -m "Отправлен локально созданный файл AMA.txt на удаленный репозиторый."
[LR4-AMA (root-commit) 7c71d0f] Отправлен локально созданный файл AMA.txt на удаленный репозиторый.
 1 file changed, 6 insertions(+)
 create mode 100644 AMA.txt

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git remote add origin https://github.com/Serpenssss/lr4.git

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git fetch origin
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 9 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (9/9), 3.29 KiB | 153.00 KiB/s, done.
From https://github.com/Serpenssss/lr4
 * [new branch]      LR4-AMA    -> origin/LR4-AMA
 * [new branch]      main       -> origin/main

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> LR4-AMA


yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git merge origin/LR4-AMA --allow-unrelated-histories
Merge made by the 'ort' strategy.
 README.md | 10 ++++++++++
 1 file changed, 10 insertions(+)
 create mode 100644 README.md

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> LR4-AMA


yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git push --set-upstream origin LR4-AMA
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 859 bytes | 859.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Serpenssss/lr4.git
   a53c9e4..2018340  LR4-AMA -> LR4-AMA
branch 'LR4-AMA' set up to track 'origin/LR4-AMA'.

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git status
On branch LR4-AMA
Your branch is up to date with 'origin/LR4-AMA'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   AMA.txt

no changes added to commit (use "git add" and/or "git commit -a")

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git add AMA.txt

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git commit -m "Добавление данных о среднем балле по предыдущему образованию."
[LR4-AMA 6ce11f1] Добавление данных о среднем балле по предыдущему образованию.
 1 file changed, 1 insertion(+)

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 459 bytes | 459.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Serpenssss/lr4.git
   2018340..6ce11f1  LR4-AMA -> LR4-AMA

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git status
On branch LR4-AMA
Your branch is up to date with 'origin/LR4-AMA'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   AMA.txt

no changes added to commit (use "git add" and/or "git commit -a")

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git add AMA.txt

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git commit -m "Добавление данных о месте рождения."
[LR4-AMA 038bfb0] Добавление данных о месте рождения.
 1 file changed, 1 insertion(+)

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 424 bytes | 424.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Serpenssss/lr4.git
   6ce11f1..038bfb0  LR4-AMA -> LR4-AMA

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git log
commit 038bfb0547c0a04b5c8f42b7bfdfdaf1e64fec41 (HEAD -> LR4-AMA, origin/LR4-AMA)
Author: Serpenssss <aowbdj@gmail.com>
Date:   Tue Dec 10 00:20:04 2024 +0500

    Добавление данных о месте рождения.

commit 6ce11f198f179282da1716a6778bc438489779ab
Author: Serpenssss <aowbdj@gmail.com>
Date:   Tue Dec 10 00:15:52 2024 +0500

    Добавление данных о среднем балле по предыдущему образованию.

commit 2018340b94c79f5ad5ea8ad2ed4a4f94dad449f7
Merge: 7c71d0f a53c9e4
Author: Serpenssss <aowbdj@gmail.com>
Date:   Tue Dec 10 00:09:19 2024 +0500

    Merge remote-tracking branch 'origin/LR4-AMA' into LR4-AMA

commit 7c71d0fc5c0364c06cf28c9dc7a36adbf6ac2354
Author: Serpenssss <aowbdj@gmail.com>
Date:   Tue Dec 10 00:05:04 2024 +0500

    Отправлен локально созданный файл AMA.txt на удаленный репозиторый.

commit a53c9e4d455b9c5b2898a3383c6f082f48899b44
Author: Serpenssss <aowbdj@gmail.com>
Date:   Mon Dec 9 23:48:34 2024 +0500

    Update README.md

commit fa4139aba48c44dae51d85d1c245e5313243c25b (origin/main)
Author: Serpenssss <aowbdj@gmail.com>
Date:   Mon Dec 9 23:44:01 2024 +0500

    Update README.md

commit 203b7a2ddc16b29598fa8865ced7c45a9549162c
Author: Serpenssss <aowbdj@gmail.com>
Date:   Mon Dec 9 23:42:21 2024 +0500

    Initial commit

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git revert 038bfb0547c0a04b5c8f42b7bfdfdaf1e64fec41
[LR4-AMA 5c0c6ac] Revert "Добавление данных о месте рождения."
 1 file changed, 1 deletion(-)

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git add .

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 381 bytes | 381.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Serpenssss/lr4.git
   038bfb0..5c0c6ac  LR4-AMA -> LR4-AMA

yuliy@Asus_TUF MINGW64 ~/Documents/LR4 (LR4-AMA)
$

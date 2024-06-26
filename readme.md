## commitログを確認(IDもここから)

```
git log --oneline
```

## 特定のファイルのみコミットしたい時

```
git add <ファイルのパス>
```

## コミットした内容をローカルで確認したい時

```
git checkout <コミットID>
```

## 特定のコミットを取り消したい時
履歴を保持したまま安全に変更を取り消したい場合:<br>
(前のコミットを残したまま、新たに「変更前のファイル内容に戻したrevertコミット」を作成)
</br>
```
git revert <コミットID>
```

## 最新のコミットを取り消したい時
### soft
最新のコミットを取り消す。ステージング(git addされた状態)には残ってて作業ディレクトリは変更しない。<br>
コミットメッセージを変更したいときに便利
</br>
<br>
```
git reset --soft HEAD~1
```
</br>

### mixed
最新のコミットが取り消されステージングから削除される。作業ディレクトリは変更しない<br>
```
git reset --mixed HEAD~1
```
</br>

### hard
最新のコミットが取り消されステージングエリアから削除されるだけでなく作業ディレクトリからもその変更が消される<br>
```
git reset --hard HEAD~1
```
</br>

## rebaseについて
mainブランチの変更と現在のブランチの変更を「統合」し新たな「マージコミット」を作成。非線形な変更<br>
```
git merge main
```
</br>

main ブランチの最後のコミットの上に現在の変更を適用。線形な変形<br>
```
git rebase main
```
</br>

### コミットしたくないけどブランチ変えたい時
```
git stash push -m "<stashメッセージ>"
```

stashすると変更されたファイルは一時的に退避され、一つ前のコミットの状態になる。(他のブランチに移動できる)

元のブランチに戻り、変更したファイルの状態を戻したい時<br>
```
git stash pop
```
</br>


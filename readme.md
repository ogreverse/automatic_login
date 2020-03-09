# 注意事項
* Macで使われることを想定してます。
* (重要) コマンドを叩いてもブラウザが開かない場合は、その都度chromedriverをアップデートしてください。

# セットアップ

## python3 (インストールされているはず)
```
# 確認
$ python3 --version
```
入っていない場合はインストールしておく。

## chromedriverインストール
```
$ brew cask install chromedriver
```

---

# 使い方 (awsログインの場合)

## ファイルコピーと編集
* aws以下のファイルを任意のディレクトリにコピーする。
* login_foo.commandのファイル名を任意のAWSアカウント名に変える。<br>
  (e.g. login_service.command)
* login_foo.command内の"FOO"の部分を任意のAWSアカウント名に変える。<br>
```
(e.g.)
cd `dirname $0`
./login_aws.py SERVICE
exit
```

## 環境変数定義
シェル起動時の設定ファイル(~/.bashrcや~/.zshrcなど)に、<br>
以下のように起動時にAWSアカウント情報を環境変数として設定するようにする。<br>
(FOOは任意のアカウント名に置き換える)
```
export AWS_FOO_ACCOUNT="1234567891234"
export AWS_FOO_USERNAME="user_no_namae"
export AWS_FOO_PASSWORD="PaSSworD"
```

## 実行
login_foo.commandを実行(もしくはspotlightで "login_foo.command" を実行)

---

# 使い方 (githubログインの場合)
awsと使い方は同じ。

環境変数は
```
export GITHUB_FOO_USERNAME="user_name"
export GITHUB_FOO_PASSWORD="PasSWord"
```
のようになる。
